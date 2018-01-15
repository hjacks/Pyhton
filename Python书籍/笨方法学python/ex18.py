# 习题18：命名，变量，代码，函数

# This one is like the scripts with argv
def print_two(*args):
    arg1,arg2=args
    print(("arg1: %r,arg2: %r") % (arg1,arg2))

# Ok,that *args is actually pointness,we can just do this
def print_two_again(arg1,arg2):
    print(("arg1: %r,arg2: %r" % (arg1, arg2)))

def print_one(arg1):
    print(("arg1: %r" % arg1 ))

def print_none():
    print("I got nothing")

print_two("xutao","xiaobai")
print_two_again("jinrong","kechen")
print_one("memeda")
print_none()