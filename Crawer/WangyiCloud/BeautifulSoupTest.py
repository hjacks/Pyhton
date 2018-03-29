from bs4 import BeautifulSoup

# html = """
# <html><head><title id='id_title' class="class_title1 class_title2">the dormous story</title></head>
# <body><p class="title"><b>the dormous story</b></p><div><!--comment test--></div><p class="story">Once upon a time there were three little girls;and they were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsize</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived a bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html,'lxml')
# #格式化输出，并自动补齐
# print(soup.prettify())

# 四大对象种类
# 1,Tag
html = """
<html><head><title id='id_title' class="class_title1 class_title2">the dormous story</title></head>
<body><p class="title"><b>the dormous story</b></p><div><!--comment test--></div><p class="story">Once upon a time there were three little girls;and they were
<a href="http://example.com/elsie" class="sister" id="link1">Elsize</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived a bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')

# print('title type:',type(soup.title))
# print('title name:',soup.title.name)#名称
# print('title attrs:',soup.title.attrs)#属性

# NavigableString
# 获取标签内部文字
# print('p.string type:',type(soup.p.string))#获取第一个p标签
# print('p.string contents:',soup.p.string)

# BeautifulSoup
# 表示一个文档的全部内容
# soup = BeautifulSoup(html,'lxml')
# print('soup type:',type(soup))
# print('soup name:',soup.name)
# print('soup attrs:',soup.attrs)

# 2,comment
# 注释

html = """
<html><head><title id='id_title' class="class_title1 class_title2">the dormous story</title></head>
<body><p class="title"><b>the dormous story</b></p><div><!--comment test--></div><p class="story">Once upon a time there were three little girls;and they were
<a href="http://example.com/elsie" class="sister" id="link1">Elsize</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived a bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.div.string:',soup.div.string)# 输出注释内容，但不输出注释符号
# print('soup.div.string.type:',type(soup.div.string))
# print('soup.p.string.type:',type(soup.p.string))

# 遍历文档树
# 节点内容
# .string
# 获取tag内容，若tag只有一个NavigableString类型子节点，那么这个tag可以使用，超过一个，返回none
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('p.string content:',soup.p.string)
# print('div.string content:',soup.div.string)

# 获取多个内容
# .strings:获取所有内容，返回一个generator(包含空白字符)
# .stripped_strings:获取所有内容，返回一个generator(剔除空白字符)

html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.p.strings content:',soup.p.strings)
# print('soup.p.strings.list:',list(soup.p.strings))
# print('-------------------')
# print('soup.div.strings content:',soup.div.strings)
# print('soup.div.strings.list:',list(soup.div.strings))

# 直接子节点
# .contents属性：将tag的子节点以列表形式输出
# .children属性：将tag的子节点以list-iterator形式输出
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.div.contents:',soup.div.contents)
# print('soup.div.contents list',list(soup.div.contents))
# print('-------------')
# print('soup.div.children:',soup.div.children)
# print('soup.div.children list:',list(soup.div.children))

# 所有子孙节点
# .descendants属性：对所有子节点递归
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.div.contents:',soup.div.contents)
# print('soup.div.contents list',list(soup.div.contents))
# print('-------------')
# print('soup.div.children:',soup.div.descendants)
# print('soup.div.children list:',list(soup.div.descendants))

# 父节点
#.parent属性：父节点
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
# soup = BeautifulSoup(html,'lxml')
# print('soup.b.parent:',soup.b.parent)
# print('soup.b.parent type:',type(soup.b.parent))

# 全部父节点
#.parents属性：所有父节点
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.b.parents:',soup.b.parents)
# print('soup.b.parents type:',type(soup.b.parents))
# print('-----------------------------')
# for i in soup.b.parents:
#     print('parent name:',i.name)

# 兄弟节点
# .next_sibling属性:下一个兄弟节点
# .previous_sibling属性：上一个兄弟节点
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.p.next_sibling:',repr(soup.p.next_sibling))
# print('soup.p.next_sibling type:',type(soup.p.next_sibling))
# print('-----------------------')
# print('soup.p.next_sibling.next_sibling:',repr(soup.p.next_sibling.next_sibling))
# print('soup.p.next_sibling.next_sibling type:',type(soup.p.next_sibling.next_sibling))
# print('-----------------------')
# print('soup.p.previous_sibling:',repr(soup.p.previous_sibling))
# print('soup.p.previous_sibling type:',type(soup.p.previous_sibling))
# print('-----------------------')
# print('soup.p.previous_sibling.previous_sibling:',soup.p.previous_sibling.previous_sibling)
# print('soup.p.previous_sibling.previous_sibling type:',type(soup.p.previous_sibling.previous_sibling))

