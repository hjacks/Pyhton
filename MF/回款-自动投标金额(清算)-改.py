#-*- coding:utf-8 -*-
#!/usr/bin/python
import smtplib
import datetime
import pymysql
from email.mime.text import MIMEText
import sys
type1 = sys.getfilesystemencoding()



mailto_list=['']

mail_host=""  #设置服务器
mail_user=""  #用户名
mail_pass=""   #口令
mail_cc = ['']


# #当前时间
# day_now=datetime.date.today()-datetime.timedelta(days=0)
day_now=datetime.date.today()
day_end = datetime.date.today()+datetime.timedelta(days=10)
# # 月初
# day_from = datetime.date(day.year, day.month, 1)
# # 上月最后一天
# day_tmp = datetime.date(day.year, day.month, 1) - datetime.timedelta(days=8)
# # 上月的今天
# try:
#     last_month_day = datetime.date(day_tmp.year, day_tmp.month, day.day)
# except:
#     last_month_day = datetime.date(day_tmp.year, day_tmp.month, day.day-1)
#     pass
# # 上月的月初
# last_month_day_from = datetime.date(day_tmp.year, day_tmp.month, 1)
# # 当前日期往前推 31 天
# day_pre = datetime.date.today()-datetime.timedelta(days=31)



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

def make_html_table_2(content_list,table_name):
    content = '<table border="1" align="center" cellpadding="4" cellspacing="0" bordercolor="#000000"> \n'
    content += '<tr align="center"><td colspan="' + str(len(content_list[0])) + '">'+ table_name +'</td></tr>'
    for l in content_list:
        content += '<tr>'
        for data in l:
            if l.index(data) in (2,10):
                content += '<td width="120"><font size="2px">' + str(data) + '</td>'
            elif l.index(data) == 9:
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
            else:
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
        content += '</tr> \n'
    content += '</table> \n\n'
    return content

# def getdata():

#     content_list = []
#     head_1 = ['日期\t', '预计回款金额', '预计自动投标金额']; 
#     content_list.append(head_1)
#     begin =day_now
#     end = day
#     star=begin
#     delta = datetime.timedelta(days=1)  
#    while star!=end:
#         sql1 = "SELECT DATE_ADD('%s', INTERVAL 1 DAY),sum(t1.amount) as back_amount \
#         ,sum(case when t2.uid is not null and COALESCE((t1.amount-t2.amount),0)>0 then COALESCE((t1.amount-t2.amount),0) else 0 end) as auto_amount \
#         FROM (SELECT a.uid,sum(amount) as amount FROM(SELECT t1.uid as uid,invest_detail_id,sum(t1.profit_amount) + t1.profit_amount + t2.invest_amount as  amount \
#         FROM licaidb.tblc_invest_detail_repay t1 LEFT JOIN licaidb.tblc_invest_detail t2 ON t1.invest_detail_id = t2.id \
#         WHERE invest_detail_id IN (SELECT id FROM licaidb.tblc_invest_detail \
#         WHERE(expect_repay_time = DATE_ADD('%s', INTERVAL 1 DAY) OR repay_time = '%s')AND invest_status = 1) GROUP BY 1,2 \
#         )a GROUP BY 1) t1 LEFT JOIN( \
#         SELECT uid,amount from licaidb.tblc_user_invest_auto where auto=1 GROUP BY 1 \
#         )t2 on t1.uid=t2.uid;" %(star,star,star)

#         cursor.execute(sql1)
#         data= cursor.fetchall()
#         line = ['0', '0', '0']
#         #for data in result1:
#         print (data[0][0])

#         content_list.append(line)

#         star+=delta
#         # 生成html
#     content_1 = make_html_table_2(content_list,u'1.回款/自动投标金额(清算)')
#     return content_1

def getdata(table_name):
    content_list = []
    head_1 = ['日期\t', '预计回款金额', '预计自动投标金额']
    content_list.append(head_1)
    start = day_now
    end = day_end
    day = start
    delta = datetime.timedelta(days=1)
    while day != end:
        sql1 = "SELECT DATE_ADD('%s', INTERVAL 1 DAY),sum(t1.amount) as back_amount \
        ,sum(case when t2.uid is not null and COALESCE((t1.amount-t2.amount),0)>0 then COALESCE((t1.amount-t2.amount),0) else 0 end) as auto_amount \
        FROM (SELECT a.uid,sum(amount) as amount FROM(SELECT t1.uid as uid,invest_detail_id,sum(t1.profit_amount) + t1.profit_amount + t2.invest_amount as  amount \
        FROM licaidb.tblc_invest_detail_repay t1 LEFT JOIN licaidb.tblc_invest_detail t2 ON t1.invest_detail_id = t2.id \
        WHERE invest_detail_id IN (SELECT id FROM licaidb.tblc_invest_detail \
        WHERE(expect_repay_time = DATE_ADD('%s', INTERVAL 1 DAY) OR repay_time = '%s')AND invest_status = 1) GROUP BY 1,2 \
        )a GROUP BY 1) t1 LEFT JOIN( \
        SELECT uid,amount from licaidb.tblc_user_invest_auto where auto=1 GROUP BY 1 \
        )t2 on t1.uid=t2.uid;" %(day,day,day)
        cursor.execute(sql1)
        #conn.commit()
        data= cursor.fetchall()
        #d = str(data[0])

        line = [str(data[0][0]),str(data[0][1]),str(data[0][2])]
        #print(line)
        content_list.append(line)
        day+=delta
        content_1 = make_html_table_2(content_list,table_name)
    return content_1

if __name__ == '__main__':
    # 连接mysql
    conn = pymysql.connect(db="", user="", passwd="", host="", port=)
    cursor = conn.cursor()

    neirong1=u'<ul style="padding:0 65px"><meta charset="UTF-8"> hi all,相关数据如下:<br/></ul>'

    content = '<html lang="en"><head><meta charset="UTF-8"><title>title</title></head><body>\n'
    content += '<h1 align="center">回款/自动投标金额(清算)</h1>'
    # neirong2=u'1.预计明日回款:'+str(date[0][0])
    # neirong3=u'2.自动投标金额:'+str(date[0][1])
    content += neirong1.encode('utf-8')
    # content += neirong2.encode('utf-8')
    # content += '<br/>'
    # content += neirong3.encode('utf-8')
    # content += '</html>\n\n'

    content += getdata('1.回款/自动投标金额(清算)')
    content += '<h1 <br/> </h1>'
    #print(5)
    content += '</html>\n\n'

    if send_mail(mailto_list,u"回款/自动投标金额(清算)",content,mail_cc):
       print ('send mail succeed!')
    else:
       send_mail('',"邮件报表发送失败","邮件报表发送失败",'')

    cursor.close()
    conn.close()
