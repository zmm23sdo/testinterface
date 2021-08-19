import types
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
    headList = ["120", "121", "122", "123", "124", "125", "126", "127", "128", "129",
               "177", "170", "171", "172", "173", "175", "176", "177", "178", "179",
               "196", "197", "198", "199", "191", "192", "193", "194", "195"]
    phoneNum = random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))
    return phoneNum

def random_name():#随机生成姓名
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛' \
           '奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康' \
           '伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵' \
           '席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗' \
           '丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫' \
           '乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄' \
           '印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂' \
           '濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘' \
           '匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相' \
           '查后荆红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳' \
           '淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木' \
           '巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生' \
           '岳帅缑亢况郈有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福'
    ming = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清' \
           '飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善' \
           '厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家' \
           '致树炎德行时泰盛秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环' \
           '雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶' \
           '怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑筠柔竹霭凝晓欢霄枫芸菲寒欣滢伊亚宜可姬舒影荔枝思丽秀' \
           '飘育馥琦晶妍茜秋珊莎锦黛青倩婷宁蓓纨苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希'
    X=random.choice(xing)
    M="".join(random.choice(ming) for i in range(2))
    time_now = int(time.time())
    name_random = X+M+str(time_now)
    return name_random


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

#1、admin新建lead
applyName = random_name()
applyTel = raddomPhone()
newLead = inter.newLead(
    carYear = "1992", 
    carBrand = "ALFA ROMEO",
    carType = "2",
    carModel = "145", 
    applyName = applyName, 
    applyTel = applyTel, 
    applyTelCode = "+86", 
    applyMail = "Mv"+Random+"@qaceshi.ro", 
    checkTime = "2021-08-23T04:00:00Z", 
    checkDetailAddress = "Address"+Random, 
    checkCity = "City"+Random, 
    checkRegion = "y", 
    checkPostcode = "Postcode"+Random, 
    headers = headers)
# print("admin新建lead返回：",newLead.json())
#2、查询等待预检的lead
searchUnchecked = inter.unchecked(current = "1",pageSize = "100",headers = headers)
# print("查询等待预检的lead返回：",searchUnchecked.json())
searchUnchecked_list = searchUnchecked.json()
#获取刚新建lead的id
for x in searchUnchecked_list["data"]:
    if x["applyName"] == applyName:
        print(x["id"],x["leadNo"],x["applyName"])
        newLead_leadNo = str(x["leadNo"])
        newLead_id = str(x["id"])
        # print("获取刚新建lead的leadNo：",newLead_leadNo)
        break
#3、获取corporate成员
searchCorMembers = inter.corporateMembers(headers = headers)
searchCorMembers_list = searchCorMembers.json()
#获取刚新建lead的id
for y in searchCorMembers_list["data"]:
    if y["name"] == username_test:
        print(y["id"],y["name"])
        corMem_id = str(y["id"])
        # print("获取corporate成员的id：",corMem_id)
        break
#4、指派经办人（Corporate）
assignCorporate = inter.assignCorporate(leadNo = newLead_leadNo, assignId = corMem_id, resourceId = newLead_leadNo, headers = headers)
# print("指派经办人（Corporate）返回：",assignCorporate.json())
headers = {'Authorization': 'Bearer '+token}#还原headers
#5、编辑车辆户口
changeCarCard = inter.changeCarCard(
    carType = "2", 
    cardUrl = "car/seller/corpSsm/252/9f328e8c5c3a41e1bd8dc9b4bd39bf84.png", 
    leadNo = newLead_leadNo, 
    headers = headers)
