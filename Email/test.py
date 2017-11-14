# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:16:07 2017

@author: Administrator
"""

from email.header import  Header
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

msg=MIMEText('hello,send by xiaohao...','plain','utf-8')
msg['From']=_format_addr("python爱好者<%s>" %from_addr)
msg['To']=_format_addr("管理员<%s>" %to_addr)
msg['Subject']=Header("来自STMP的问候",'utf-8').encode()

sever=smtplib.SMTP(smtp_sever,25)
sever.set_debuglevel(1)
sever.login(from_addr,password)
sever.sendmail(from_addr,[to_addr],msg.as_string())
sever.quit()


