# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:55:32 2018

@author: Administrator
"""

import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from proxypool.db import RedisClient
from proxypool.setting import *

class Tester(object):
    def __init__(self):
        self.redis = RedisClient()
        
    async def test_single_proxy(self,proxy):
        """
        测试单个代理
        ：param proxy：单个代理
        ：return：None
        """
        
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://'+proxy
                print('正在测试',proxy)
                async with session.get(test_url,proxy=real_proxy,timeout=15,allow_redirects=False) as response:
                    if response.status in valid_status_codes:
                        self.redis.max(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法',proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败',proxy)
                
    def run(slef):
        """
        测试主函数
        ：return：None
        """
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余',count,'个代理')
            for i in range(0,count,batch_test_size):
                start = i
                stop = min(i+batch_test_size,count)
                print('正在测试第',start+i,'-',stop,'个代理')
                test_proxies = self.redis.batch(start,stop)
                loop= asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误',e.args)