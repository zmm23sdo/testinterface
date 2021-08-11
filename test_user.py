from interface import Interface
from myRedis import Redis
import pytest
import json
import time

inter = Interface()
    

def getVerifyCodeImage():#获取验证码id
    code = inter.getVerifyCodeImage()
    print("获取验证码ID:",code)
    return code

def getRedis():#获取验证码从Redis
    code = getVerifyCodeImage()
    rdis = Redis()
    value = "verify_code_id_"+code
    verify = eval(rdis.client.get(value))
    print("获取验证码从Redis:",verify)
    return code,verify

def loginTrue():#登录正则提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest1","qwer`123",code,verify)
    print("^^^^^^^",Response.json())
    token = Response.json()['token']
    print("token:",Response.json()['token'])
    return token

def tokenTrue():#激活token
    token = loginTrue()
    rdis = Redis()
    redis_token = rdis.get(token())
    verified = json.loads(redis_token)
    rdis.set(token, json.dumps(verified))
    print(redis_token)
    print("Token:",token)
    return token

#拼接含有token的headers
token = tokenTrue()
headers = {'Authorization': 'Bearer '+token}
headers.update({'resourceId':resourceId})
print(headers,"\n",headersnew)    
