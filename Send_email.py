#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pip:pip install library_you_need -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
'''
#--------------------------------------------------------------#
#                                                              #
#--------------------------------------------------------------#
#
#                   @Project Name：Auto_Clock_in_NUAA                    #
#
#                   @File Name：Send_email.py                           #
#
#                   @Programmer：wzdrsy                   #
#
#                   @Start Date：2021/9/27 0027 14:21          #
#
#                   @Last Update：2021/9/27 0027 14:21         #
#-------------------------------------------------------------#   
#Class:
#                  SendEmail
#-------------------------------------------------------------#
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication
msg_from = '161983374@qq.com'  # 发送方邮箱
passwd = 'yybemuygyoojbgeb'  # 填入发送方邮箱的授权码
#msg_to = 'brianlin091994@gmail.com'  # 收件人邮箱
msg_to = '2557833850@qq.com'
subject = "闲鱼发货(测试)"  # 主题
class SendEmails():
    def Send(self, content):
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")

        except(s.SMTPException):
            print("发送失败")

        finally:
            s.quit()

    def Sendwithappendix(self, file_list):
        """
                发送邮件
                :param file_list: 附件文件列表
                """
        try:
            # 创建一个带附件的实例
            msg = MIMEMultipart()
            # 发件人格式
            msg['Subject'] = subject
            msg['From'] = msg_from
            msg['To'] = msg_to

            # 邮件正文内容
            msg.attach(MIMEText(subject, 'plain', 'utf-8'))

            # 多个附件
            for file_name in file_list:
                print("file_name", file_name)
                # 构造附件
                xlsxpart = MIMEApplication(open(file_name, 'rb').read())
                # filename表示邮件中显示的附件名
                xlsxpart.add_header('Content-Disposition', 'attachment', filename='%s' % file_name)
                msg.attach(xlsxpart)

            try:
                s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
                s.login(msg_from, passwd)
                s.sendmail(msg_from, msg_to, msg.as_string())
                print("发送成功")

            except(s.SMTPException):
                print("发送失败")

            finally:
                s.quit()
        except Exception as e:
            print(e)

