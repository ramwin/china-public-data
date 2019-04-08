#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-10-08 14:42:54


import json


origin_data = json.load(open('中国行政编码数据.json'))

provinces = []
cities = []  # 地级市
countries = []  # 县级市

location_names = set()

for province in origin_data:
    assert province['name'] not in provinces
    assert province['name'] not in location_names
    provinces.append(province['name'])
    location_names.add(province['name'])
    for city in province['childs']:
        if city["name"] in ("市辖区", "省直辖县级行政区划"):  # 四个直辖市都叫市辖区, 有四个省有这个省直辖县级行政区划
            pass
        else:
            assert city["name"] not in cities
            assert city["name"] not in location_names
            cities.append(city["name"])
            location_names.add(city["name"])
        for country in city["childs"]:
            try:
                assert country["name"] not in countries
                assert country["name"] not in location_names
                countries.append(country["name"])
                location_names.add(country["name"])
            except:
                print(country["name"])  # 有几个县级市有重复的。


print("中国的省份有:{}, 共计{}个".format(provinces, len(provinces)))
print("中国的地级市有(不包含省直辖县级行政区划, 市辖区):{}, 共计{}个".format(cities, len(cities)))
