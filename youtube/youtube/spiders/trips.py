from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import MySQLdb

class happy_trips(BaseSpider):
    name = 'trips'
    start_urls = ['http://www.happytrips.com/destinations']
    
    def __init__(self, *args, **kwargs):
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd='01491a0237db', db="tripsdb", charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

         
    def parse(self, response):
        sel = Selector(response)
        nodes = sel.xpath('//div[@id="content_wrapper"]')
        for node in nodes:
            image_desc = ''.join(node.xpath('.//div[@class="image"]/a/@href').extract())
            link = ''.join(node.xpath('.//div/h3/a/@href').extract())
           # print (image_desc, link) 
            qry = 'insert into infor(image_desc, link_avail) values (%s, %s )'
            #qry = 'insert into raja (image_desc, link_avail) values ("a","b")'
            values = (image_desc, link)
            self.cur.execute(qry, values)
            self.conn.commit()
