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


# 使用,请安装python3
1. [安装python3](https://www.python.org/downloads/)
2. 运行以下代码
```python
python convert.py
```

# 更新
2018-01-09 添加了行政区划数据和行业分类数据
2018-01-05 把数据导出成嵌套的json格式，方便前端和后端使用。
