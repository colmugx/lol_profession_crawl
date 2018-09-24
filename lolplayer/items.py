# -*- coding: utf-8 -*-

from scrapy import Field, Item


class LolplayerItem(Item):

    # 队伍信息
    team = Field()
    name = Field()

    # 使用韩服ID
    game_id = Field()

    # 使用英雄
    hero = Field()

    # 赛场位置
    position = Field()

    # 比赛状态
    status = Field()

    # 天赋
    mainRune = Field()
    subRune = Field()

    # KDA
    kill = Field()
    death = Field()
    assist = Field()

    # 时间
    time = Field()

    # 当场数据
    cs = Field()
    mmr = Field()

    # 出装
    equip = Field()

    # 参与选手
    enemyTeam = Field()
    ourTeam = Field()
