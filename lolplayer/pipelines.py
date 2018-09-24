# -*- coding: utf-8 -*-
import pymongo


class LolplayerPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('''数据库ip''', 27017)
        # db = client[yourdb]
        self.db = db

    def process_item(self, item, spider):
        post = dict(item)
        name = post.name
        coll = self.db[name]
        coll.insert(post)
        return item
