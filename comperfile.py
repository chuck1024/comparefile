# -*- coding: utf-8 -*-

__author__='chuck1024'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import commands
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import shutil
import time
import urllib
import urllib2

localtime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
commands.getoutput("diff -r -a /tmp /newtmp > /opt/comperfile/result/out1.txt")
commands.getoutput("diff -r -a /tmp1 /newtmp1 > /opt/comperfile/result/out2.txt")
commands.getoutput("cat /opt/comperfile/result/out1.txt /opt/comperfile/result/out2.txt >  /opt/comperfile/result/out.txt")

f = open("/opt/comperfile/result/out.txt")
ff=f.read()
f.close()
r = r'diff -r'
#r1 = r'Only'
count = len(re.findall(r,ff))
#count2 = len(re.findall(r1,ff))
#count = count1 + count2
#print count
f = open("/opt/comperfile/result/out.txt")
c = 0
d = 0
for eachLine in f.readlines():
        if 'Only' in eachLine and 'data' in eachLine:
                c+=1
        if 'Only' in eachLine and 'apps' in eachLine:
                d+=1
#print c
#print d

with open('/opt/comperfile/result/out.txt', 'r') as f:
    with open('/opt/comperfile/result/outs.txt', 'w') as g:
        for line in f.readlines():
            if 'diff -r' in line or 'Only in' in line:
                g.write(line)
shutil.move('/opt/comperfile/result/outs.txt', '/opt/comperfile/result/out.txt')

number1 =int(commands.getoutput("find /apps/static -type f | wc -l"))
number2 =int(commands.getoutput("find /apps/ui_template -type f | wc -l"))
number = number1 + number2

mobile = '18888888888'
mobile1 = '13000000000'

// 发送短信模板
def SendSMS(mobile,msg):
   header = {"Content-Type":"application/json"}
   urlnm='*******'
   values ={'templateNo':'64001','mobileNo':mobile,'content':msg,'key':'**************'}
   jdata = urllib.urlencode(values)
   req = urllib2.Request(urlnm,jdata)
   print req.get_full_url()
   response = urllib2.urlopen(req)
   return response.read()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

//收发邮件信息
from_addr = '*******@qq.com'
password = '******'
to_addr = ['****@qq.com']
to_addr1 = ['******@163.com',]
smtp_server = 'smtp.qq.com'
smtp_port = 25

to_string =''
for item in to_addr:
        to_string += item +','
to_string1 =''
for item1 in to_addr1:
        to_string1 +=item1 +','

msg = MIMEMultipart()
msg['From'] = _format_addr('啦啦啦<%s>' % from_addr)
if count != 0 or c != 0 or d != 0:
        msg['To'] = to_string
	msg['Subject'] = Header('%s 文件对比结果' %localtime, 'utf-8').encode()
        msg.attach(MIMEText('%s \n####文件对比结果####\n对比的文件总数: %s \n差异文件的数量: %s\n线上增加文件的数量: %s\n线上删除文件的数量: %s\n' %(localtime,number,count,c,d), 'plain', 'utf-8'))
#	str='文件对比结果异常！具体见邮件附件！'
#	resp=SendSMS(mobile,str)
#        print resp
else:
	msg['TO'] = to_string1
        msg['Subject'] = Header('没有异常!!！文件对比结果 %s'%localtime, 'utf-8').encode()
        msg.attach(MIMEText('%s \n####文件对比结果####\n对比的文件总数: %s \n没有异常!!!' %(localtime,number),'plain', 'utf-8'))
#	str1='文件对比结果无异常！！！'
 #       resp1=SendSMS(mobile1,str1)
 #      print resp1

if count != 0 or c != 0 or d != 0:
	att2 = MIMEText(open('/opt/comperfile/result/out.txt', 'rb').read(), 'base64', 'utf-8')
	att2["Content-Type"] = 'application/octet-stream'
	att2["Content-Disposition"] = 'attachment; filename="result.txt"'
	msg.attach(att2)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
	str='文件对比结果异常！具体见邮件附件！'
        resp=SendSMS(mobile,str)
        print resp
else:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr1, msg.as_string())
        server.quit()
	str1='文件对比结果无异常！！！'
        resp1=SendSMS(mobile1,str1)
        print resp1
