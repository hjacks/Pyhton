from functools import wraps

import time
import logging

def warn(timeout):
	def decorator(func):
		@wraps(func)
		def warpper(*args,**kargs):
			start = time.time()
			res = func(*args,**kargs)
			used = time.time() - start
			if used >timeout:
				msg=' "%s" : %s > %s' %(func.__name__,used,timeout)
				logging.warn(msg)
			return res
		def setTimeout(k):
			nonlocal timeout
			timeout = k
		warpper.setTimeout = setTimeout
		return warpper
	return decorator

from random import randint
@warn(1.5)
def test():
	print('In test')
	while randint(0,1):
		time.sleep(0.5)

for _ in range(20):
	test()

test.setTimeout(1)
for _ in range(20):
	test()