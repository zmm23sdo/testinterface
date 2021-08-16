from requests.models import Response
from interface import Interface
from myRedis import Redis
import pytest
import json
import time
import random

#登录准备：
inter = Interface()
redis = Redis()    

def raddomPhone():#随机生成不重复的手机号
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189"]
    phoneNum = random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))
    return phoneNum


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


#######设置新的用户#####
username_test = "mingvtest2"
#######设置新的用户#####


def loginTrue():#登录正则提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser(username_test,"qwer`123",code,verify)
    # print("^^^^^^^",Response.json())
    token = Response.json()['data']['token']
    # print("token:",Response.json()['data']['token'])
    return token
#激活token
token = redis.activateToken(loginTrue())
print("可使用的激活token：",token)
#创建新用户，最后用新用户登录
Random = str(random.randint(0,100))#随机数
#拼接含有token的headers
headers = {'Authorization': 'Bearer '+token}


#1、创建卖家账户
name = "dealerSeller"+ Random
email = name + "@qacehi.to"
phonePrefix = "+86"
phoneNumber = raddomPhone()

dealerSeller = inter.addCorpSeller(name=name,email=email,phonePrefix=phonePrefix,phoneNumber=phoneNumber,headers=headers)
# print("创建Seller返回：",dealerSeller.json())
#2、指派Executive
#查询获取可查看审核人
executiveSeller = inter.getSellerExecutive(headers=headers)
# print("查询获取可查看审核人返回：",executiveSeller.json())
executiveSeller_list = executiveSeller.json()
#获取登录的用户作为审核人
for x in executiveSeller_list["data"]:
    if x["name"] == username_test:
        # print(x["id"],x["name"])
        user_executiveSellerId = str(x["id"])
        # print("查询获取可查看审核人id：",user_executiveSellerId)
        break
#查询seller
querySeller = inter.querySellerAccount(pageSize=100,current=1,headers=headers)
#print("查询Seller的返回：",querySeller.json())
querySeller_list = querySeller.json()
for y in querySeller_list["data"]:
    # print(y)
    if y["assignedName"] == username_test:
        # print(y["id"],y["assignedId"],y["assignedName"])
        user_SellerId = str(y["id"])
        user_SellerAssignedId = str(y["assignedId"])
        # print("审核人的Sellerid：",user_SellerId)
        # print("审核人的SellerAssignedid：",user_SellerAssignedId)
        break
#指定经办人
assignSeller = inter.assignSeller(id=user_executiveSellerId,assignId=user_SellerAssignedId,resourceId=user_SellerId,headers=headers)
# print("指定经办人返回：",assignSeller.json())
headers = {'Authorization': 'Bearer '+token}#还原headers
#3、提交审核
#上传图片
corpSsmphoto = "car/seller/corpSsm/252/9f328e8c5c3a41e1bd8dc9b4bd39bf84.png"
upload = inter.uploadResultSeller(photo=corpSsmphoto,headers=headers)
# print("上传图片反馈：",upload.json())

submitAdudit = inter.submitCorpSellerInfo(
    id=user_SellerId,
    email=email,
    name=name,
    companyName="Company"+name,
    city="City"+Random,
    country="Country"+Random,
    state="21315",
    companyAddress="companyAddress"+Random,
    registrationNumber="0123"+Random,
    phoneNumber=phoneNumber,
    phonePrefix=phonePrefix,
    corpSsmname="截图20210316142730.png",
    corpSsmphoto=corpSsmphoto,
    corpCardname="截图20210316142730.png",
    corpCardphoto=corpSsmphoto,
    corpDocname="截图20210316142730.png",
    corpDocphoto=corpSsmphoto,
    remarks="Remark",
    postcode = "21312d",
    resourceId=user_SellerId,
    headers=headers)
# print("提交审核反馈：",submitAdudit.json())
headers = {'Authorization': 'Bearer '+token}#还原headers
#4、审核通过
audit = inter.auditSuccessSeller(resourceId=user_SellerId,id=user_SellerId,headers=headers)
# print("审核通过返回：",audit.json())
headers = {'Authorization': 'Bearer '+token}#还原headers
#5、账户可用
# id = user_SellerId
def test_seller():
    # print("user_SellerId:",user_SellerId)
    id = user_SellerId
    # print("\nid:",id)
    searchSeller = inter.querySellerAccount(pageSize="100",current="1",headers=headers)
    Response_searchSeller = searchSeller.json()
    # print("\nResponse_searchSeller:",Response_searchSeller)
    for a in Response_searchSeller["data"]:
        # print("\n",a)
        if a["id"] == id:
            print("*"*100)
            print(a["id"],a["name"],a["status"])
            sellerStatus = a["status"]
            # print("审核人的Sellerid：",user_SellerId)
            # print("审核人的SellerAssignedid：",user_SellerAssignedId)
            break
    assert sellerStatus == "active"