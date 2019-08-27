import scrapy
from ..items import CycleCrawlerItem

#creating spider
class MTB_Bicyle_Crawl(scrapy.Spider):
    name = "MTB"          #spider name
    start_urls=[
        'https://www.firefoxbikes.com/bicycles-and-bikes-store/mountain-bikes/'
    ]

    def parse(self , response):
        items = CycleCrawlerItem() #creating instances of the item class

        model = response.css(".above_image a").css("::text").extract(),
        amount = response.css(".price::text").extract(),
        link = response.css(".product-image img::attr(src)").extract()

        items['model'] = model
        items['amount'] = amount
        items['link'] = link

        yield items





