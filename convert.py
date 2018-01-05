#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-19 15:44:29

import pprint
import csv
import re
import json
from collections import OrderedDict


file_name = 'sw.csv'


class Industry(object):
    """代表了行业的类"""
    def __init__(self, name, code, parent=None, index_code=None):
        self.name = name.strip()
        self.code = str(code)
        self.parent = parent
        self.children = []
        self.index_code = index_code

    def has_child(self, industry):
        """self的children里面是存在code和industry的code一致的元素"""
        for i in self.children:
            if i == industry:
                return True
        else:
            return False

    def has_generation(self, industry):
        """self的children， children的children里面是否存在和industry的code一致的元素"""
        pass

    def code_without_zero(self):
        return re.sub("(00)*$", "", self.code)

    def contains(self, industry):
        """判断一个industry是否属于self"""
        return industry.code_without_zero() != self.code_without_zero() and \
            industry.code_without_zero().startswith(self.code_without_zero())

    def contains_directly(self, industry):
        """判断一个industry是不是直接隶属于self"""
        if not self.contains(industry):
            return False
        return len(industry.code_without_zero()) - len(self.code_without_zero()) == 2

    def get_next_level(self, industry):
        """返回self的children里面是industry的组辈的那个元素"""
        for i in self.children:
            if i.contains(industry):
                return i
        return None

    def get_next_level_of_industry(self, industry):
        """返回industry的父辈们，哪个应该是直接隶属于self的"""
        assert self.contains(industry)
        while True:
            if industry.parent == self:
                return industry
            else:
                return self.get_next_level_of_industry(industry.parent)

    def insert(self, industry):
        """把industry加入到self的children或者children的children里面"""
        print("把%s加入%s" % (industry, self))
        assert self.contains(industry)
        if self.contains_directly(industry):
            if self.has_child(industry):
                pass
            else:
                print("把%s加入%s的children"%(industry, self))
                industry.parent = self  # 有待商榷，内存泄露
                self.children.append(industry)
        else:
            next_level = self.get_next_level(industry)
            if next_level:
                next_level.insert(industry)
            for child in self.children:
                if child.contains(industry):
                    child.insert(industry)
                    break
            else:
                raise Exception("没有这个元素，你怎么添加了呢")

    @property
    def ancestor(self):
        if self.parent:
            return self.parent.ancestor
        else:
            return self

    def to_dict(self):
        """返回dict格式"""
        return {}

    def __str__(self):
        return self.name

    def __eq__(self, industry):
        return self.code == industry.code

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'index_code': self.index_code,
            'children': list(map(lambda x: x.to_dict(), self.children))
        }


def main():
    """把文件里面的csv格式转变成嵌套的json格式"""
    result = []
    reader = csv.DictReader(open(file_name), delimiter=' ')
    print(reader.fieldnames)
    industry_list = list(map(
        lambda x: Industry(name=x['name'], code=x['code'], index_code=x['index_code']),
        reader))
    # 添加一级行业
    for index, industry in enumerate(industry_list):
        if industry.code[-4:] == '0000':
            result.append(industry)
    # 添加二级行业
    for index, industry in enumerate(industry_list):
        if industry.code[-4:] != '0000':
            for i in result:
                if i.contains(industry):
                    i.insert(industry)
                    break
            else:
                raise Exception("报错")
    return result


if __name__ == '__main__':
    print("====starts=====")
    for index, i in enumerate(main()):
        pprint.pprint(i.to_dict(), indent=4)
    data = []
    for i in main():
        data.append(i.to_dict())
    with open('result/result.json', 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("===end===")
