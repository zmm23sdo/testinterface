import redis 
import json
class Redis:
    def __init__(self):#初始化Redis
        self.client = redis.Redis(host='192.168.102.252', port=6379,decode_responses=True,password="qwer1234", db=0)
        
    def activateToken(self,token):#在Redis中激活token
        R = redis.Redis(host='192.168.102.252', port=6379, decode_responses=True,password="qwer1234", db=0)
        redis_token = R.get(token)
        verified = json.loads(redis_token);
        verified['verified'] = True
        R.set(token, json.dumps(verified))
        # print(R.get(token))
        # print("Token:",token)
        return token

"""

初始化redis

def __init__(self):
    self.redisClient = myRedis.Redis()

"""