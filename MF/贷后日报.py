#-*- coding:utf-8 -*-
#!/usr/bin/python
import smtplib
import datetime
import pymysql
from email.mime.text import MIMEText

mailto_list = []


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


def getdata(task_status,task_status_1,product_id,product_id_1,table_name):
    content_list = []

    head_1 = ['应还日期\t', '应还笔数', '提前还款', '正常还款', '逾期还款', '逾期笔数','首逾率','逾期率','回收率'];
    content_list.append(head_1)

    # link=['月环比','0', '0', '0', '0', '0'] #月环比
    # content_list.append(link)

    # 日期  审核通过率
    sql1 = " select  t1.day_key as shouldback_day \
    ,count(distinct t1.id) as shouldback_cnt \
    ,count(distinct case when is_front='1' then t2.credit_id else null end) as pre_repay_cnt \
    ,count(distinct case when is_front='0' then t2.credit_id else null end) as normal_repay_cnt \
    ,count(distinct case when is_front='-1' then t1.id else null end) as overdue_repay_cnt \
    ,count(distinct case when t1.status in(6,8) then t1.id else null end) as untill_overdue_cnt \
    ,(count(distinct t1.id)-count(distinct case when is_front in('1','0') then t2.credit_id else null end))*1.0 \
    /count(distinct t1.id) as first_overdue_lv \
    ,count(distinct case when t1.status in(6,8)   then t1.id else null end)*1.0/count(distinct t1.id) as overdue_lv \
    ,count(distinct case when is_front='-1' then t1.id else null end)*1.0/ \
    (count(distinct case when is_front='-1' then t1.id else null end) \
    +count(distinct case when t1.status in(6,8) then t1.id else null end)) as recovery_lv \
    from  \
    ( select date(shouldback_time) as day_key \
        ,id,uid,status from  bmdb.tb_credit_record \
        where date(shouldback_time)>=date('%s') and date(shouldback_time) <= date('%s') and task_status in('%s','%s') and product_id in('%s','%s') group by 1,2,3 \
    )t1 left  join \
    (select credit_id,(case when date(normal_time) > date(actual_time) then '1' \
        when date(normal_time) = date(actual_time) then '0' \
        when date(normal_time) < date(actual_time) then '-1' end ) as is_front \
        from  bmdb.tb_repayment_record group by 1,2 \
    )t2  on t1.id=t2.credit_id group by t1.day_key ORDER BY 1 desc;"  %(day_from,day_now,task_status,task_status_1,product_id,product_id_1)

    cursor.execute(sql1)
    result1 = cursor.fetchall()

    for data in result1:
        d = str(data[0])
        line = [d, '0', '0', '0', '0', '0','0','0','0']
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
        if not data[6] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[6] = str(round(data[6]*100,2))+'%'
        if not data[7] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[7] = str(round(data[7]*100,2))+'%'
        if not data[8] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[8] = str(round(data[8]*100,2))+'%'
        content_list.append(line)

    # 生成html
    content_1 = make_html_table_2(content_list,table_name)
    return content_1

