#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-01-17 10:46:13


from bs4 import BeautifulSoup

file_path = "国民经济行业分类_2017_prettify.html"
soup = BeautifulSoup(open(file_path).read(), 'html.parser')
body = soup.body
nodes = list(filter(lambda x: x!='\n', body.children))
top_values = set()
left_values = set()
for node in nodes:
    try:
        assert node.name == 'div'
        assert node.span.text.strip()
    except Exception as e:
        print(node)
        break
