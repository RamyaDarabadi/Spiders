from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

class youtube_crawl(BaseSpider):
    name = "youtube"
    start_urls= ['https://www.youtube.com/feed/trending']
    def parse(self, response):
        sel = Selector(response)
	video_links = sel.xpath('//a[@id="video-title"]/@href')
	print video_links
	import pdb; pdb.set_trace()
	'''
        page=sel.xpath('//ul[@class="expanded-shelf-content-list has-multiple-items"]').extract()
        movie_content=sel.xpath('//div[@class="yt-lockup-dismissable yt-uix-tile"]').extract()
        image=sel.xpath('//div[@class="yt-lockup-thumbnail contains-addto"]').extract()
        print page
        print movie_content
        print image   
	'''