# 全部兄弟节点
# .next_siblings:全部弟弟(generator)
# .previous_siblings：全部哥哥(generator)
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
# soup = BeautifulSoup(html,'lxml')
# print('soup.p.next_silibings type:',type(soup.p.next_siblings))
# print('soup.p.next_silibings list:',list(soup.p.next_siblings))
# print('----------------------------------')
# print('soup.p.previous_silibings type:',type(soup.p.previous_siblings))
# print('soup.p.previous_silibings list:',list(soup.p.previous_siblings))

# 前后节点
# .next_element:后一个节点
# .previous_element:前一个节点
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
# soup = BeautifulSoup(html,'lxml')
# print('soup.p.next_element:',repr(soup.p.next_element))
# print('soup.p.next_element.next_element:',repr(soup.p.next_element.next_element))
# print('soup.p.next_element.next_element.next_element:',repr(soup.p.next_element.next_element.next_element))
# print('soup.p.next_element.next_element.next_element.next_element:',repr(soup.p.next_element.next_element.next_element.next_element))
# print('-----------------')
# print('soup.p.previous_element:',repr(soup.p.previous_element))
# print('soup.p.previous_element.previous_element:',repr(soup.p.previous_element.previous_element))
# print('soup.p.previous_element.previous_element.previous_element:',repr(soup.p.previous_element.previous_element.previous_element))
# print('soup.p.previous_element.previous_element.previous_element.previous_element:',repr(soup.p.previous_element.previous_element.previous_element.previous_element))

# 所有前后节点
# .next_elements:所有后节点，返回生成器
# .previous_elemetns:所有前节点，返回生成器
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print('soup.p.next_elements type:',type(soup.p.next_elements))
# for i in soup.p.next_elements:
#     print('soup.p.next_element:',repr(i))
# print('-------------------------')
# print('soup.p.previous_elements type:',type(soup.p.previous_elements))
# for i in soup.p.previous_elements:
#     print('soup.p.previous_element:',repr(i))

# 搜索文档树
# find_all():当前标签的所有子节点及当前节点，返回一个列表
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<div>div-content<span>span-content</span></div>
"""
# soup = BeautifulSoup(html,'lxml')
# print(soup.find_all('p'))

# 通过正则找
import re
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda>panda-content</panda>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(re.compile('^p')))

# 通过列表查找
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda>panda-content</panda>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(['p','div']))

# 通过正则配合内容查找
from bs4 import BeautifulSoup
html = """
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda>panda-content</panda>
<div>div-content<span>span-content</span></div>
"""
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(text=re.compile('content$'))) # find_all()返回标签，内容用text

# 通过属性查找
# html = """
# <html><head></head>
# <body>
# <p><b>p-content1</b></p>
# <p>p-content2</p>
# <panda id='panda'>panda-content</panda>
# <div>div-content<span>span-content</span></div>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(id='panda'))

# 限制次数
# html = """
# <html><head></head>
# <body>
# <p><b>p-content1</b></p>
# <p>p-content2</p>
# <p>p-content3</p>
# <p>p-content4</p>
# <p>p-content5</p>
# <p>p-content6</p>
# <p>p-content7</p>
# <panda id='panda'>panda-content</panda>
# <div>div-content<span>span-content</span></div>
# """

# soup=BeautifulSoup(html,'lxml')
# print(soup.find_all('p',limit=3))

# find():返回第一个结果
# find_parent():在当前元素的父节点中查找，并返回第一个
# find_parents():在当前元素的父节点中查找，并列表
# find_next_sibling():在当前元素的兄弟节点中查找（弟弟），并返回第一个
# find_next_siblings():在当前元素的兄弟节点中查找（弟弟），并返回列表
# find_previous_sibling():在当前元素的兄弟节点中查找（哥哥），并返回第一个
# find_previous_siblings():在当前元素的兄弟节点中查找（哥哥），并返回列表
# find_next():在当前元素的相邻节点中查找（向下），并返回第一个
# find_all_next():在当前元素的相邻节点中查找（向下），并返回列表
# find_previous():在当前元素的相邻节点中查找（向上），并返回第一个
# find_all_previous():在当前元素的相邻节点中查找（向上），并返回列表

# css选择器
# 通过标签查找
# html = """
# <html><head></head>
# <body>
# <p><b>p-content1</b></p>
# <p>p-content2</p>
# <p class='p-class'>p-content3</p>
# <p>p-content4</p>
# <p class='p-class'>p-content5</p>
# <p>p-content6</p>
# <p>p-content7</p>
# <panda id='panda'>panda-content</panda>
# <div>div-content<span>span-content</span></div>
# """

# soup = BeautifulSoup(html,'lxml')
# print(soup.select('p'))

# 通过类名查找
# print(soup.select('.p-class'))
# 通过id名查找
# print(soup.select('#panda'))
# 组合查找
# print(soup.select('body panda'))
# 通过属性查找
# print(soup.select('p[class="p-class"]'))
