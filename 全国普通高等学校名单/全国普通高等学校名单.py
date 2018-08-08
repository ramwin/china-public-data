#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-08-08 10:43:58


import csv
import json
import re

result = {
    "北京市": [ ],
}

count_dict = {
}
with open('全国普通高等学校名单.csv', 'r') as csvfile:
    for i in range(3):  # 去掉前面3行多余数据
        csvfile.readline()
    fieldnames = ['序号', '学校名称', '学校标识码', '主管部门', '所在地', '办学层次', '备注']
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    for row in reader:
        if row["学校名称"] == "":
            province_name, count = re.match(r'^(.*)（(\d+)所）$', row["序号"]).groups()
            count = int(count)
            count_dict[province_name] = count
            print("当前处理到的省份为: {}".format(province_name))
            print(row)
            result[province_name] = []
        else:
            result[province_name].append(row)

for key, value in count_dict.items():
    assert len(result[key]) == value
with open('全国普通高等学校名单.json', 'w') as f:
    f.write(json.dumps(result, indent=4, ensure_ascii=False))
