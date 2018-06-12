# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
# print(L)
# L = list(filter(lambda n:n%2==1,range(1,20)))
# print(L)
# def now():
#     print('2018-5-25')

# f = now
# f()
# print(now.__name__)   
# print(f.__name__)
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper
# @ log
# def now():
#     print('2018-5-25')

def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@ log1('excute')
def now():
    print('2018-5-25')

now()


