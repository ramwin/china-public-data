#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-01-17 18:20:56


"""
第一列: 门类 大类 中类 小类
"""
from openpyxl import Workbook, load_workbook
import re


wb = load_workbook('国民经济行业分类_v2.xlsx')
ws = wb.get_active_sheet()
matrix = []
for row_num, row in enumerate(ws.rows):
    matrix.append([])
    has_value = False
    for column, cell in enumerate(row):
        if cell.value:
            has_value = True
        matrix[row_num].append(cell.value)
    if has_value is False:  # 保证每一行都有数据
        raise Exception


for index, i in enumerate(matrix):
    if i[0] != '门类  大类  中类  小类' and i[0]:  # 标题 (门类，大类，中类，小类)
        print(i[0])
        print(index)
    if i[1]:  # 门类
        assert re.match(r'^[A-T]$', i[1])
    assert not i[2]
    if i[3]:  # 大类
        assert re.match(r'^\d{2}$', i[3])
    if i[4]:  # 标题（代码）
        assert i[4] == '代    码'
    if i[5]:  # 中类
        assert re.match(r'^\d{3}$', i[5])
    if i[6]:  # 中类
        assert re.match(r'^\d{3}$', i[6])
    if i[7]:  # 小类
        assert re.match(r'^\d{4}$', i[7])
    if i[8]:  # 门类名称
        pass
    if i[9]:  # 大类中类小类名称
        pass
    if i[10]:  # 大类中类小类名称
        pass
    if i[11]:  # 大类中类小类名称
        pass
    if i[12]:  # 大类中类小类名称
        pass
    if i[13]:
        assert i[13] == '表 1  国民经济行业分类和代码'
    if i[14]:
        assert i[14] == '类 别 名 称'
    if i[15]:  # 注释
        pass
    if i[16]:
        pass
    if i[17]:
        assert i[17] == '说    明'
    if i[18]:  # 页码
        assert re.match(r'^\d{2}$', i[18])
    if i[19]:  # 页码
        assert re.match(r'^\d{1}$', i[19])
