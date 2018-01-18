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


class Category(object):

    def __init__(self, code, name, parent=None):
        self.code = code
        self.name = name
        self.parent = parent
        self.children = []

    def to_dict(self):
        data = {
            'code': self.code,
            'name': self.name,
            'children': []
        }
        for child in self.children:
            data['children'].append(child.to_dict())
        return data

def count(*args):
    return len(list(filter(lambda x: x, args)))


def get_value(*args):
    assert count(*args) == 1
    return list(filter(lambda x: x, args))[0]


categories = []


def has_code(i):
    """是否存在code"""
    return count(i[3], i[4], i[5], i[6], i[7]) >= 1

num_code = '0'

for index, i in enumerate(matrix):
    if i[0] != '门类  大类  中类  小类' and i[0]:  # 标题 (门类，大类，中类，小类)
        print(i[0])
        print(index)
        assert count(*i) == 1
    if i[1]:  # 门类
        assert re.match(r'^[A-T]$', i[1])
        if not i[8]:
            assert i[9]
        else:
            assert not i[9]
        code = i[1]
        name = get_value(i[8], i[9])
        category_men = Category(code=code, name=name)
        categories.append(category_men)
    assert not i[2]
    if count(i[3], i[4], i[5], i[6], i[7]) > 1:
        if i[6] and i[7] and count(i[3], i[4], i[5], i[6], i[7]) == 2:
            pass # 中类和小类一个名字
        elif i[5] and i[7] and count(i[3], i[4], i[5], i[6], i[7]) == 2:
            pass # 中类和小类一个名字
        else:
            print("code很多")
            print(index)
    elif count(i[3], i[5], i[6], i[7]) == 1:
        new_num_code = get_value(i[3], i[5], i[6], i[7])
        if not new_num_code > num_code:
            print("新编码 %s" % new_num_code)
            print("旧编码 %s" % num_code)
            print(index)
        num_code = new_num_code
    if count(i[8], i[9], i[10], i[11], i[12]) > 1:
        print("Name很多")
        print(index)
    if i[3]:  # 大类
        assert re.match(r'^\d{2}$', i[3])
        code = i[3]
        name = get_value(i[8], i[9], i[10], i[11], i[12])
        category_da = Category(code=code, name=name, parent=category_men)
        category_men.children.append(category_da)
    if i[4]:  # 标题（代码）
        assert i[4] == '代    码'
    if i[5]:  # 中类
        assert re.match(r'^\d{3}$', i[5])
        assert i[9]
        code = i[5]
        name = get_value(i[8], i[9], i[10], i[11], i[12])
        category_zhong = Category(code=code, name=name, parent=category_da)
        category_da.children.append(category_zhong)
        if i[7]:
            category_xiao = Category(code=i[7], name=name, parent=category_zhong)
            category_zhong.children.append(category_xiao)
    if i[6]:  # 中类
        assert re.match(r'^\d{3}$', i[6])
        if not count(i[9], i[10]) == 1:
            print(index)
        code = i[6]
        name = get_value(i[8], i[9], i[10], i[11], i[12])
        category_zhong = Category(code=code, name=name, parent=category_da)
        category_da.children.append(category_zhong)
        if i[7]:
            category_xiao = Category(code=i[7], name=name, parent=category_zhong)
            category_zhong.children.append(category_xiao)
    if i[7]:  # 小类
        assert re.match(r'^\d{4}$', i[7])
        if not count(i[9], i[10], i[11], i[12]) == 1:
            print(index)
            print(i)
    if i[7]:
        if i[5] or i[6]:
            pass
        else:
            name = get_value(i[8], i[9], i[10], i[11], i[12])
            category_xiao = Category(code=i[7], name=name, parent=category_zhong)
            category_zhong.children.append(category_xiao)
    if i[8]:  # 门类名称
        pass
    if i[9]:  # 门类大类中类小类名称
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


results = []
for category in categories:
    results.append(category.to_dict())

import json
with open('results.json', 'w') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
