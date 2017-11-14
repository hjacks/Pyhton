# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:33:37 2017

@author: Administrator
"""

from email import encoders
from email.header import  Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr='xutao@51jnq.com'
password='xt123123654..'
to_addr='CuVees@163.com'
smtp_sever='smtp.mxhichina.com'

msg=MIMEMultipart()
msg['From']=_format_addr('python爱好者<%s>' %from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自徐涛的问候。。。','utf-8').encode()

msg.attach(MIMEText('send with file...','plain','utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/Administrator/Desktop/123.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='123.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

sever_semp=smtplib.SMTP(smtp_sever,25)
sever_semp.login(from_addr,password)
sever_semp.sendmail(from_addr,[to_addr],msg.as_string())
sever_semp.quit()
    

