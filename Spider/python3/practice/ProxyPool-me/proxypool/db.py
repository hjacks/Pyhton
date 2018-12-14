# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:18:43 2018

@author: Administrator
"""

import redis
from random import choice
from proxypool.error import PoolEmptyError
from proxypool.setting import redis_host,redis_port,redis_password,redis_key
from proxypool.setting import max_score,min_score,initial_score
import re

class RedisClient(object):
    def __init__(self,host=redis_host,port=redis_port,password=redis_password):
        """
        初始化
        ：param host: Redis 地址
        ：param port：Redis 端口
        ：param password：Redis 密码
        """
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        
    def add(self,proxy,score=initial_score):
        """
        添加代理，设置分数为最高
        ：param proxy：代理
        ：param score：分数
        ：return：添加结果
        """
        if not re.match('\d+\.\d+.\d+.\d+\:\d+',proxy):
            print('代理不符合规范',proxy,'丢弃')
            return
        if not self.db.zscore(redis_key,proxy):
            return self.db.zadd(redis_key,score,proxy)
        
    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常
        ：return：随机代理
        """
        result = self.db.zrangebyscore(redis_key,max_score,max_score)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(redis_key,0,100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError
    
    def decrease(self,proxy):
        """
        代理值减一分，分数小于最小值，则代理删除
        ：param proxy：代理
        ：return：修改后的代理分数
        """
        score = self.db.zscore(redis_key,proxy)
        if score and score > min_score:
            print('代理',proxy,'当前分数',score,'减1')
            return self.db.zincrby(redis_key,proxy,-1)
        else:
            print('代理',proxy,'当前分数',score,'移除')
            return self.db.zrem(redis_key,proxy)
    
    def exists(self,proxy):
        """
        判断是否存在
        ：param proxy：代理
        ：return：是否存在
        """
        return not self.db.zscore(redis_key,proxy) == None
    
    def max(self,proxy):
        """
        将代理设置为max_score
        ：param proxy：代理
        ：return：设置结果
        """
        print('代理',proxy,'可用，设置为',max_score)
        return self.db.zadd(redis_key,max_score,proxy)
    
    def count(self):
        """
        获取数量
        ：return：数量
        """
        return self.db.zcard(redis_key)
    
    def all(self):
        """
        获取全部代理
        ：return：全部代理列表
        """
        return self.db.zrangebyscore(redis_key,min_score,max_score)

    def batch(self,start,stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(redis_key,start,stop-1)

if __name__ == '__main__':
    conn = RedisClient()
    result = conn.batch(680,688)
    print(result)
