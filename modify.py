#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-01-17 10:46:13


import re
from bs4 import BeautifulSoup
from openpyxl import Workbook

file_path = "国民经济行业分类_2017_prettify.html"
soup = BeautifulSoup(open(file_path).read(), 'html.parser')
body = soup.body
nodes = list(filter(lambda x: x!='\n', body.children))
top_values = set()
left_values = set()


class Style(object):
    def __init__(self, data):
        self._data = {}
        for key, value in data.items():
            if value[-2:] == 'px':
                self._data[key] = int(value[0:-2])
            else:
                self._data[key] = value
    @classmethod
    def from_text(cls, text):
        """返回一个 Style 的类"""
        attrs = re.split(r'; *', text.strip())
        data = {}
        for attr in attrs:
            if re.match(r'^\s*$', attr):
                continue
            key, value = re.split(r': *', attr)
            data[key] = value
        return cls(data)


class Cell(object):
    def __init__(self, style, text):
        self.text = text
        self.style = style
        self.top = None
        self.left = None


cells = []
for node in nodes:
    try:
        assert node.name == 'div'
        assert node.span.text.strip()
        style = Style.from_text(node['style'])
        cell = Cell(text=node.span.text.strip(), style=style)
        top_values.add(cell.style._data['top'])
        left_values.add(cell.style._data['left'])
        cells.append(cell)
    except Exception as e:
        raise e
        print(e)
        print(node)
        break


left_value_index = {}  # 135:1  偏移135像素的是第零个格子
for index, value in enumerate(sorted(left_values)):
    left_value_index[value] = index
top_value_index = {}
for index, value in enumerate(sorted(top_values)):
    top_value_index[value] = index
for cell in cells:
    cell.top = top_value_index[cell.style._data['top']]
    cell.left = left_value_index[cell.style._data['left']]


import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.get_active_sheet()
for cell in cells:
    ws.cell(row=int(cell.top)+1, column=int(cell.left)+1, value=cell.text)
wb.save('国民经济行业分类.xlsx')