def getdata_1(product_id,product_id_1,is_new,table_name):
    content_list = []

    head_1 = ['应还日期\t', '应还笔数', '提前还款', '正常还款', '逾期还款', '逾期笔数','首逾率','逾期率','回收率'];
    content_list.append(head_1)

    # link=['月环比','0', '0', '0', '0', '0'] #月环比
    # content_list.append(link)

    # 
    sql1 = "select t1.day_key as shouldback_day ,count(distinct t1.id) as shouldback_cnt\
    ,count(distinct case when is_front='1' then t2.credit_id else null end) as pre_repay_cnt \
    ,count(distinct case when is_front='0' then t2.credit_id else null end) as normal_repay_cnt \
    ,count(distinct case when is_front='-1' then t1.id else null end) as overdue_repay_cnt \
    ,count(distinct case when t1.status in(6,8) then t1.id else null end) as untill_overdue_cnt \
    ,(count(distinct t1.id)-count(distinct case when is_front in('1','0') then t2.credit_id else null end))*1.0 \
   /count(distinct t1.id) as first_overdue_lv \
   ,count(distinct case when t1.status in(6,8)   then t1.id else null end)*1.0/count(distinct t1.id) as overdue_lv \
   ,count(distinct case when is_front='-1' then t1.id else null end)*1.0 \
   /(count(distinct case when is_front='-1' then t1.id else null end)+count(distinct case when t1.status in(6,8) then t1.id else null end)) as recovery_lv \
   from (select a1.day_key,a1.id,a1.status,a2.credit_id,a2.user_id from \
        (select date(shouldback_time) as day_key,id,uid,status \
         from  bmdb.tb_credit_record  where  shouldback_time>=date('%s') and shouldback_time <= date('%s') \
         and product_id in('%s','%s') and task_status=0 group by 1,2,3,4 \
        ) a1 left join \
        ( select user_id,credit_id from reportdb.agg_first_success_loan_repay_user )a2 on a1.uid=a2.user_id \
        group by a1.day_key,a1.id,a1.status,a2.credit_id,a2.user_id \
    )t1 left  join \
    (select credit_id \
     ,(case when date(normal_time) > date(actual_time) then '1' when date(normal_time) = date(actual_time) then '0' \
        when date(normal_time) < date(actual_time) then '-1' end ) as is_front \
        from  bmdb.tb_repayment_record group by 1,2 \
    )t2  on t1.id=t2.credit_id  \
    where (case when t1.user_id is not null and t1.credit_id<>t1.id then 0 else 1 end)='%s' \
group by t1.day_key ORDER BY 1 desc;"  %(day_from,day_now,product_id,product_id_1,is_new)

    cursor.execute(sql1)
    result1 = cursor.fetchall()

    for data in result1:
        d = str(data[0])
        line = [d, '0', '0', '0', '0', '0','0','0','0']
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
        if not data[6] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[6] = str(round(data[6]*100,2))+'%'
        if not data[7] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[7] = str(round(data[7]*100,2))+'%'
        if not data[8] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[8] = str(round(data[8]*100,2))+'%'
        content_list.append(line)

    # 生成html
    content_1 = make_html_table_2(content_list,table_name)
    return content_1


if __name__ == '__main__':
    # 连接mysql
    conn = pymysql.connect(db="", user="", passwd="", host="", port=)
    cursor = conn.cursor()

    neirong1=u'<ul style="padding:0 65px"><meta charset="UTF-8"> hi all,昨天数据如下:<br/></ul>'
    # print(1)
    # neirong2 = u'<p style="padding:0 65px">ps：类型push之类没有特定时间点和规律的活动，带来的导单量，请相关人员回复本邮件，一周我会汇总一次数据，感谢配合！</p>'
    # print(2)
    content = '<html lang="en"><head><meta charset="UTF-8"><title>title</title></head><body>\n'
    # print(3)
    #报表头部
    content += '<h1 align="center">贷后日报</h1>'
    #print(4)
    content += neirong1.encode('utf-8')
    # getdata表格
    content += getdata(3,7,1,3,'1.贷后-7天-新客')
    content += '<h1 <br/> </h1>'
    content += getdata(4,7,1,3,'2.贷后-7天-老客')
    content += '<h1 <br/> </h1>'
    content += getdata(1,2,1,3,'3.贷后-7天-白客')
    content += '<h1 <br/> </h1>'
    content += getdata(3,7,2,4,'4.贷后-14天-新客')
    content += '<h1 <br/> </h1>'
    content += getdata(4,7,2,4,'5.贷后-14天-老客')
    content += '<h1 <br/> </h1>'
    content += getdata(1,2,2,4,'6.贷后-14天-白客')
    content += '<h1 <br/> </h1>'

    #content += getdata_1(1,3,1,'7.贷后-7天-新客(白名单上线前存量用户)')
    #content += '<h1 <br/> </h1>'
    #content += getdata_1(1,3,0,'8.贷后-7天-老客(白名单上线前存量用户)')
    #content += '<h1 <br/> </h1>'
    #content += getdata_1(2,4,1,'9.贷后-14天-新客(白名单上线前存量用户)')
    #content += '<h1 <br/> </h1>'
    #content += getdata_1(2,4,0,'10.贷后-14天-老客(白名单上线前存量用户)')
    #content += '<h1 <br/> </h1>'
    #print(5)
    content += '</html>\n\n'

    if send_mail(mailto_list,u"贷后日报",content,mail_cc):
        print ('send mail succeed!')
    else:
        send_mail('zhoushibin@51jnq.com',"邮件报表发送失败","邮件报表发送失败",'zhoushibin@51jnq.com')

    cursor.close()
    conn.close()
