import scrapy
from web_scrape.items import ActorItem


# response.xpath('//table[@class="infobox biography vcard"]/tr/td/span[contains(text(),"age")]').extract()

# response.xpath('//span[@class="noprint ForceAgeToShow"]/text()').extract_first()

# https://en.wikipedia.org/wiki/List_of_action_film_actors

# https://en.wikipedia.org/wiki/Category:American_martial_arts_films
class ActorSpider(scrapy.Spider):
    name = "actor"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_action_film_actors"
    ]

    '''
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Morgan_Freeman'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''

    def parse(self, response):
        # divs = response.xpath('//div[@id="mw-content-text"]')
        for sel in response.xpath('//div[@class="div-col columns column-count column-count-3"]/ul/li'):
            url = sel.xpath('a/@href').extract_first()
            url = response.urljoin(url)
            #yield scrapy.Request(url, self.parse)
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        if response.xpath('//table[@class="infobox biography vcard"]') != [] or response.xpath('//table[@class="infobox vcard plainlist"]') != []:
            if response.xpath('//table[@class="infobox biography vcard"]') != []:
                table = response.xpath('//table[@class="infobox biography vcard"]')
            else:
                table = response.xpath('//table[@class="infobox vcard plainlist"]')
            if table.xpath('//tr/td/span[@class="noprint ForceAgeToShow"]') != []:
                actor_item = ActorItem()
                if response.xpath('//table[@class="infobox biography vcard"]') != []:
                    actor_item['actorName'] = table.xpath('//tr/th/span/text()')[0].extract()
                else:
                    actor_item['actorName'] = table.xpath('//tr/th/text()')[0].extract()
                actor_item['actorAge'] = table.xpath('//tr/td/span[@class="noprint ForceAgeToShow"]/text()')[0].extract()
                yield actor_item
