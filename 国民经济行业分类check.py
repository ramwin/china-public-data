#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-01-16 18:11:43


import re


f = open("国民经济行业分类_2017.txt")
line = True
index = 0
current_menlei = {}
current_dalei = {}
current_zhonglei = {}
current_xiaolei = {}
while line:
    line = f.readline(); index += 1
    # print("当前处理: %s" % line)
    # 普通的注释行
    if re.match(
            r'(^代    码\n$)|'
            r'(^门类  大类  中类  小类\n$)|'
            r'(^类 别 名 称\n$)|'
            r'(^说    明\n$)'
        , line):
        pass
    elif re.match(r'^[A-Z]\n$', line):
        current_menlei['code'] = line.strip()
        line = f.readline(); index+=1
        current_menlei['name'] = line.strip()
        # print("遇到了门类: %s" % current_menlei)
    elif re.match(r'^\d{2}\n$', line):
        current_dalei['code'] = line.strip()
        line = f.readline(); index+=1
        current_dalei['name'] = line.strip()
        # print("遇到了大类: %s" % current_dalei)
    elif re.match(r'^\d{3}\n$', line):
        current_zhonglei['code'] = line.strip()
        line = f.readline(); index+=1
        if re.match(r'^\d{4}\n$', line):  # 中类没名字:
            current_zhonglei['name'] = ""
            print("中类:%s没名字" % current_zhonglei['code'])
            line = f.readline(); index+=1
            current_xiaolei['name'] = line.strip()
            current_xiaolei['code'] = line.strip()
        else:
            current_zhonglei['name'] = line.strip()
        # print("遇到了中类: %s" % current_zhonglei)
    elif re.match(r'^\d{4}\n$', line):
        current_xiaolei['code'] = line.strip()
        line = f.readline(); index+=1
        current_xiaolei['name'] = line.strip()
        # print("遇到了小类: %s" % current_xiaolei)
    elif re.match(r'^注释: .*\n$', line):
        pass
        # print("遇到了注释: %s" % line.strip())
    else:
        print("第%d行处理不了"%index)
        break
