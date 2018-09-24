# -*- coding: utf-8 -*-

from scrapy import Spider, Request
from lolplayer.items import LolplayerItem
import re


class MatchlistSpider(Spider):
    name = 'matchlist'

    def start_requests(self):
        name = self.username or 'wdtt'
        yield Request(
            'http://www.op.gg/summoner/userName=%s' % name,
            callback=self.parse)

    def parse(self, response):
        game_name = response.css(
            '.Profile .Information > .Name::text').extract_first()
        team_name = response.css(
            '.Profile .Information > .Team::text').extract_first().strip()
        team_id = re.findall(
            r'\[(.*)\]',
            response.css('.Profile .Information > .Team .Name::text')
            .extract_first())[0]
        positions = ['上路', '打野', '中单', '下路', '辅助']
        data_list = response.css('.GameItemList .GameItemWrap')
        for match in data_list:
            item = LolplayerItem()
            hero = match.css('.ChampionName a::text').extract_first()
            status = match.css(
                '.GameItem::attr(data-game-result)').extract_first()
            mainRune = match.css(
                '.Rune:nth-child(1) img::attr(alt)').extract_first()
            subRune = match.css(
                '.Rune:nth-child(2) img::attr(alt)').extract_first()
            kill = match.css('.KDA .KDA .Kill::text').extract_first()
            death = match.css('.KDA .KDA .Death::text').extract_first()
            assist = match.css('.KDA .KDA .Assist::text').extract_first()
            time = match.css('.GameLength::text').extract_first()
            cs = match.css('.Stats .CS.tip::text').extract_first()
            mmr = match.css('.Stats .MMR b::text').extract_first()
            items = match.css('.Items .Item img::attr(alt)').extract()
            blueTeam = match.css(
                '.FollowPlayers .Team:nth-child(1) .SummonerName a::text'
            ).extract()
            redTeam = match.css(
                '.FollowPlayers .Team:nth-child(2) .SummonerName a::text'
            ).extract()

            item['game_id'] = game_name
            item['team'] = team_name
            item['name'] = team_id
            item['hero'] = hero
            item['status'] = status
            item['mainRune'] = mainRune
            item['subRune'] = subRune
            item['kill'] = kill
            item['death'] = death
            item['assist'] = assist
            item['time'] = time
            item['cs'] = cs
            item['mmr'] = mmr
            item['equip'] = items
            if (game_name in blueTeam):
                item['ourTeam'] = blueTeam
                item['enemyTeam'] = redTeam
                item['position'] = positions[blueTeam.index(game_name)]
            else:
                item['enemyTeam'] = blueTeam
                item['ourTeam'] = redTeam
                item['position'] = positions[redTeam.index(game_name)]

            yield item
