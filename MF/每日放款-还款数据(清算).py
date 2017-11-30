#-*- coding:utf-8 -*-
#!/usr/bin/python
import smtplib
import datetime
import pymysql
from email.mime.text import MIMEText



mailto_list=['']

mail_host=""  #设置服务器
mail_user=""  #用户名
mail_pass=""   #口令



mail_cc = ['']


#当前时间
day_now=datetime.date.today()-datetime.timedelta(days=1)
# 当前日期-7
day = datetime.date.today()-datetime.timedelta(days=1)
# 月初
day_from = datetime.date(day.year, day.month, 1)
# 上月最后一天
day_tmp = datetime.date(day.year, day.month, 1) - datetime.timedelta(days=8)
# 上月的今天
try:
    last_month_day = datetime.date(day_tmp.year, day_tmp.month, day.day)
except:
    last_month_day = datetime.date(day_tmp.year, day_tmp.month, day.day-1)
    pass
# 上月的月初
last_month_day_from = datetime.date(day_tmp.year, day_tmp.month, 1)
# 当前日期往前推 31 天
day_pre = datetime.date.today()-datetime.timedelta(days=31)



#发送邮件
def send_mail(to_list,sub,content,cc):  #to_list：收件人；sub：主题；content：邮件内容
    me=""
    
    msg = MIMEText(content,_subtype='html',_charset='utf8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)
    msg['CC'] = ";".join(cc)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except smtplib.SMTPException:
        print (smtplib.SMTPException)
        return False

def make_html_table(content_list):
    content = '<table border="1" align="center" cellpadding="4" cellspacing="0" bordercolor="#000000"> \n'
    for l in content_list:
        content += '<tr>'
        for data in l:
            if l.index(data) in (1,3,4,5,6,7):
                content += '<td align="center" width="60">' + str(data) + '</td>'
            elif l.index(data) == 2:
                content += '<td align="center" width="60">' + str(data) + '</td>'
            else:
                content += '<td align="center" width="60">' + str(data) + '</td>'
        content += '</tr> \n'
    content += '</table> \n\n'
    return content

def make_html_table_2(content_list,table_name):
    content = '<table border="1" align="center" cellpadding="4" cellspacing="0" bordercolor="#000000"> \n'
    content += '<tr align="center"><td colspan="' + str(len(content_list[0])) + '">'+ table_name +'</td></tr>'
    for l in content_list:
        content += '<tr>'
        for data in l:
            if l.index(data) in (8,10):
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
            elif l.index(data) == 9:
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
            else:
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
        content += '</tr> \n'
    content += '</table> \n\n'
    return content


def getdata_1(table_name):
    content_list = []

    head_1 = ['日期\t', '放款笔数','放款金额', '还款笔数', '还款金额','逾期费'];
    content_list.append(head_1)

    # link=['月环比','0', '0', '0', '0', '0'] #月环比
    # content_list.append(link)

    # 日期  放款回款数据
    sql1 = "SELECT t1.day_key,t1.order_cnt,t1.order_amount,t2.repay_cnt,t2.actual_fee,t2.overdue_fee FROM \
            (SELECT date(arrive_time) as day_key,count(id) as order_cnt,sum(actual_balance) as order_amount \
             from  bmdb.tb_credit_record where arrive_time>='%s' and date(arrive_time)<='%s'   GROUP BY 1 )t1 left JOIN \
            (SELECT date(create_time) as day_key,count(credit_id) as repay_cnt,sum(actual_fee) as actual_fee,sum(overdue_fee) as overdue_fee \
            from  bmdb.tb_repayment_record where create_time>='%s'   and  date(create_time)<='%s'  GROUP BY 1 \
            )t2 on t1.day_key=t2.day_key GROUP BY 1,2,3,4,5,6 ORDER BY 1 desc;" %(day_from,day_now,day_from,day_now)
    cursor.execute(sql1)
    result1 = cursor.fetchall()

    for data in result1:
        d = str(data[0])
        line = [d,'0','0', '0', '0', '0']
        if not data[1] == None:
            line[1] = str(data[1])
        if not data[2] == None:
            line[2] = str(data[2])
        if not data[3] == None:
            line[3] = str(data[3])
        if not data[4] == None:
            line[4] = str(data[4])
        if not data[5] == None:
            line[5] = str(data[5])
            #line[5] = str(round(data[4]*100,2))+'%'
        content_list.append(line)


    # 生成html
    content_1 = make_html_table_2(content_list,table_name)
    return content_1


if __name__ == '__main__':
    # 连接mysql
    conn = pymysql.connect(db="", user="", passwd="", host="", port=)
    cursor = conn.cursor()

    neirong1=u'<ul style="padding:0 65px"><meta charset="UTF-8"> hi all,相关数据如下:<br/></ul>'
    # print(1)
    content = '<html lang="en"><head><meta charset="UTF-8"><title>title</title></head><body>\n'
    # print(3)
    #报表头部
    content += '<h1 align="center">每日放款-还款数据(清算)</h1>'

    content += neirong1.encode('utf-8')
    #getdata表格

    content += getdata_1('1.每日放款-还款数据(清算)')

    content += '</html>\n\n'

    if send_mail(mailto_list,u"每日放款-还款数据(清算)",content,mail_cc):
        print (str(day) +'send mail succeed!')
    else:
        send_mail('',"邮件报表发送失败","邮件报表发送失败",'')

    cursor.close()
    conn.close()
