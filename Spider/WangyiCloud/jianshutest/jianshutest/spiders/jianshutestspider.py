from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from jianshutest.items import JianshutestItem

class jianshutest(CrawlSpider):
    name = 'jianshutest'
    start_urls = ['https://www.jianshu.com/c/fcd7a62be697?order_by=top&page=1']

    def parse(self, response):
        item = JianshutestItem()
        selector = Selector(response)
        infos = selector.xpath('//ul[@class="flow-list-ul"]/li')
        
        
        for info in infos:
            title = info.xpath('a/div/h6/text()').extract()[0]
            name = info.xpath('div/span[1]/text()').extract()[0]
            comment = info.xpath('div/span[2]/text()').extract()[0].strip()
            like = info.xpath('div/span[3]/text()').extract()[0].strip()
            gain = info.xpath('div/span[4]/text()').extract()

            if gain:
                gain = gain[0].strip()
            else:
                gain = '0'
        
            item['title'] = title 
            item['name'] =  name
            item['comment'] =  comment
            item['like'] =  like
            item['gain'] =  gain
        
            yield item

        urls = ['https://www.jianshu.com/c/fcd7a62be697?order_by=top&page={}'.format(str(i)) for i in range(2,21)]
        for url in urls:
            yield Request(url,callback=self.parse)