# print("编辑车辆户口返回：",changeCarCard.json())
#6、获取lead详情
id = newLead_leadNo
searchLeadInfo = inter.infoLead(id = id,headers = headers)
# print("获取lead详情返回：",searchLeadInfo.json())
customerIdA = searchLeadInfo.json()["data"]["seller"]
customerIdB = searchLeadInfo.json()["data"]["salesAgent"]
print("获取lead的customerId返回：\n","customerIdA:",customerIdA,"\n","customerIdB:",customerIdB)
if customerIdA == None and customerIdB ==None:
    #lead创建seller
    phoneNumber = searchLeadInfo.json()["data"]["lead"]["applyTel"]
    phonePrefix = searchLeadInfo.json()["data"]["lead"]["applyTelCode"]
    type = searchLeadInfo.json()["data"]["lead"]["carType"]
    email = "MvSeller"+Random+"@qaceshi.so"
    name = random_name()
    # print("phoneNumber:",phoneNumber)
    # print("phonePrefix:",phonePrefix)
    # print("type:",type)
    # print("email:",email)
    # print("name:",name)
    leadNewSeller = inter.leadNewSeller(
        phoneNumber = phoneNumber, 
        phonePrefix = phonePrefix, 
        type = type, 
        email = email, 
        name = name, 
        headers = headers)
    # print("lead创建seller返回：",leadNewSeller.json())

    #激活seller
    #1.查询seller
    searchSeller = inter.querySellerAccount(pageSize = "100",current = "1",headers = headers)
    searchSeller_list_new = searchSeller.json()
    # print(searchSeller_list)
    # print(phoneNumber)
    for w in searchSeller_list_new["data"]:
        # print(w["phoneNumber"])
        if (w["phoneNumber"] == phoneNumber):
            # print(w["id"],w["name"])
            usernew_SellerId = str(w["id"])
            # print("查询获取查询sellerid：",usernew_SellerId)
            break
    usernew_SellerId = str(w["id"])
    print("查询获取查询sellerid：",usernew_SellerId,name)
    #2.获取可选经办人列表
    getSellerExecutive = inter.getSellerExecutiveId(id = usernew_SellerId, headers = headers)
    getSellerExecutive_list = getSellerExecutive.json()
    # time.sleep(3)
    # print("\ngetSellerExecutive_list:",getSellerExecutive_list,"\n")
    for u in getSellerExecutive_list["data"]:
        if u["name"] == username_test:
            # print(u["id"],u["name"])
            user_ExecutiveId = str(u["id"])
            # print("查询获取可查看审核人id：",user_ExecutiveId)
            break
    user_ExecutiveId = str(u["id"])
    print("查询获取可查看审核人id：",user_ExecutiveId,username_test)
    #3.指定经办人
    assignSeller = inter.assignSeller(id=usernew_SellerId,assignId=user_ExecutiveId,resourceId=usernew_SellerId,headers=headers)
    # print("指定经办人返回：",assignSeller.json())
        
    #4.上传图片
    corpSsmphoto = "car/seller/corpSsm/252/9f328e8c5c3a41e1bd8dc9b4bd39bf84.png"
    upload = inter.uploadResultSeller(photo=corpSsmphoto,headers=headers)
    # print("上传图片反馈：",upload.json())
    #5.提交审核
    submitAdudit = inter.submitCorpSellerInfo(
        id=usernew_SellerId,
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
        resourceId=usernew_SellerId,
        headers=headers)
    print("提交审核反馈：",submitAdudit.json())
    #6.审核通过
    audit = inter.auditSuccessSeller(resourceId=user_ExecutiveId,id=usernew_SellerId,headers=headers)
    print("审核通过返回：",audit.json())


    #获取lead详情
    searchLeadInfo = inter.infoLead(id = newLead_leadNo,headers = headers)
    # print("获取lead详情返回：",searchLeadInfo.json())
    customerId = searchLeadInfo.json()["data"]["seller"]["id"]
    print("获取lead的customerId返回：",customerId)
else:
    print("获取lead的customerId返回sellerId",customerIdA)
    print("获取lead的customerId返回agentId",customerIdB)
    if customerIdA != None:
        customerId = customerIdA
    elif customerIdB != None:
        customerId = customerIdB
    print("获取lead的customerId返回**：",customerId)

#7、关联seller
associateSeller = inter.associateSellerLead(leadNo = newLead_leadNo,customerId = customerId,headers = headers)
print("关联seller返回：",associateSeller.json())
#8、lead申请确认
checkLead = inter.checkLead(leadNo = newLead_leadNo,headers = headers)
print("lead申请确认返回：",checkLead.json())
#9、生成新检车单
def test_lead():
    #查询待处理检车任务
    queryInspector = inter.queryNoConfirmInspections(current="1", pageSize="1000", headers=headers)
    # queryInspector_list = queryInspector.json()
    # print("查询待处理检车任务返回：",queryInspector_list)
    app_Name = queryInspector.json()['data'][0]['applyName']
    print(app_Name)
    app_Name = str(app_Name)
        
    if app_Name == applyName:
        print("Yes")
    else:
        print("Eorro")
    assert app_Name == applyName