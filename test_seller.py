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

def loginTrue():#登录正则提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest1","qwer`123",code,verify)
    # print("^^^^^^^",Response.json())
    token = Response.json()['data']['token']
    # print("token:",Response.json()['data']['token'])
    return token
#激活token
token = redis.activateToken(loginTrue())
#创建新用户，最后用新用户登录
Random = str(random.randint(0,100))#随机数
#拼接含有token的headers
headers = {'Authorization': 'Bearer '+token}


#1、创建非公司卖家账户
name = "dealerSeller"+ Random
email = name + "@qacehi.to"
phonePrefix = "+86"
phoneNumber = raddomPhone()

dealerSeller = inter.addSellerForDealer(name,email,phonePrefix,phoneNumber,headers)
#2、卖家激活账户
#3、账户可用
#4、创建非公司卖家账户
#5、指派Executive
#6、Executive填写并上传公司信息
#7、Corporate Manager审核公司信息
#8、审核不通过
#9、重新Executive填写并上传公司信息
#10、重新审核通过
#11、卖家激活账户
#12、账户可用