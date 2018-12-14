# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:45:34 2018

@author: Administrator
"""

# import multiprocessing
# import time
# def func(msg):
#     for i in range(3):
#         print(msg)
#         time.sleep(1)
        
# if __name__ == '__main__':
#     p = multiprocessing.Process(target = func,args = ('hello',))
#     p.start()
#     p.join()
#     print('Sub_process done')

# import multiprocessing
# import time
# import os
# from multiprocessing import Process
# def func(msg):
#     for i in range(3):
#         print(msg)
#         time.sleep(1)

# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes = 4)
#     for i in range(10):
#         msg = 'hello %d' %(i)
#         pool.apply_async(func,(msg,))
#     pool.close()
#     pool.join()
#     print('Sub_process(es) done')

# def run_proc(name):
#     print ('Run child process %s (%s) ' %(name,os.getpid()))
    
# if __name__=='__main__':
#     print ('Parent process %s ' %os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print ('Process will start')
#     p.start()
#     p.join()
#     print ('Process end')

import multiprocessing
import time
import os
from multiprocessing import Process
from multiprocessing import Pool 

# def task(name):
#     print('Run task %s (%s)...'%(name,os.getpid()))
#     print(time.time())
#     time.sleep(3)


# if __name__ == '__main__':
#     print('Parent process %s'%os.getpid())
#     p = Pool()
#     for i in range(9):
#         p.apply_async(task,args = (i,))
#     print('Waiting for subprocess done..')
#     p.close()
#     p.join()
#     print('All process done')
