#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pip:pip install library_you_need -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
'''
#--------------------------------------------------------------#
#                                                              #
#--------------------------------------------------------------#
#
#                   @Project Name：RAP                    #
#
#                   @File Name：1.py                           #
#
#                   @Programmer：WZDRSY                   #
#
#                   @Start Date：2022/8/9 14:11          #
#
#                   @Last Update：2022/8/9 14:11         #
#-------------------------------------------------------------#   
#Class:
#
#-------------------------------------------------------------#
'''
from Send_email import SendEmails
import pandas as pd
if __name__ == '__main__':
    send_email = SendEmails()
    # 替换成自己的df
    df = pd.read_excel('commission_fee_20220809.xlsx',engine='openpyxl')
    # df = pd.DataFrame({
    #     'A': [1, 2, 3],
    #     'B': [4.1, 5.2, 6.3],
    #     'C': ["7", "8", "9"]})

    # send_email.Send(df.to_string())
    file_list = ['commission_fee_20220809.xlsx']
    send_email.Sendwithappendix(file_list)