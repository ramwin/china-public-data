#### Xiang Wang @ 2018-01-05 10:40:29


# Introduction/简介
Here is some standardized classification data of Shenyin&Wanguo classification data.  
这里是一些格式化的数据。  


# 数据类型
1. 申万 申银万国 申万行业分类 申银万国行业分类  
    * 数据来源: [申银万国官网](http://www.swsindex.com/idx0530.aspx)
2. 中国地理信息编码 中国行政区划 中国行政规划数据
    * 数据来源; [Administrative-divisions-of-China](https://github.com/modood/Administrative-divisions-of-China)
3. 中国行业分类数据
    * ~~数据来源: [中华人民共和国国家统计局](http://www.stats.gov.cn/tjsj/tjbz/201709/t20170929_1539288.html)~~
    * 数据来源: [StandardIndustrialClassificationCodes](https://github.com/EarlYan/StandardIndustrialClassificationCodes)
4. 全国普通高等学校名单
    * 数据来源: [中国人民共和国教育部](http://www.moe.gov.cn/srcsite/A03/moe_634/201706/t20170614_306900.html)
    > 截至2017年5月31日，全国高等学校共计2914所，其中：普通高等学校2631所（含独立学院265所），成人高等学校283所。
    * [原始数据.excel](./全国普通高等学校名单/全国普通高等学校名单.xls)
    * [处理好的json数据](./全国普通高等学校名单/全国普通高等学校名单.json)
    * [处理脚本](./全国普通高等学校名单/全国普通高等学校名单.py)


# 使用,请安装python3
1. [安装python3](https://www.python.org/downloads/)
2. 运行以下代码
```python
python convert.py
```

# 更新
* 2018-01-09 添加了行政区划数据和行业分类数据
* 2018-01-05 把数据导出成嵌套的json格式，方便前端和后端使用。

# TODO
整理出2017年的国民经济行业分类数据

# 版权
本项目采用GPL协议。如果你更改了此项目的代码用于自己的项目，请开源你更改的代码
