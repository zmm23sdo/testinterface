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
    #验证邮箱是否可用User
    def checkEmailUser(self,email,headers):
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
                            registrationNumber,phoneNumber,phonePrefix,corpSsmname,corpSsmphoto,corpCardname,corpCardphoto,corpDocname,corpDocphoto,remarks,headers):
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
            "corpSsm":[{"name":corpSsmname,
                        "photo":corpSsmphoto}],
            "corpCard":[{"name":corpCardname,
                        "photo":corpCardphoto}],
            "corpDoc":[{"name":corpDocname,
                        "photo":corpDocphoto}],
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
    #审核退回Seller
    def auditReviseSeller(self,id,comment,headers):
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
    def saveEditInfoSeller(self,id,createdTime,email,name,phoneNumber,type,headers):
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
                            registrationNumber,phoneNumber,phonePrefix,corpSsmname,corpSsphoto,corpCardname,corpCardphoto,filename,filephoto,remarks,companyPic,
                            picIDCardname,picIDCardphoto,marginPaid,marginFilename,marginFilephoto,headers):
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
            "corpSsm":[{"name":corpSsmname,
                        "photo": corpSsphoto}],
            "corpCard":[{"name":corpCardname,
                        "photo":corpCardphoto}],
            "file":[{"name":filename,
                        "photo":filephoto}],
            "remarks":remarks,
            "companyPic":companyPic,
            "picIDCard":[{"name":picIDCardname,
                        "photo":picIDCardphoto}],
            "marginPaid":marginPaid,
            "marginFile":[{"name":marginFilename,
                        "photo":marginFilephoto,
                        "type":type}]
        },headers=headers)
        return res
    #保存dealer修改信息
    def saveEditInfoDealer(self,resourceId,id,email,contactPerson,companyName,city,country,state,companyAddress,
                            registrationNumber,phoneNumber,phonePrefix,corpSsmname,corpSsmphoto,corpCard,corpCardname,corpCardphoto,filename,filephoto,
                            remarks,companyPic,picIDCardname,picIDCardphoto,marginPaid,marginFilename,marginFilephoto,headers):
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
            "corpSsm":[{"name":corpSsmname,
                        "photo":corpSsmphoto}],
            "corpCard":[{"name":corpCardname,
                        "photo":corpCardphoto}],
            "file":[{"name":filename,
                        "photo":filephoto}],
            "remarks":remarks,
            "companyPic":companyPic,
            "picIDCard":[{"name":picIDCardname,
                        "photo":picIDCardphoto}],
            "marginPaid":marginPaid,
            "marginFile":[{"name":marginFilename,
                        "photo":marginFilephoto,
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
    #审核退回Dealer
    def auditReviseDealer(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/auditRevise"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #获取审核dealer信息
    def getAuditDealerInfo(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/getAuditDealerInfo/"
        res = requests.post(self.url+path+id,headers=headers)
        return res
    #获取dealer账户历史
    def getDealerHistory(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/getDealerHistory/"
        res = requests.post(self.url+path+id,headers=headers)
        return res
    #检查电话号码
    def checkPhoneNumber(self,phonePrefix,phoneNumber,headers):
        path = "/dealer/admin/api/dealer/checkPhoneNumber"
        res = requests.post(self.url+path,json={
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #检查公司注册码
    def checkRegistrationNumber(self,registrationNumber,headers):
        path = "/dealer/admin/api/dealer/checkRegistrationNumber"
        res = requests.post(self.url+path,json={
            "registrationNumber":registrationNumber
        },headers=headers)
        return res
    #检查邮箱Dealer
    def checkEmailDealer(self,email,headers):
        path = "/dealer/admin/api/dealer/checkEmail"
        res = requests.post(self.url+path,json={
            "email":email
        },headers=headers)
        return res
    #创建corporate dealer
    def createCorporateDealer(self,email,contactPerson,phonePrefix,phoneNumber,headers):
        path = "/dealer/admin/api/dealer/createCorporateDealer"
        res = requests.post(self.url+path,json={
            "email":email,
            "contactPerson":contactPerson,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #创建dealer
    def createDealer(self,email,contactPerson,phonePrefix,phoneNumber,headers):
        path = "/dealer/admin/api/dealer/createDealer"
        res = requests.post(self.url+path,json={
            "email":email,
            "contactPerson":contactPerson,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #获取dealer信息
    def getDealerInfo(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/getDealerInfo/"
        res = requests.post(self.url+path+id,headers=headers)
        return res
    #注销dealer
    def closeDealer(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/getDealerInfo/"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #冻结dealer
    def freezeDealer(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/freezeDealer"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #解冻dealer
    def reactivateDealer(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/reactivateDealer"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #创建dealer子账号
    def createSubsidiaryDealer(self,resourceId,id,phonePrefix,phoneNumber,email,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/reactivateDealer"
        res = requests.post(self.url+path,json={
            "id":id,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber,
            "email":email
        },headers=headers)
        return res
    #注销dealer子账号
    def closeSubsidiaryDealer(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/closeSubsidiaryDealer"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #获取dealer子账号列表
    def getSubsidiaryDealer(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/getSubsidiaryDealer"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #分配dealer
    def assignDealer(self,resourceId,id,assignId,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/dealer/admin/api/dealer/getSubsidiaryDealer"
        res = requests.post(self.url+path,json={
            "id":id,
            "assignId":assignId
        },headers=headers)
        return res
    

    '''【SalesAgent2.0】'''
    #新建salesAgent
    def addSalesAgent(self,phoneNumber,phonePrefix,email,name,type,headers):
        '''
        type:
        New Car Dealership     ---NCD
        Recond Car Dealership  ---RCD
        Used Car Dealership    ---UCD
        Individual Broker.     ---INDIVIDUAL_BROKER
        '''
        path = "/sa/admin/api/sa/addSalesAgent"
        res = requests.post(self.url+path,json={
            "phoneNumber":phoneNumber,
            "phonePrefix":phonePrefix,
            "email":email,
            "name":name,
            "type":type
        },headers=headers)
        return res
    #查询salesAgent
    def querySalesAgent(self,current,pageSize,headers):
        path = "/sa/admin/api/sa/querySalesAgent"
        res = requests.get(self.url+path,params={
            "current":current,
            "pageSize":pageSize
        },headers=headers)
        return res
    #冻结salesAgent
    def freezeSalesAgent(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/freezeSalesAgent"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #解冻salesAgent
    def unfreezeSalesAgent(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/unfreezeSalesAgent"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #注销salesAgent
    def closeSalesAgent(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/closeSalesAgent"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #获取可选分配人
    def getSalesAgentExecutive(self,headers):
        path = "/sa/admin/api/sa/getSalesAgentExecutive"
        res = requests.get(self.url+path,headers=headers)
        return res
    #分配salesAgent
    def assignSalesAgent(self,resourceId,id,assignId,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/assignSalesAgent"
        res = requests.post(self.url+path,json={
            "id":id,
            "assignId":assignId
        },headers=headers)
        return res
    #获取子账号列表
    def getSalesAgentSubsidiary(self,resourceId,id,pageSize,current,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/getSalesAgentSubsidiary"
        res = requests.get(self.url+path,params={
            "id":id,
            "pageSize":pageSize,
            "current":current
        },headers=headers)
        return res
    #查看salesAgent信息
    def salesAgentInfo(self,resourceId,id,pageSize,current,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/salesAgentInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #提交审核（除Individual broker）
    def submitSalesAgentInfo(self,resourceId,id,email,name,companyName,city,country,state,companyAddress,
                            registrationNumber,phoneNumber,phonePrefix,corpCardname,corpCardphoto,corpCardtype,remarks,postcode,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/submitSalesAgentInfo"
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
            "corpCard":[{"name":corpCardname,
                        "photo":corpCardphoto,
                        "type":corpCardtype}],
            "remarks":remarks,
            "postcode":postcode
        },headers=headers)
        return res
    #创建子账号
    def createSalesAgentSubsidiary(self,resourceId,id,email,phonePrefix,phoneNumber,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/salesAgentInfo/"
        res = requests.post(self.url+path,json={
            "id":id,
            "email":email,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #关闭子账号
    def closeSalesAgentSubsidiary(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/closeSalesAgentSubsidiary"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #审核页面
    def auditAgentInfo(self,resourceId,id,pageSize,current,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/auditAgentInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #审核成功Sa
    def auditSuccessSa(self,resourceId,id,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/auditSuccess"
        res = requests.post(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #审核失败Sa
    def auditFailSa(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/auditFail"
        res = requests.post(self.url+path,params={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #审核退回Sa
    def auditReviseSa(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/auditRevise"
        res = requests.post(self.url+path,params={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #账号历史
    def agentAccountHistory(self,resourceId,id,comment,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/agentAccountHistory/"
        res = requests.post(self.url+path+id,headers=headers)
        return res
    #提交individual broker审核
    def submitIndividualBrokerInfo(self,email,name,remarks,corpCardname,corpCardurl,id,headers):
        path = "/seller/admin/api/seller/submitCorpSellerInfo"
        res = requests.post(self.url+path,json={
            "email":email,
            "name":name,
            "remarks":remarks,
            "corpCard":[{"name":corpCardname,
                        "url":corpCardurl}],
            "id":id
        },headers=headers)
        return res
    #保存editInfo
    def saveEditInfoSa(self,resourceId,id,email,name,companyName,city,country,state,companyAddress,
                            registrationNumber,phoneNumber,phonePrefix,corpCardname,corpCardphoto,
                            corpDocname,corpDocphoto,remarks,postcode,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId
        path = "/sa/admin/api/sa/saveEditInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "info":{
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
            "corpSsm":[{"name":corpSsmname,
                        "photo":corpSsmphoto}],
            "corpCard":[{"name":corpCardname,
                        "photo":corpCardphoto}],
            "corpDoc":[{"name":corpDocname,
                        "photo":corpDocphoto}],
            "remarks":remarks,
            "postcode":postcode
            }
        },headers=headers)
        return res
    #sa check email Sa
    def checkEmailSa(self,email):
        path = "/sa/admin/api/sa/checkEmail"
        res = requests.post(self.url+path,json={
            "email":email
        },headers=headers)
        return res
    

    '''【检车2.0】'''
    #创建检车单
    def createInspection(self,carYear,carBrand,carModel,applyTel,applyTelCode,applyName,applyMail,carType,cardUrl,headers):
        path = "/inspector/admin/api/inspector/createInspection"
        res = requests.post(self.url+path,json={
            "carYear":carYear,
            "carBrand":carBrand,
            "carModel":carModel,
            "applyTel":applyTel,
            "applyTelCode":applyTelCode,
            "applyName":applyName,
            "applyMail":applyMail,
            "carType":carType,
            "cardUrl":cardUrl
        },headers=headers)
        return res
    #获取关联系统客户
    def relatedCustomer(self,no,headers):
        path = "/inspector/admin/api/inspector/relatedCustomer"
        res = requests.get(self.url+path,params={
            "no":no
            },headers=headers)
        return res
    #取消检车单
    def cancelInspection(self,no,comment,headers):
        path = "/inspector/admin/api/inspector/cancelInspection"
        res = requests.post(self.url+path,json={
            "no":no,
            "comment":comment
        },headers=headers)
        return res
    #查询待处理检车任务
    def queryNoConfirmInspections(self,current,pageSize,headers):
        path = "/inspector/admin/api/inspector/queryNoConfirmInspections"
        res = requests.get(self.url+path,params={
            "current":current,
            "pageSize":pageSize
            },headers=headers)
        return res
    #获取所有检车任务安排
    def checkerTasks(self,checkDateA,checkDateB,headers):
        path = "/inspector/admin/api/inspector/checkerTasks"
        res = requests.get(self.url+path,params={
            "checkDate":checkDateA,
            "checkDate":checkDateB
            },headers=headers)
        return res
    #获取待确认检车单详情
    def noConfirmInspectionInfo(self,id,headers):
        path = "/inspector/admin/api/inspector/noConfirmInspectionInfo"
        res = requests.get(self.url+path,params={
            "id":id
            },headers=headers)
        return res
    #获取待分配检车员
    def inspectorsWithTarget(self,checkTime,headers):
        path = "/inspector/admin/api/inspector/inspectorsWithTarget"
        res = requests.get(self.url+path,params={
            "checkTime":checkTime
            },headers=headers)
        return res
    #确认检车单
    def confirmInspection(self,id,checkTime,address,city,region,postCode,checkerName,checkerId,headers):
        path = "/inspector/admin/api/inspector/confirmInspection"
        res = requests.post(self.url+path,json={
            "id":id,
            "checkTime":checkTime,
            "address":address,
            "city":city,
            "region":region,
            "postCode":postCode,
            "checkerId":checkerId,
            "checkerName":checkerName
        },headers=headers)
        return res
    #关联seller
    def associateSeller(self,id,customerId,headers):
        path = "/inspector/admin/api/inspector/associateSeller"
        res = requests.post(self.url+path,json={
            "id":id,
            "customerId":customerId
        },headers=headers)
        return res
    #关联agent
    def associateAgent(self,id,customerId,headers):
        path = "/inspector/admin/api/inspector/associateAgent"
        res = requests.post(self.url+path,json={
            "id":id,
            "customerId":customerId
        },headers=headers)
        return res
    #查询审核未完成
    def queryCheckedInspection(self,current,pageSize,headers):
        path = "/inspector/admin/api/inspector/queryCheckedInspection"
        res = requests.get(self.url+path,params={
            "current":current,
            "pageSize":pageSize
            },headers=headers)
        return res
    #查询已完成
    def queryFinishedInspection(self,current,pageSize,headers):
        path = "/inspector/admin/api/inspector/queryFinishedInspection"
        res = requests.get(self.url+path,params={
            "current":current,
            "pageSize":pageSize
            },headers=headers)
        return res
    #审核详情
    def auditInspectionInfo(self,current,pageSize,headers):
        path = "/inspector/admin/api/inspector/queryFinishedInspection"
        res = requests.get(self.url+path,params={
            "current":current,
            "pageSize":pageSize
            },headers=headers)
        return res
    #已完成检车单详情
    def finishedInspectionInfo(self,id,headers):
        path = "/inspector/admin/api/inspector/finishedInspectionInfo"
        res = requests.get(self.url+path,params={
            "id":id
            },headers=headers)
        return res
    #审核成功Inspector
    def auditSuccessInspector(self,no,comment,price,headers):
        path = "/inspector/admin/api/inspector/auditSuccess"
        res = requests.post(self.url+path,json={
            "no":no,
            "comment":comment,
            "price":price
            },headers=headers)
        return res
    #审核失败Inspector
    def auditFailInspector(self,no,comment,headers):
        path = "/inspector/admin/api/inspector/auditSuccess"
        res = requests.post(self.url+path,json={
            "no":no,
            "comment":comment
            },headers=headers)
        return res
    #审核退回Inspector
    def auditReviseInspector(self,no,comment,headers):
        path = "/inspector/admin/api/inspector/auditRevise"
        res = requests.post(self.url+path,json={
            "no":no,
            "comment":comment
            },headers=headers)
        return res
    #上传结果
    def uploadResult(self,path,headers):
        path = "/inspector/admin/api/inspector/uploadResult"
        res = requests.post(self.url+path,json={
            "path":path
            },headers=headers)
        return res
    #取消关联
    def disassociate(self,id,headers):
        path = "/inspector/admin/api/inspector/uploadResult"
        res = requests.post(self.url+path,json={
            "id":id
            },headers=headers)
        return res
    #获取已确认检车单列表
    def queryConfirmedInspection(self,headers):
        path = "/inspector/admin/api/inspector/queryConfirmedInspection"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取已确认检车单详情
    def getConfirmedInspectionInfo(self,id,headers):
        path = "/inspector/admin/api/inspector/getConfirmedInspectionInfo"
        res = requests.get(self.url+path,json={
            "id":id
            },headers=headers)
        return res
    #获取检车报告车辆信息User
    def getCarInfoUser(self,id,resourceId,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId	
        path = "/inspector/admin/api/inspector/getCarInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取检车报告车辆照片Inspector
    def getCarPhotoInspector(self,id,resourceId,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId	
        path = "/inspector/admin/api/inspector/getCarPhoto/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取检车报告车辆损伤照片Inspector
    def getCarDamagePhotoInspector(self,id,resourceId,headers):
        headers.update({'resourceId':resourceId})#更新headers，插入resourceId	
        path = "/inspector/admin/api/inspector/getCarDamagePhoto/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取检车任务列表
    def getCheckerTaskListself(self,startTime,endTime,headers):
        path = "/inspector/api/inspector/getCheckerTaskList"
        res = requests.get(self.url+path,params={
            "startTime":startTime,
            "endTime":endTime
        },headers=headers)
        return res
    #编辑车辆损伤信息Inspector
    def editCarDamageInfoInspector(self,position,photo,photos,headers):
        path = "/inspector/api/inspector/editCarDamageInfo/"
        res = requests.post(self.url+path,json={
            "id	":id,
            "damagePhoto":{"name":{
                            "position":position,
                            "photo":photo,
                            "photos":photos
                            },}
        },headers=headers)
        return res
    #提交检车任务
    def submitCheckerTask(self,id,expectPrice,inspectorDecision,remarks,headers):
        path = "/inspector/api/inspector/submitCheckerTask"
        res = requests.post(self.url+path,json={
            "id	":id,
            "expectPrice":expectPrice,
            "inspectorDecision":inspectorDecision,
            "remarks":remarks
        },headers=headers)
        return res
    #取消检车任务
    def cancelCheckerTask(self,id,cancelReason,remarks,headers):
        path = "/inspector/api/inspector/cancelCheckerTask"
        res = requests.post(self.url+path,json={
            "id	":id,
            "cancelReason":cancelReason,
            "remarks":remarks
        },headers=headers)
        return res
    #编辑车辆信息
    def editCarInfoInspector(self,id,brand,model,chassisNumber,currentColor,currentMileage,engineCapacity,engineNumber,existingLoan,
                    fuelType,licensePlateNumber,manufacturedYear,originalColor,registrationDate,registrationType,reservedPrice,
                    roadTaxExpiryDate,seat,soldWithLicensePlate,transmission,variant,inspectionNotes,spareKey,b5,location,dealerIndicator,headers):
        path = "/inspector/api/inspector/editCarInfo"
        res = requests.post(self.url+path,json={
            "id	":id,
            "brand":brand,
            "model":model,
            "chassisNumber":chassisNumber,
            "currentColor":currentColor,
            "currentMileage":currentMileage,
            "engineCapacity":engineCapacity,
            "engineNumber":engineNumber,
            "existingLoan":existingLoan,
            "fuelType":fuelType,
            "licensePlateNumber":licensePlateNumber,
            "manufacturedYear":manufacturedYear,
            "originalColor":originalColor,
            "registrationDate":registrationDate,
            "registrationType":registrationType,
            "reservedPrice":reservedPrice,
            "roadTaxExpiryDate":roadTaxExpiryDate,
            "seat":seat,
            "soldWithLicensePlate":soldWithLicensePlate,
            "transmission":transmission,
            "variant":variant,
            "inspectionNotes":inspectionNotes,
            "spareKey":spareKey,
            "b5":b5,
            "location":location,
            "dealerIndicator":dealerIndicator
        },headers=headers)
        return res
    #获取检车报告信息
    def getInspectionReport(self,id,headers):
        path = "/inspector/api/inspector/getInspectionReport/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #退出审核
    def quitAudit(self,id,headers):
        path = "/inspector/admin/api/inspector/quitAudit"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #检查检车员时间
    def checkInspectionTime(self,checkTime,checkerId,headers):
        path = "/inspector/admin/api/inspector/checkInspectionTime"
        res = requests.post(self.url+path,json={
            "checkTime":checkTime,
            "checkerId":checkerId
        },headers=headers)
        return res
    

    '''【业绩管理2.0】'''
    #获取检车员业绩统计
    def performanceInfo(self,type,date,headers):
        path = "/user/admin/api/checker/performanceInfo"
        res = requests.get(self.url+path,params={
            "type":type,
            "date":date
        },headers=headers)
        return res
    #更改检车员目标
    def changeInspectorTarget(self,id,dayTarget,monthTarget,headers):
        path = "/user/admin/api/checker/changeInspectorTarget"
        res = requests.post(self.url+path,json={
            "id":id,
            "dayTarget":dayTarget,
            "monthTarget":monthTarget
        },headers=headers)
        return res
    #更改检车员工作区域
    def changeInspectorRegion(self,id,region,headers):
        path = "/user/admin/api/checker/changeInspectorRegion"
        res = requests.post(self.url+path,json={
            "id":id,
            "region":region
        },headers=headers)
        return res
    #获取检车员工作状态表
    def userBreakMonthDetail(self,year,month,id,headers):
        path = "/user/admin/api/checker/performanceInfo"
        res = requests.get(self.url+path,params={
            "year":year,
            "month":month,
            "id":id
        },headers=headers)
        return res
    #更改检车员工作状态
    def changeUserWorkState(self,date,userId,isBreak,remark,headers):
        path = "/user/admin/api/checker/changeUserWorkState"
        res = requests.post(self.url+path,json={
            "date":date,
            "userId":userId,
            "isBreak":isBreak,
            "remark":remark
        },headers=headers)
        return res
    #获取检车员信息变更历史
    def userChangeHistory(self,id,headers):
        path = "/user/admin/api/checker/userChangeHistory"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #获取客服业绩统计
    def getCustomerServicePerformanceInfo(self,date,type,headers):
        path = "/user/admin/api/user/getCustomerServicePerformanceInfo"
        res = requests.get(self.url+path,params={
            "date":date,
            "type":type
        },headers=headers)
        return res
    #更改客服目标
    def changeCustomerServiceTarget(self,id,dayTarget,monthTarget,headers):
        path = "/user/admin/api/user/changeCustomerServiceTarget"
        res = requests.post(self.url+path,json={
            "id":id,
            "dayTarget":dayTarget,
            "monthTarget":monthTarget
        },headers=headers)
        return res
    #获取客服工作状态表
    def userBreakMonthDetail(self,year,month,id,headers):
        path = "/user/admin/api/user/userBreakMonthDetail"
        res = requests.get(self.url+path,params={
            "year":year,
            "month":month,
            "id":id
        },headers=headers)
        return res
    #更改客服工作状态
    def changeUserWorkState(self,date,userId,isBreak,remark,headers):
        path = "/user/admin/api/user/changeUserWorkState"
        res = requests.post(self.url+path,json={
            "date":date,
            "userId":userId,
            "isBreak":isBreak,
            "remark":remark
        },headers=headers)
        return res
    #客服信息变更历史
    def userChangeHistory(self,id,headers):
        path = "/user/admin/api/user/userChangeHistory"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    
    
    '''【车辆管理2.0】'''
    #获取车辆列表
    def getCarList(self,headers):
        path = "/user/admin/api/user/userChangeHistory"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取关联卖家
    def getRelatedCustomer(self,phonePrefix,phoneNumber,headers):
        path = "/inspector/admin/api/car/getRelatedCustomer"
        res = requests.get(self.url+path,params={
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #添加车辆Car
    def createCar(self,brand,model,manufacturedYear,type,customerId,customerName,customerType,phonePrefix,phoneNumber,headers):
        path = "/inspector/admin/api/car/createCar"
        res = requests.post(self.url+path,json={
            "brand":brand,
            "model":model,
            "manufacturedYear":manufacturedYear,
            "type":type,
            "customerId":customerId,
            "customerName":customerName,
            "customerType":customerType,
            "phonePrefix":phonePrefix,
            "phoneNumber":phoneNumber
        },headers=headers)
        return res
    #获取车辆检车报告列表
    def getCarInspectionReports(self,number,headers):
        path = "/inspector/admin/api/car/getCarInspectionReports/"
        res = requests.get(self.url+path+number,headers=headers)
        return res
    #获取检车报告车辆信息Car
    def getCarInfoCar(self,id,headers):
        path = "/inspector/admin/api/car/getCarInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取检车报告车辆照片Car
    def getCarPhotoCar(self,id,headers):
        path = "/inspector/admin/api/car/getCarPhoto/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取检车报告车辆损伤照片Car
    def getCarDamagePhotoCar(self,id,headers):
        path = "/inspector/admin/api/car/getCarDamagePhoto/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #确认检车报告
    def confirmInspectionReport(self,id,headers):
        path = "/inspector/admin/api/car/confirmInspectionReport"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #删除检车报告
    def deleteInspectionReport(self,id,headers):
        path = "/inspector/admin/api/car/deleteInspectionReport"
        res = requests.post(self.url+path,json={
            "id":id
        },headers=headers)
        return res
    #修改检车报告到期时间
    def editInspectionReportExpiredTime(self,id,expiredTime,headers):
        path = "/inspector/admin/api/car/editInspectionReportExpiredTime"
        res = requests.post(self.url+path,json={
            "id":id,
            "expiredTime":expiredTime
        },headers=headers)
        return res
    #冻结车辆
    def freezeCar(self,number,days,reason,headers):
        path = "/inspector/admin/api/car/freezeCar"
        res = requests.post(self.url+path,json={
            "number":number,
            "days":days,
            "reason":reason
        },headers=headers)
        return res
    #解冻车辆
    def unfreezeCar(self,number,reason,headers):
        path = "/inspector/admin/api/car/unfreezeCar"
        res = requests.post(self.url+path,json={
            "number":number,
            "reason":reason
        },headers=headers)
        return res
    #注销车辆
    def deleteCar(self,number,reason,headers):
        path = "/inspector/admin/api/car/deleteCar"
        res = requests.post(self.url+path,json={
            "number":number,
            "reason":reason
        },headers=headers)
        return res
    #变更车辆起拍价
    def editReservedPrice(self,number,reservedPrice,headers):
        path = "/inspector/admin/api/car/editReservedPrice"
        res = requests.post(self.url+path,json={
            "number":number,
            "reservedPrice":reservedPrice
        },headers=headers)
        return res
    #获取车辆活动日志
    def getCarHistory(self,number,headers):
        path = "/inspector/admin/api/car/getCarHistory/"
        res = requests.get(self.url+path+number,headers=headers)
        return res
    #获取检车报告活动日志
    def getInspectionReportHistory(self,id,headers):
        path = "/inspector/admin/api/car/getInspectionReportHistory/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #触发检车
    def createInspection(self,number,headers):
        path = "/inspector/admin/api/car/createInspection"
        res = requests.post(self.url+path,json={
            "number":number
        },headers=headers)
        return res
    #创建检车报告
    def createInspectionReport(self,number,headers):
        path = "/inspector/admin/api/car/createInspectionReport"
        res = requests.post(self.url+path,json={
            "number":number
        },headers=headers)
        return res
    #获取已完成车辆列表
    def getCompletedCarList(self,headers):
        path = "/inspector/admin/api/car/getInspectionReportHistory/"
        res = requests.get(self.url+path,headers=headers)
        return res
    #编辑车辆信息
    def editCarInfoCar(self,id,brand,model,chassisNumber,currentColor,currentMileage,engineCapacity,engineNumber,existingLoan,
                        fuelType,licensePlateNumber,manufacturedYear,originalColor,registrationDate,registrationType,reservedPrice,
                        roadTaxExpiryDate,seat,soldWithLicensePlate,transmission,variant,inspectionNotes,spareKey,b5,location,dealerIndicator,
                        headers):
        path = "/inspector/admin/api/car/editCarInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "brand":brand,
            "model":model,
            "chassisNumber":chassisNumber,
            "currentColor":currentColor,
            "currentMileage":currentMileage,
            "engineCapacity":engineCapacity,
            "engineNumber":engineNumber,
            "existingLoan":existingLoan,
            "fuelType":fuelType,
            "licensePlateNumber":licensePlateNumber,
            "manufacturedYear":manufacturedYear,
            "originalColor":originalColor,
            "registrationDate":registrationDate,
            "registrationType":registrationType,
            "reservedPrice":reservedPrice,
            "roadTaxExpiryDate":roadTaxExpiryDate,
            "seat":seat,
            "soldWithLicensePlate":soldWithLicensePlate,
            "transmission":transmission,
            "variant":variant,
            "inspectionNotes":inspectionNotes,
            "spareKey":spareKey,
            "b5":b5,
            "location":location,
            "dealerIndicator":dealerIndicator
        },headers=headers)
        return res
    #编辑车辆损伤信息Car
    def editCarDamageInfoCar(self,id,name,position,photo,headers):
        path = "/inspector/admin/api/car/editCarDamageInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "name":name,
            "position":position,
            "photo":photo
        },headers=headers)
        return res
    #删除车辆损伤信息
    def deleteCarDamageInfo(self,id,name,position,headers):
        path = "/inspector/admin/api/car/deleteCarDamageInfo"
        res = requests.post(self.url+path,json={
            "id":id,
            "name":name,
            "position":position
        },headers=headers)
        return res
    #删除车辆照片
    def deleteCarPhoto(self,id,name,headers):
        path = "/inspector/admin/api/car/deleteCarPhoto"
        res = requests.post(self.url+path,json={
            "id":id,
            "name":name
        },headers=headers)
        return res
    #关联车辆
    def slotCar(self,number,id,headers):
        path = "/inspector/admin/api/car/slotCar"
        res = requests.post(self.url+path,json={
            "number":number,
            "id":id
        },headers=headers)
        return res
    #获取车辆竞标历史
    def getBiddingHistory(self,number,headers):
        path = "/inspector/admin/api/car/getBiddingHistory/"
        res = requests.get(self.url+path+number,headers=headers)
        return res
    #编辑检车备注
    def editInspectionNotes(self,id,comment,headers):
        path = "/inspector/admin/api/car/editInspectionNotes"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #获取车辆检车报告完成情况
    def getReportRequiredInfo(self,id,headers):
        path = "/inspector/admin/api/car/getReportRequiredInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res


    '''【竞标管理2.0】'''
    #获取竞标场次列表
    def queryBiddingBlock(self,headers):
        path = "/bidding/admin/api/bidding/queryBiddingBlock"
        res = requests.get(self.url,headers=headers)
        return res
    #批量关联车辆
    def slotCars(self,id,numbers,headers):
        path = "/inspector/admin/api/car/slotCars"
        res = requests.post(self.url+path,json={
            "id":id,
            "numbers":numbers
        },headers=headers)
        return res
    #添加竞标场次
    def createBiddingBlock(self,startTime,endTime,maxCarCount,countDownTime,systemBidPrice,
                                bidPrice1,bidPrice2,bidPrice3,startNotified,noticeTime,headers):
        path = "/bidding/admin/api/bidding/createBiddingBlock"
        res = requests.post(self.url+path,json={
            "startTime":startTime,
            "endTime":endTime,
            "maxCarCount":maxCarCount,
            "countDownTime":countDownTime,
            "systemBidPrice":systemBidPrice,
            "bidPrice1":bidPrice1,
            "bidPrice2":bidPrice2,
            "bidPrice3":bidPrice3,
            "startNotified":startNotified,
            "noticeTime":noticeTime
        },headers=headers)
        return res
    #获取竞标场次详情
    def getBiddingBlockInfo(self,id,headers):
        path = "/bidding/admin/api/bidding/getBiddingBlockInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res
    #获取车辆出价明细
    def getBidList(self,biddingBlockId,carNumber,headers):
        path = "/bidding/admin/api/bidding/getBidList"
        res = requests.get(self.url+path,params={
            "biddingBlockId":biddingBlockId,
            "carNumber":carNumber
        },headers=headers)
        return res
    #批量添加竞标场次
    def createBiddingBlocks(self,maxCarCount,countDownTime,systemBidPrice,startNotified,startTime,endTime,noticeTime,headers):
        path = "/bidding/admin/api/bidding/createBiddingBlocks"
        res = requests.post(self.url+path,json={
            "maxCarCount":maxCarCount,
            "countDownTime":countDownTime,
            "systemBidPrice":systemBidPrice,
            "startNotified":startNotified,
            "times":[{
                "startTime":startTime,
                "endTime":endTime,
                "noticeTime":noticeTime
            }]
        },headers=headers)
        return res
    #取消竞标场次
    def cancelBiddingBlock(self,id,comment,headers):
        path = "/bidding/admin/api/bidding/cancelBiddingBlock"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #批量取消车辆关联
    def cancelCars(self,ids,id,headers):
        path = "/bidding/admin/api/bidding/cancelCars"
        res = requests.post(self.url+path,json={
            "ids":ids,
            "id":id
        },headers=headers)
        return res
    #编辑Seller中标意见
    def editSellerComment(self,id,comment,headers):
        path = "/bidding/admin/api/bidding/editSellerComment"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #按时间段获取竞标场次
    def getBiddingBlocks(self,startTime,endTime,headers):
        path = "/bidding/admin/api/bidding/getBiddingBlocks"
        res = requests.get(self.url+path,params={
            "startTime":startTime,
            "endTime":endTime
        },headers=headers)
        return res
    #获取竞标场次关联车辆列表
    def getSlottedCars(self,id,pageSize,headers):
        path = "/bidding/admin/api/bidding/getSlottedCars"
        res = requests.get(self.url+path,params={
            "id":id,
            "pageSize":pageSize
        },headers=headers)
        return res
    #获取待关联车辆列表
    def getApprovedCars(self,id,headers):
        path = "/bidding/admin/api/bidding/getApprovedCars"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #编辑竞标场次
    def editBiddingBlock(self,startTime,endTime,maxCarCount,countDownTime,systemBidPrice,startNotified,noticeTime,headers):
        path = "/bidding/admin/api/bidding/editBiddingBlock"
        res = requests.post(self.url+path,json={
            "startTime":startTime,
            "endTime":endTime,
            "maxCarCount":maxCarCount,
            "countDownTime":countDownTime,
            "systemBidPrice	":systemBidPrice,
            "startNotified":startNotified,
            "noticeTime":noticeTime,
            "id":id
        },headers=headers)
        return res
    

    '''【交易2.0】'''
    #查询交易
    def queryTransOrder(self,headers):
        path = "/trans/admin/api/transaction/queryTransOrder"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取operationAdmin以及sellerTransaction
    def executiveWithSeller(self,headers):
        path = "/trans/admin/api/transaction/executiveWithSeller"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取operationAdmin以及dealerExecutive
    def executiveWithDealer(self,headers):
        path = "/trans/admin/api/transaction/executiveWithDealer"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取seller交易员
    def sellerTraders(self,headers):
        path = "/trans/admin/api/transaction/sellerTraders"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取dealer交易员
    def dealerTraders(self,headers):
        path = "/trans/admin/api/transaction/dealerTraders"
        res = requests.get(self.url+path,headers=headers)
        return res
    #指定分配人
    def assignExecutive(self,assignId,id,headers):
        path = "/trans/admin/api/transaction/assignExecutive"
        res = requests.post(self.url+path,json={
            "assignId":assignId,
            "id":id
        },headers=headers)
        return res
    #查看预约信息
    def appointmentInfo(self,headers):
        path = "/trans/admin/api/transaction/appointmentInfo"
        res = requests.get(self.url+path,headers=headers)
        return res
    #提交预约信息
    def submitAppointmentInfo(self,bizId,appointmentDate,province,district,zipCode,detail,files,transAmount,headers):
        path = "/trans/admin/api/transaction/submitAppointmentInfo"
        res = requests.post(self.url+path,json={
            "bizId":bizId,
            "appointmentDate":appointmentDate,
            "province":province,
            "district":district,
            "zipCode":zipCode,
            "detail":detail,
            "files":files,
            "transAmount":transAmount
        },headers=headers)
        return res
    #保存预约信息
    def saveAppointmentInfo(self,bizId,appointmentDate,province,district,zipCode,detail,files,transAmount,headers):
        path = "/trans/admin/api/transaction/saveAppointmentInfo"
        res = requests.post(self.url+path,json={
            "bizId":bizId,
            "appointmentDate":appointmentDate,
            "province":province,
            "district":district,
            "zipCode":zipCode,
            "detail":detail,
            "files":files,
            "transAmount":transAmount
        },headers=headers)
        return res
    #获取sellerTX
    def sellerTransInfo(self,id,headers):
        path = "/trans/admin/api/transaction/appointmentInfo"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #保存sellerTx
    def saveSellerTransInfo(self,transDate,carLocation,operatorId,operatorName,serviceFee,loanAmount,remark,
                            type_purchaseInvoice,photo_purchaseInvoice,name_purchaseInvoice,
                            type_odo,photo_odo,name_odo,type_vccl,photo_vccl,name_vccl,
                            type_partyLetter,photo_partyLetter,name_partyLetter,transId,headers):
        path = "/trans/admin/api/transaction/saveSellerTransInfo"
        res = requests.post(self.url+path,json={
            "transDate":transDate,
            "carLocation":carLocation,
            "operatorId":operatorId,
            "operatorName":operatorName,
            "serviceFee":serviceFee,
            "loanAmount":loanAmount,
            "remark":remark,
            "purchaseInvoice":[{
                "type":type_purchaseInvoice,
                "photo":photo_purchaseInvoice,
                "name":name_purchaseInvoice
            }],
            "odo":[{
                "type":type_odo,
                "photo":photo_odo,
                "name":name_odo
            }],
            "vccl":[{
                "type":type_vccl,
                "photo":photo_vccl,
                "name":name_vccl
            }],
            "partyLetter":[{
                "type":type_partyLetter,
                "photo":photo_partyLetter,
                "name":name_partyLetter
            }],
            "transId":transId
        },headers=headers)
        return res
    #提交sellerTX
    def submitSellerTransInfo(self,transDate,carLocation,operatorId,operatorName,serviceFee,loanAmount,remark,
                            type_purchaseInvoice,photo_purchaseInvoice,name_purchaseInvoice,
                            type_odo,photo_odo,name_odo,type_vccl,photo_vccl,name_vccl,
                            type_partyLetter,photo_partyLetter,name_partyLetter,transId,headers):
        path = "/trans/admin/api/transaction/submitSellerTransInfo"
        res = requests.post(self.url+path,json={
            "transDate":transDate,
            "carLocation":carLocation,
            "operatorId":operatorId,
            "operatorName":operatorName,
            "serviceFee":serviceFee,
            "loanAmount":loanAmount,
            "remark":remark,
            "purchaseInvoice":[{
                "type":type_purchaseInvoice,
                "photo":photo_purchaseInvoice,
                "name":name_purchaseInvoice
            }],
            "odo":[{
                "type":type_odo,
                "photo":photo_odo,
                "name":name_odo
            }],
            "vccl":[{
                "type":type_vccl,
                "photo":photo_vccl,
                "name":name_vccl
            }],
            "partyLetter":[{
                "type":type_partyLetter,
                "photo":photo_partyLetter,
                "name":name_partyLetter
            }],
            "transId":transId
        },headers=headers)
        return res
    #获取dealerInfo
    def dealerTransInfo(self,id,headers):
        path = "/trans/admin/api/transaction/dealerTransInfo"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #保存dealeInfo
    def saveDealerTransInfo(self,transDate,registrationFee,interestAmount,payMethod,remark,
                            type_carSalesInvoice,photo_carSalesInvoice,name_carSalesInvoice,
                            type_pdo,photo_pdo,name_pdo,type_receipt,photo_receipt,name_receipt,
                            transId,headers):
        path = "/trans/admin/api/transaction/saveDealerTransInfo"
        res = requests.post(self.url+path,json={
            "transDate":transDate,
            "registrationFee":registrationFee,
            "interestAmount":interestAmount,
            "payMethod":payMethod,
            "remark":remark,
            "carSalesInvoice":[{
                "type":type_carSalesInvoice,
                "photo":photo_carSalesInvoice,
                "name":name_carSalesInvoice
            }],
            "pdo":[{
                "type":type_pdo,
                "photo":photo_pdo,
                "name":name_pdo
            }],
            "receipt":[{
                "type":type_receipt,
                "photo":photo_receipt,
                "name":name_receipt
            }],
            "transId":transId
        },headers=headers)
        return res
    #提交dealerInfo
    def submitDealerTransInfo(self,transDate,registrationFee,interestAmount,payMethod,remark,
                            type_carSalesInvoice,photo_carSalesInvoice,name_carSalesInvoice,
                            type_pdo,photo_pdo,name_pdo,type_receipt,photo_receipt,name_receipt,
                            transId,headers):
        path = "/trans/admin/api/transaction/submitDealerTransInfo"
        res = requests.post(self.url+path,json={
            "transDate":transDate,
            "registrationFee":registrationFee,
            "interestAmount":interestAmount,
            "payMethod":payMethod,
            "remark":remark,
            "carSalesInvoice":[{
                "type":type_carSalesInvoice,
                "photo":photo_carSalesInvoice,
                "name":name_carSalesInvoice
            }],
            "pdo":[{
                "type":type_pdo,
                "photo":photo_pdo,
                "name":name_pdo
            }],
            "receipt":[{
                "type":type_receipt,
                "photo":photo_receipt,
                "name":name_receipt
            }],
            "transId":transId
        },headers=headers)
        return res
    #取消订单
    def cancelTrans(self,id,comment,headers):
        path = "/trans/admin/api/transaction/cancel"
        res = requests.post(self.url+path,json={
            "id":id,
            "comment":comment
        },headers=headers)
        return res
    #订单详情
    def orderDetail(self,id,headers):
        path = "/trans/admin/api/transaction/orderDetail"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #订单历史记录
    def historyTrans(self,id,headers):
        path = "/trans/admin/api/transaction/history"
        res = requests.get(self.url+path,params={
            "id":id
        },headers=headers)
        return res
    #（服务调用接口） biding 成功生成订单
    def createBiddingOrder(self,dealerId,sellerId,isAgent,carNo,transAmount,isBuyBye,headers):
        path = "/trans/admin/api/transaction/createBiddingOrder"
        res = requests.post(self.url+path,json={
            "dealerId":dealerId,
            "sellerId":sellerId,
            "isAgent":isAgent,
            "carNo":carNo,
            "transAmount":transAmount,
            "isBuyBye":isBuyBye
        },headers=headers)
        return res
    #(服务调用接口)买断订单
    def createBuyOutOrder(self,carId,carYear,carBrand,carNo,carModel,carLicence,customerType,
                            customerId,price,customerName,phonePrefix,phone,headers):
        path = "/trans/admin/api/transaction/createBuyOutOrder"
        res = requests.post(self.url+path,json={
            "carId":carId,
            "carYear":carYear,
            "carBrand":carBrand,
            "carModel":carModel,
            "carLicence":carLicence,
            "customerType":customerType,
            "customerId":customerId,
            "price":price,
            "customerName":customerName,
            "phonePrefix":phonePrefix,
            "phone":phone
        },headers=headers)
        return res
    #生成线下订单
    def createOfflineOrder(self,id,phoneNumber,phonePrexfix,email,assignId,headers):
        path = "/trans/admin/api/transaction/createOfflineOrder"
        res = requests.post(self.url+path,json={
            "id":id,
            "phoneNumber":phoneNumber,
            "phonePrexfix":phonePrexfix,
            "email":email,
            "assignId":assignId
        },headers=headers)
        return res
    #导出trans
    def exportTrans(self,headers):
        path = "/trans/admin/api/transaction/exportTrans"
        res = requests.get(self.url+path,headers=headers)
        return res
    #获取检车报告信息
    def reportViewInfo(self,id,headers):
        path = "/trans/admin/api/transaction/reportViewInfo/"
        res = requests.get(self.url+path+id,headers=headers)
        return res


    '''【仪表盘2.0】'''
    