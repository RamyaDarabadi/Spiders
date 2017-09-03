from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector

class TheHindu(BaseSpider):
	name = 'hindu'
	start_urls = ['http://www.thehindu.com/news/national/']

	def parse(self, response):
		sel = Selector(response)
		news_node_links = sel.xpath('//div[@class="container section-container "]//div[@class="33_1x_OtherStoryCard mobile-padding"]//a[@class="light-gray-color Other-StoryCard-text hidden-xs"]/@href').extract()

		for li in news_node_links:
			yield Request(li, callback=self.parse_news)

	def parse_news(self, response):
		sel = Selector(response)
		title = sel.xpath('//div[@class="article"]/h1[@class="title"]/text()').extract()
		
