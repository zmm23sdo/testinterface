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

def random_name():
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


#######设置的用户信息#####
username_test = "mingvtest2"
#######设置的用户信息#####


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


#1、新建salesAgent
phoneNumber = raddomPhone()
phonePrefix = "+86"
email = "MvAgent"+Random+"@qaceshi.fo"
name = random_name()
type = "NCD"
addAgent = inter.addSalesAgent(phoneNumber = phoneNumber,
                               phonePrefix = phonePrefix,
                               email = email,
                               name = name,
                               type = type,
                               headers = headers)
# print("新建salesAgent返回：",addAgent.json())
#2、查询salesAgent
searchAgent = inter.querySalesAgent(current = "1",pageSize = "1000",headers = headers)
# print("查询salesAgent返回：",searchAgent.json())
searchAgent_list = searchAgent.json()
#获取salesAgentId
for x in searchAgent_list["data"]:
    if x["name"] == name:
        # print(x["id"],x["name"])
        salesAgentId = str(x["id"])
        print("查询salesAgent的id：",salesAgentId)
        break
#3、获取可选分配人
getExecutive = inter.getSalesAgentExecutive(headers = headers)
# print("获取可选分配人返回：",getExecutive.json())
getExecutive_list = getExecutive.json()
for y in getExecutive_list["data"]:
    if y["name"] == username_test:
        # print(y["id"],y["name"])
        user_executiveId = str(y["id"])
        print("获取可选分配人id:",user_executiveId)
        break
#4、分配salesAgent
id = salesAgentId
resourceId = id
assignId = user_executiveId
assignAgent = inter.assignSalesAgent(resourceId = resourceId,id = id,assignId = assignId,headers = headers)
# print("分配salesAgent返回：",assignAgent.json())
headers = {'Authorization': 'Bearer '+token}#还原headers
#5、查看salesAgent信息
agentInfo = inter.salesAgentInfo(resourceId = resourceId,id = id,headers = headers)
# print("查看salesAgent信息返回：",agentInfo.json())
agentStatus = agentInfo.json()['data']['salesAgent']['status']
print("查看审核前的agent状态：",agentStatus)
#6、提交审核（除Individual broker）
#上传图片
corpCardphoto = "car/seller/corpSsm/252/9f328e8c5c3a41e1bd8dc9b4bd39bf84.png"
upload = inter.uploadResultSa(photo=corpCardphoto,headers=headers)
# print("上传图片反馈：",upload.json())

submitAgentAdult = inter.submitSalesAgentInfo(
    id=id,
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
    corpCardname="截图20210316142730.png",
    corpCardphoto=corpCardphoto,
    corpCardtype=type,
    remarks="Remark",
    postcode = "21312d",
    resourceId=resourceId,
    headers=headers)
print("提交审核返回：",submitAgentAdult.json())
#7、审核成功
auditAgent = inter.auditSuccessSa(resourceId = resourceId,id = id,headers = headers)
print("审核成功返回：",auditAgent.json())
headers = {'Authorization': 'Bearer '+token}#还原headers
#确认Agent状态改变
print("查看审核前的agent状态：",agentStatus)
def test_agent():
    agentInfo = inter.salesAgentInfo(resourceId = resourceId,id = id,headers = headers)
    # print("查看salesAgent信息返回：",agentInfo.json())
    agentStatusNew = agentInfo.json()['data']['salesAgent']['status']
    print("查看审核后的agent状态：",agentStatusNew)
    assert agentStatusNew == "active"