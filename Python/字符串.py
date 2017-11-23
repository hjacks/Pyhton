#3.1字符串格式化
formats='Hello,%s,%s enough for ya?'
values=('World','Hot')
print(formats % values)
print('Price for eggs:$%d' %42)
print('Haxadecimal price of eggs:$%x'%42)
from math import pi
print('Pi:%f'%pi)
print('%10f'%pi)
print('%10.2f'%pi)
print('%.2f'%pi)
print('%.5s'%'hello world!')
print('%.*s'%(4,'hello world'))
print('%010.2f'%pi)
print('%-10.2f'%pi)
print('% 5d'%10)
print('% 5d'%-10)
print('%+5d'%10)
print('%+5d'%-10)
#3.2字符串方法
#1.find
#返回子串所在位置的最左端索引，没有找到返回-1
title='hello world!I"m fine'
print(title.find('hello'))
print(title.find('fine'))
#该方法还接受参数表示起始点和结束点
print(title.find('o',5,9))
#2.join
seq=['1','2','3']
print('+'.join(seq))
#3.lower
print('HEFFH'.lower())
#4.replace
#替换所有匹配项
print('abcsaac'.replace('a','1'))
#5.split
print('1+2+3+4+5+6'.split('+'))
#6.strip
print('    sdfa    '.strip())
#7.translate
#只处理单个字符

