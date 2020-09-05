import scrapy
import requests
import random


class ZoominfoSpider(scrapy.Spider):
    name = 'zoominfo'

    def __init__(self, *args, **kwargs):
        super(ZoominfoSpider, self).__init__(*args, **kwargs)
        r = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt')
        self.proxy_pool = r.text.split('\n')
        print(self.proxy_pool)

    def set_proxy(self, request):
        if self.proxy_pool:
            request.meta['proxy'] = random.choice(self.proxy_pool)
        return request

    def start_requests(self):
        with open("input.csv", 'r') as input_file:
            for company_name in input_file:
                company = company_name.strip()
                url = f"https://www.google.com.ua/search?q={company + '+zoominfo+overview'}"
                req = scrapy.Request(url=url, callback=self.parse_google_results, cb_kwargs={"company": company})
                yield self.set_proxy(req)

    def parse_google_results(self, response, **kwargs):
        all_links = response.css("a::attr(href)").getall()
        zoomlinks = [link for link in all_links if "www.zoominfo.com/c/" in link]
        req = scrapy.Request(url=zoomlinks[0], callback=self.parse, cb_kwargs=kwargs)
        yield self.set_proxy(req)

    def parse(self, response, **kwargs):
        yield {
            'company': kwargs['company'],
            'headquarters': response.xpath("//h3[text()='Headquarters:']/following-sibling::div/span/text()").get(),
            'phone': response.xpath("//h3[text()='Phone:']/following-sibling::div/span/text()").get(),
            'revenue': response.xpath("//h3[text()='Revenue:']/following-sibling::div/span/text()").get(),
            'employees_num': response.xpath("//h3[text()='Employees:']/following-sibling::div/span/text()").get(),
            'website': response.xpath("//h3[text()='Website:']/following-sibling::a/text()").get()
        }
