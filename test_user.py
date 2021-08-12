from interface import Interface
from myRedis import Redis
import pytest
import json
import time
import random
import hmac, base64, struct, hashlib, time


inter = Interface()
redis = Redis()    

def getVerifyCodeImage():#获取验证码id
    code = inter.getVerifyCodeImage()
    # print("获取验证码ID:",code)
    return code

def getRedis():#获取验证码从Redis
    code = getVerifyCodeImage()
    rdis = Redis()
    value = "verify_code_id_"+code
    verify = eval(rdis.client.get(value))
    # print("获取验证码从Redis:",verify)
    return code,verify

def loginTrue():#登录正则提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest1","qwer`123",code,verify)
    # print("^^^^^^^",Response.json())
    token = Response.json()['data']['token']
    # print("token:",Response.json()['data']['token'])
    return token


#拼接含有token的headers
token = redis.activateToken(loginTrue())
# print("激活后的token:",token)
# headers = {'Authorization': 'Bearer '+token}
#headers.update({'resourceId':resourceId})#接口headers需要resourceId
# print(headers) 


#创建新用户，最后用新用户登录
Random = str(random.randint(0,100))#随机数
#1、创建一个superadmin的用户组
headers = {'Authorization': 'Bearer '+token}
roles = inter.getGroupRoles(id="1",headers=headers)#获取用户组角色列表，id默认1
role_names = list(map(lambda x:x['name'],roles.json()['data']))
# print(role_names)
title = "Group"+Random
group = inter.createGroup(title=title,roles=role_names,parentId="1",headers=headers)

# print("获取Group返回：")
# print(group.json())#获取返回

group_id = group.json()['data']['id']# 获取新用户组id
# print("拿到新用户组id:")
# print("group_id:",group_id)
#2、创建新的用户，并关联新的用户组
username = "Username"+Random    #随机用户名
password = "qwer`123"           #固定密码
email = username+"@qaceshi.to"  #随机邮箱地址
name = "Michael_Test"+Random    #随机姓名
enabled = True  #是否强制修改密码: true:不强制修改密码; false: 强制修改密码
user_new = inter.createUser(username=username,
                            password=password,
                            email=email,
                            name=name,
                            enabled=enabled,
                            headers=headers)
# print("创建新用户返回:\n",user_new.json())
#3、从用admin用户列表中获取刚刚创建的id
response_userList = inter.getUsers(headers=headers).json()
#print(response_userList)
for x in response_userList["data"]:
    if x["username"] == username:
        # print(x["id"],x["username"])
        user_newId = str(x["id"])
        user_newName = x["username"]
    
#4、获取用户组信息编辑，关联上新的用户
group_id = str(group_id)
group_info = inter.getGroupInfo(id=group_id,headers=headers)
title_old = group_info.json()["data"]["title"]
roles_old = list(map(lambda x:x['id'],group_info.json()['data']['roles']))
groupuser_old = list(map(lambda x:x['id'],group_info.json()['data']['groupUsers']))
# print("获取用户组返回：")
# print(group_info.json())
# print("获取Old用户组信息：")
# print("title_old:",title_old)
# print("roles_old:",roles_old)
# print("groupuser_old:",groupuser_old)
#添加新的用户id
groupuser_old.append(user_newId)
# print("user_newId:",user_newId)
# print("groupuser_old:",groupuser_old)
edit_groupInfo = inter.editGroupInfo(groupId=group_id,title=title_old,roles=roles_old,groupUsers=groupuser_old,headers=headers)
# group_info = inter.getGroupInfo(id=group_id,headers=headers)
# print("查看修改后的用户组返回：",group_info.json())

#5、给新用户绑定二步验证
#获取二步验证的密钥
secret = inter.getQRBarcode(username=username,headers=headers)
secretKey = secret.json()['data']['secret']
# print("QR Response:",secret.json())#获取QR返回
# print("secret:",secretKey)
secretKey = str(secretKey)

def calGoogleCode(secret_key):
    """
    基于时间的算法
    :param secret_key:
    :return:
    """
    # 密钥长度非8倍数，用'='补足
    # lens = len(secret_key)
    # lenx = 8 - (lens % 4 if lens % 4 else 4)
    # secret_key += lenx * '='
    # print(secret_key)
   
    decode_secret = base64.b32decode(secret_key, True)
    # 解码 Base32 编码过的 bytes-like object 或 ASCII 字符串 s 并返回解码过的 bytes。

    interval_number = int(time.time() // 30)

    message = struct.pack(">Q", interval_number)
    digest = hmac.new(decode_secret, message, hashlib.sha1).digest()
    index = ord(chr(digest[19])) % 16   # 注：网上材料有的没加chr，会报错
    google_code = (struct.unpack(">I", digest[index:index + 4])[0] & 0x7fffffff) % 1000000

    return "%06d" % google_code

googleCode = calGoogleCode(secretKey)#获取二步验证码
# print("\n Code:",googleCode,type(googleCode))
#绑定二步验证
bindTFA = inter.bindTFA(id=user_newId,secret=secretKey,code=googleCode,headers=headers)
# print("绑定二步验证返回:",bindTFA.json())
#6、用新创建的用户登录
def test_NewUser():
    code = inter.getVerifyCodeImage()
    value = "verify_code_id_"+code
    rdis = Redis()
    verify = eval(rdis.client.get(value))
    res = inter.loginUser(username=user_newName,password=password,verifyCodeId=code,verifyCode=verify)
    # print(res.json())
    assert res.json()['success'] == True