# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:33:37 2017

@author: Administrator
"""

from email.header import  Header
from email.mime.multipart import MIMEMultipart
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

# 构造附件1
att1=MIMEText(open('/Users/Administrator/Desktop/123.jpg','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="123.jpg"'
msg.attach(att1)

# 构造附件2
att2=MIMEText(open('/Users/Administrator/Desktop/456.txt','rb').read(),'base64','utf-8')
att2['Content-Type']='application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="456.txt"'
msg.attach(att2)

sever_semp=smtplib.SMTP(smtp_sever,25)
sever_semp.login(from_addr,password)
sever_semp.sendmail(from_addr,[to_addr],msg.as_string())
sever_semp.quit()
    
