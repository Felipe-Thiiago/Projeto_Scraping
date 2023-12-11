import scrapy


class AdorecinemaSpider(scrapy.Spider):
    name = "adorecinema"
    #allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
