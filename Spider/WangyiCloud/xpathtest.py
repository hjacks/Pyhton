from lxml import etree
html = etree.parse("hello.html")
#print(type(html))

# result = html.xpath("//li")
# print(result)
# print(len(result))
# print(type(result))
# print(type(result[0]))

# result = html.xpath("//li/@class")
# print(result)

# result = html.xpath("//li//a[@href='link1html']")
# print(result)
# print(result[0].text)

# result = html.xpath("//li//span")
# print(result)
# print(result[0].text)

# result = html.xpath("//li/a//@class")
# print(result)

# result = html.xpath("//li[last()]/a/@href")
# print(result)

result = html.xpath("//li[last()-1]/a")
print(result)

# result = html.xpath('//*[@class="bold"]')
# print(result)
# print(result[0].tag)
# print(result[0].text)