import requests
import json


class Interface:
    def __init__(self):
        self.url = "http://192.168.102.252:8081"
        """初始化host url"""
    #获取验证码图片
    def getVerifyCodeImage(self):
        """获取验证码图片"""
        path = "/user/admin/api/account/getVerifyCodeImage" 
        res = requests.get(self.url+path)#拼接url
        verifyCodeId=res.json()['data']['verifyCodeId']
        return verifyCodeId
    #登录
    def login(self, username,password,verifyCodeId,verifyCode):
        """登录"""
        path = "/user/admin/api/account/login"
        res = requests.post(self.url+path, json={
            "username": username,
            "password": password,
            "verifyCodeId": verifyCodeId,
            "verifyCode": verifyCode
            }
            )
        return res
    #获取admin所有用户
    def allUsers(self,pageSize,current,headers):
        """获取admin所有用户"""
        path = "/user/admin/api/user/getUserList"
        res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "current":current
        },headers=headers)
        return res
    #获取admin用户列表
    def getUsers(self,headers):
        """获取admin用户列表"""
        path = "/user/admin/api/user/getUsers"
        res = requests.get(self.url+path,headers=headers)
        return res
    #创建用户组
    def createGroup(self,title,roles,parentId,headers):
        """创建用户组"""
        path = "/user/admin/api/user/createGroup"
        res = requests.post(self.url+path,json={
            "title":title,
            "roles": [],
            "parentId":parentId
        },headers=headers)
        return res
    #修改admin用户邮箱
    def editUserEmail(self,id,email,headers):
        """修改admin用户邮箱"""
        path = "/user/admin/api/user/editUserEmail"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email
        },headers=headers)
        return res
    #修改admin用户姓名
    def editUsername(self,id,name,headers):
        """修改admin用户姓名"""
        path = "/user/admin/api/user/editUsername"
        res = requests.post(self.url+path,json={
            "id":id,
            "name":name
        },headers=headers)
        return res
    #修改admin用户密码
    def resetpassword(self,id,newPassword,setDisable,headers):
        """修改admin用户密码"""
        path = "/user/admin/api/user/resetpassword"
        res = requests.post(self.url+path,json={
            "id":id,
            "newPassword":newPassword,
            "setDisable	":setDisable
        },headers=headers)
        return res
    #修改交易员姓名
    def changeName(self,userId,name,headers):
        """修改交易员姓名"""
        path = "/user/admin/api/trader/changeName"
        res = requests.post(self.url+path,json={
            "userId":userId,
            "name":name
        },headers=headers)
        return res
    #新建检车员
    def new(self,username,password,name,email,headers):
        """新建检车员"""
        path = "/user/admin/api/checker/new"
        res = requests.post(self.url+path,json={
            "username":username	,
            "password":password,
            "name":name,
            "email":email
        },headers=headers)
        return res
    #绑定二步验证
    def bindTFA(self,id,secret,code,headers):
        path = "/user/admin/api/user/bindTFA"
        res = requests.post(self.url+path,json={
            "id":id,
            "secret":secret,
            "code":code
        },headers=headers)
        return res
    #解除二步验证
    def clearTFA(self,id,headers):
        path = "/user/admin/api/user/clearTFA"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #获取二步验证二维码
    def getQRBarcode(self,username,headers):
        path = "/user/admin/api/user/getQRBarcode"
        res = requests.get(self.url+path,params={"username":username},headers=headers)
        return res
    #验证邮箱是否可用
    def checkEmail(self,email,headers):
        path = "/user/admin/api/user/checkEmail"
        res = requests.post(self.url+path,json={
            "email":email
        },headers=headers)
        return res
    #查询检车员
    def query(self,pageSize,current,headers):
        path = "/user/admin/api/checker/query"
        res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "current":current
        },headers=headers)
        return res
    #检查用户名是否可用
    def checkUsername(self,username,headers):
        path = "/user/admin/api/user/checkUsername"
        res = requests.post(self.url+path,json={
            "username":username
        },headers=headers)
        return res
    #重置检车员密码
    def resetPassword(self,id,password,headers):
        path = "/user/admin/api/checker/resetPassword"
        res = requests.post(self.url+path,json={
            "id":id,
            "password":password
        },headers=headers)
        return res
    #修改检车员邮箱
    def changeEmail(self,id,email,headers):
        path = "/user/admin/api/checker/changeEmail"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email
        },headers=headers)
        return res
    #修改检车员姓名
    def changeName(self,id,username,headers):
        path = "/user/admin/api/checker/changeName"
        res = requests.post(self.url+path,json={
            "id":id,
            "username":username
        },headers=headers)
        return res
    #注销交易员
    def logoff(self,userId,headers):
        path = "/user/admin/api/trader/logoff"
        res = requests.post(self.url+path,json={
            "userId":userId
        },headers=headers)
        return res
    #检验用户组内用户是否可以被删除
    def checkGroupUser(self,id,headers):
        path = "/user/admin/api/user/checkGroupUser"