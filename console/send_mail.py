#coding=utf-8

__author__ = 'John Wang'
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib

from_addr = input('From:') or 'wzjg520@126.com'
password = input('password:') or 'xhcljjjzyqtlst'
to_addr = input('To:') or 'phpandjs@sina.com'
content = input('Content:') or 'hello word'

smtp_server = input('SMTP server:') or 'smtp.126.com'

port = 25
while smtp_server is '':
    smtp_server = input('SMTP server:')
    if smtp_server is '':
        continue
    smpt_arr = smtp_server.split(':')
    if len(smpt_arr) == 2:
        port = smpt_arr[1]
    smtp_server = smpt_arr[0]



def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr('媳妇这是我用python发的牛逼吧<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自python脚本的问候', 'utf-8').encode()

try:
    smtp = smtplib.SMTP(smtp_server, port)
    smtp.starttls()
    smtp.set_debuglevel(1)
    smtp.login(from_addr, password)
    ret = smtp.sendmail(from_addr, [to_addr], msg.as_string())
    smtp.quit()
    print(ret)
except:
    # print('excute error')
    pass





