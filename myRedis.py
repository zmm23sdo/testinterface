import redis 

class Redis:
    def __init__(self):
        self.client = redis.Redis(host='192.168.102.252', port=6379,decode_responses=True,password="qwer1234", db=0)
        


"""
初始化redis

def __init__(self):
    self.redisClient = myRedis.Redis()

"""