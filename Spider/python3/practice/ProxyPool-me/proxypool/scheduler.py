import time
from multiprocessing import Process
from proxypool.api import app
from proxypool.getter import Getter
from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.setting import *


class Scheduler():
    def schedule_tester(self, cycle=tester_cycle):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)
    
    def schedule_getter(self, cycle=getter_cycle):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        """
        开启API
        """
        app.run(api_host, api_port)
    
    def run(self):
        print('代理池开始运行')
        
        if tester_enabled:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        
        if getter_enabled:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        
        if api_enabled:
            api_process = Process(target=self.schedule_api)
            api_process.start()
