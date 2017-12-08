# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import codecs
import json

class EmailtestPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'admin123', 'newdb', charset='utf8')
        self.cursor = self.conn.cursor()
        print('connect successed')

    def process_item(self, item, spider):
        # insert_sql = """
        #            insert into pxc_product(title,code)
        #                VALUES (%s,%s)
        #            """
        # table = (item["title"],item["code"])
        insert_sql = """
                           insert into protien(name,price,url)
                               VALUES (%s,%s,%s)                
                           """
        table = (item["name"], item["price"], item["url"])
        self.cursor.execute(insert_sql, table)
        self.conn.commit()

class JsonWithEncodeingPipeline(object):
    def __init__(self):
        self.file = codecs.open('restaurant.json','w',encoding = "utf-8")
    def process_item(self,item,spider):
        lines = json.dumps(dict(item),ensure_ascii = False)+"\n"
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()