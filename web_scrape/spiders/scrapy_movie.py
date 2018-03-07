import scrapy
from web_scrape.items import MovieItem

#response.xpath('//table[@class="infobox biography vcard"]/tr/td/span[contains(text(),"age")]').extract()

#response.xpath('//span[@class="noprint ForceAgeToShow"]/text()').extract_first()

#https://en.wikipedia.org/wiki/List_of_action_film_actors

#https://en.wikipedia.org/wiki/Category:American_martial_arts_films
class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Category:American_action_comedy_films"
    ]

    def parse(self, response):
        for character in response.xpath('//div[@class="mw-category"]/div'):
            for name in character.xpath('ul/li'):
                url = name.xpath('a/@href').extract_first()
                url = response.urljoin(url)
                yield scrapy.Request(url, self.parse_content)

    def parse_content(self, response):
        table = response.xpath('//table[@class="infobox vevent"]')
        if table.xpath('//tr/th[contains(text(), "Box office")]') != []:
            movie_item = MovieItem()
            movie_item['movieName'] = table.xpath('//tr/th/text()')[0].extract()
            #movie_grossing['movieGrossing'] = table.xpath('//tr/th[contains(text(), "Box office")]')
            movie_item['movieGrossing'] = table.xpath('//tr/th[contains(text(), "Box office")]/ancestor::tr/td/text()').extract_first()
            if table.xpath('//tr/th[contains(text(), "Starring")]/ancestor::tr/td/div/ul/li//text()').extract() != []:
                movie_item['movieStaring'] = table.xpath('//tr/th[contains(text(), "Starring")]/ancestor::tr/td/div/ul/li//text()').extract()
                #movie_item['movieYear'] = table.xpath('//tr/th/div[contains(text(), "Release date")]/ancestor::tr/td/div/ul/li/text()').extract()
            else:
                movie_item['movieStaring'] = table.xpath('//tr/th[contains(text(), "Starring")]/ancestor::tr/td/a//text()').extract()
                #movie_item['movieYear'] = table.xpath('//tr/th[contains(text(), "Release date")]/ancestor::tr/td/a//text()').extract()
            if table.xpath('//tr/th/div[contains(text(), "Release date")]/ancestor::tr/td/div/ul/li/text()').extract() != []:
                movie_item['movieYear'] = table.xpath('//tr/th/div[contains(text(), "Release date")]/ancestor::tr/td/div/ul/li/text()').extract_first()
            else:
                movie_item['movieYear'] = table.xpath('//tr/th/div[contains(text(), "Release date")]/ancestor::tr/td/text()').extract_first()
            yield movie_item