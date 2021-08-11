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

def test_loginNull():#空参提交
    Response = inter.loginUser("","","","")
    code,verify = getRedis()#取出验证码id和验证码 
    print(Response.json())
    assert Response.json()['errorCode'] == '402'

def test_loginError():#用户不存在提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest0","qwer`123",code,verify)
    print(Response.json())
    assert Response.json()['errorCode'] == '101'

def test_loginPasswordError():#用户名和密码不匹配提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest1","DEF",code,verify)
    print(Response.json())
    assert Response.json()['errorCode'] == '100'

def test_loginVerifyError():#验证码错误提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest1","qwer`123",code,"ABC")
    print(Response.json())
    assert Response.json()['errorCode'] == '104'

def test_loginVerifyIdError():#验证码ID错误提交
    code,verify = getRedis()#取出验证码id和验证码  
    Response = inter.loginUser("mingvtest1","qwer`123","abc",verify)
    print(Response.json())
    assert Response.json()['errorCode'] == '104'

def test_loginTrue():#登录正则提交
    code,verify = getRedis()#取出验证码id和验证码
    # print("*"*10,code)
    # print("*"*10,verify)
    Response = inter.loginUser("mingvtest1","qwer`123",code,verify)
    print()
    print("^^^^^^^",Response.json())
    print( type(Response.json()['success']) )
    # assert Response.json()['success']
    #assert Response.json()['success'] == True