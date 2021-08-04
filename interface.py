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
    

    '''【User用户管理模块2.0】'''
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
    def newChecker(self,username,password,name,email,headers):
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
    def queryChecker(self,pageSize,current,headers):
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
    def changeEmailChecker(self,id,email,headers):
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
        res = requests.post(self.url+path,json={
            "id	":id
        },headers=headers)
        return res
    #检查admin用户是否可以被注销
    def checkUser(self,id,headers):
        path = "/user/admin/api/user/checkUser"
        res = requests.post(self.url+path,json={
            "id	":id
        },headers=headers)
        return res
    #注销admin用户
    def deleteUser(self,id,headers):
        path = "/user/admin/api/user/deleteUser"
        res = requests.post(self.url+path,json={
            "id	":id
        },headers=headers)
        return res
    #获取用户下级用户组用户信息
    def getGroupUsers(self,userId,roles,headers):
        path = "/user/admin/api/user/getGroupUsers"
        res = requests.get(self.url+path,params={
            "userId	":userId,
            "roles":roles
        },headers=headers)
        return res
    #编辑用户组信息
    def editGroupInfo(self,groupId,title,roles,groupUsers,headers):
        path = "/user/admin/api/user/editGroupInfo"
        res = requests.post(self.url+path,json={
            "groupId":groupId,
            "title":title,

        },headers=headers)
        return res
    #获取用户组角色列表
    def getGroupRoles(self,id,headers):
        path = "/user/admin/api/user/getGroupRoles/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取用户组信息
    def getGroupInfo(self,id,headers):
        path = "/user/admin/api/user/getGroupInfo/"
        res = requests.get(self.url+path+id,headers=headers)
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
    #获取用户组树
    def groupTree(self,headers):
        path = "/user/admin/api/user/groupTree"
        res = requests.get(self.url+path,headers=headers)
        return res
    #删除用户组
    def deleteGroup(self,id,headers):
        path = "/user/admin/api/user/deleteGroup"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #创建用户
    def createUser(self,username,password,email,name,enabled,headers):
        path = "/user/admin/api/user/createUser"
        res = requests.post(self.url+path,json={
            "username":username,
            "password":password,
            "email":email,
            "name":name,
            "enabled":enabled
        },headers=headers)
        return res
    #重置密码
    def resetPassword(self,username,newPassword,setDisable,headers):
        path = "/user/admin/api/user/resetPassword"
        res = requests.post(self.url+path,json={
            "username":username,
            "newPassword":newPassword,
            "setDisable":setDisable
        },headers=headers)
        return res
    #新建交易员
    def newTrader(self,role,username,email,headers):
        path = "/user/admin/api/trader/new"
        res = requests.post(self.url+path,json={
            "role":role,
            "username":username,
            "email":email
        },headers=headers)
        return res
    #交易员查询
    def queryTrader(self,pageSize,current,headers):
        path = "/user/admin/api/trader/query"
        res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "current":current
        },headers=headers)
        return res
    #修改交易员邮箱
    def changeEmailTrader(self,userId,email,headers):
        path = "/admin/api/trader/changeEmail"
        res = requests.post(self.url+path,json={
            "userId":userId,
            "email":email
        },headers=headers)
        return res
    '''【Seller 2.0】'''
    #新建corp seller
    def addCorpSeller(self,phoneNumber,phonePrefix,email,name,headers):
        path = "/seller/admin/api/seller/addCorpSeller"
        res = requests.post(self.url+path,json={
            "phoneNumber":phoneNumber,
            "phonePrefix":phonePrefix,
            "email":email,
            "name":name
        },headers=headers)
        return res
    #查询seller
    def querySellerAccount(self,pageSize,current,headers):
        path = "/seller/admin/api/seller/querySellerAccount"
        res = requests.get(self.url+path,params={
            "pageSize":pageSize,
            "current":current
        },headers=headers)
        return res
    #冻结seller
    def freezeSeller(self,id,comment,headers):
        path = "/seller/admin/api/seller/freezeSeller"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #解冻seller
    def unfreezeSeller(self,id,comment,headers):
        path = "/seller/admin/api/seller/unfreezeSeller"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #注销seller
    def closeSeller(self,id,comment,headers):
        path = "/seller/admin/api/seller/closeSeller"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #获取可选经办人列表
    def getSellerExecutive(self,id,headers):
        path = "/seller/admin/api/seller/getSellerExecutive/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #指定经办人
    def assignSeller(self,id,assignId,headers):
        path = "/seller/admin/api/seller/assignSeller"
        res = requests.post(self.url+path,json={
            "id":id,
            "assignId":assignId
        },headers=headers)
        return res
    #获取子账号列表
    def getSellerSubsidiary(self,id,headers):
        path = "/seller/admin/api/seller/getSellerSubsidiary/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #创建Seller子账号
    def createSellerSubsidiary(self,id,email,phonePrefix,phoneNumber,headers):
        path = "/seller/admin/api/seller/createSellerSubsidiary"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #注销Seller子账号
    def closeSellerSubsidiary(self,id,headers):
        path = "/seller/admin/api/seller/closeSellerSubsidiary"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #新建个人seller
    def addIndividualSeller(self,name,email,phonePrefix,phoneNumber,headers):
        path = "/seller/admin/api/seller/addIndividualSeller"
        res = requests.post(self.url+path,json={
            "name":name,
            "email":email,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #为dealer创建seller
    def addSellerForDealer(self,name,email,phonePrefix,phoneNumber,headers):
        path = "/seller/admin/api/seller/addSellerForDealer"
        res = requests.post(self.url+path,json={
            "name":name,
            "email":email,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #获取分派的seller详情
    def sellerInfo(self,id,headers):
        path = "/seller/admin/api/seller/sellerInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取需要审核的seller详情
    def auditSellerInfo(self,id,resourceId,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId	
        path = "/seller/admin/api/seller/auditSellerInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #提交公司seller审核
    def submitCorpSellerInfo(self,id,email,name,companyName,city,country,state,companyAddress,
                            registrationNumber,phoneNumber,phonePrefix,corpSsm,corpCard,corpDoc,remarks,headers):
        path = "/seller/admin/api/seller/submitCorpSellerInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email,
            "name":name,
            "companyName":companyName,
            "city":city,
            "country":country,
            "state":state,
            "companyAddress":companyAddress,
            "registrationNumber":registrationNumber,
            "phoneNumber":phoneNumber,
            "phonePrefix":phonePrefix,
            "corpSsm":[{"name":name,
                        "photo": photo}],
            "corpCard":[{"name":name,
                        "photo": photo}],
            "corpDoc":[{"name":name,
                        "photo": photo}],
            "remarks":remarks
        },headers=headers)
        return res
    #提交个人seller信息修改
    def submitIndividualSellerInfo(self,name,email,id,headers):
        path = "/seller/admin/api/seller/submitIndividualSellerInfo"
        res = requests.post(self.url+path,json={
            "name":name,
            "email":email,
            "id":id
        },headers=headers)
        return res
    #审核通过Seller
    def auditSuccessSeller(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})
        path = "/seller/admin/api/seller/auditSuccess"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #获取seller history
    def sellerAccountHistory(self,id,headers):
        path = "/seller/admin/api/seller/sellerAccountHistory/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #审核失败Seller
    def auditFailSeller(self,id,comment,headers):
        path = "/seller/admin/api/seller/auditFail"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #审核退回
    def auditRevise(self,id,comment,headers):
        path = "/seller/admin/api/seller/auditRevise"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #上传图片成功
    def uploadResultSeller(self,photo,headers):
        path = "/selle/admin/api/seller/uploadResult"
        res = requests.post(self.url+path,json={
            "photo": photo
        },headers=headers)
        return res
    #查询获取可查看审核人
    def getSellerExecutive(self,headers):
        path = "/seller/admin/api/seller/getSellerExecutive"
        res = requests.get(self.url+path,headers=headers)
        return res
    #保存修改信息
    def saveEditInfoSeller(self,id,info,headers):
        path = "/seller/admin/api/seller/saveEditInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "info":[{
                "createdTime":createdTime,
                "email":email,
                "name":name,
                "phoneNumber":phoneNumber,
                "type":type
            }]
        },headers=headers)
        return res


    '''【Dealer2.0】'''
    #获取dealer列表
    def getDealerList(self,createdBy,createdTime,headers):
        path = "/dealer/admin/api/dealer/getDealerList"
        res = requests.get(self.url+path,params={
            "createdBy":createdBy,
            "createdTime":createdTime
        },headers=headers)
        return res
    #文件上传结果
    def uploadResultDealer(self,photo,headers):
        path = "/dealer/admin/api/dealer/uploadResult"
        res = requests.post(self.url+path,json={
            "photo": photo
        },headers=headers)
        return res
    #获取可选经办人列表
    def getDealerExecutive(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})
        path = "/dealer/admin/api/dealer/getDealerExecutive/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取所有经办人列表
    def getDealerExecutive(self,headers):
        path = "/dealer/admin/api/dealer/getDealerExecutive"
        res = requests.get(self.url+path,headers=headers)
        return res
    #提交dealer审核
    def submitDealerInfo(self,resourceId,id,email,contactPerson,companyName,city,country,state,companyAddress,
                            registrationNumber,phoneNumber,phonePrefix,corpSsm,corpCard,file,remarks,companyPic,
                            picIDCard,marginPaid,marginFile,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId	
        path = "/seller/admin/api/seller/submitCorpSellerInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email,
            "contactPerson":contactPerson,
            "companyName":companyName,
            "city":city,
            "country":country,
            "state":state,
            "companyAddress":companyAddress,
            "registrationNumber":registrationNumber,
            "phoneNumber":phoneNumber,
            "phonePrefix":phonePrefix,
            "corpSsm":[{"name":name,
                        "photo": photo}],
            "corpCard":[{"name":name,
                        "photo": photo}],
            "file":[{"name":name,
                        "photo": photo}],
            "remarks":remarks,
            "companyPic":companyPic,
            "picIDCard":[{"name":name,
                        "photo": photo}],
            "marginPaid":marginPaid,
            "marginFile":[{"name":name,
                        "photo": photo,
                        "type":type}]
        },headers=headers)
        return res
    #保存dealer修改信息
    def saveEditInfoDealer(self,resourceId,id,email,contactPerson,companyName,city,country,state,companyAddress,
                            registrationNumber,phoneNumber,phonePrefix,corpSsm,corpCard,file,remarks,companyPic,
                            picIDCard,marginPaid,marginFile,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId	
        path = "/dealer/admin/api/dealer/saveEditInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email,
            "contactPerson":contactPerson,
            "companyName":companyName,
            "city":city,
            "country":country,
            "state":state,
            "companyAddress":companyAddress,
            "registrationNumber":registrationNumber,
            "phoneNumber":phoneNumber,
            "phonePrefix":phonePrefix,
            "corpSsm":[{"name":name,
                        "photo": photo}],
            "corpCard":[{"name":name,
                        "photo": photo}],
            "file":[{"name":name,
                        "photo": photo}],
            "remarks":remarks,
            "companyPic":companyPic,
            "picIDCard":[{"name":name,
                        "photo": photo}],
            "marginPaid":marginPaid,
            "marginFile":[{"name":name,
                        "photo": photo,
                        "type":type}]
        },headers=headers)
        return res
    #审核通过Dealer
    def auditSuccessDealer(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/auditSuccess"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #审核失败Dealer
    def auditFailDealer(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/auditFail"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    