# lol_profession_crawl
profession player's game data crawl and analyze in League of Legends.
League of Legends 职业选手（韩服）游戏记录爬虫和分析。

根据数据随缘更新一些发现和有趣的点。尝试在S8把RNG奶爆。


## 来源 Data-origin

[op.gg](http://www.op.gg/)

每个ID每次取最近200场游戏，对该游戏场次数据提取。


## 使用 Usage

### Crawl

```python
# spider/
scrapy crawl matchlist -a username=[选手id]
```

### Analyze

## 发现 Discovery

1. Faker 最近有15场狂玩彗星剑魔中单（未计算补位和换位），胜率53%(8/7)