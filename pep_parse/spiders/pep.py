import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section = response.css('section[id="numerical-index"]')
        links = section.css('a[href^="/pep"]')
        for pep_link in links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        for pep in response.css('section[id="pep-content"]'):
            data = {
                'number': pep.css('h1::text').get().split()[1],
                'name': pep.css('h1::text').get().split('– ')[1],
                'status': pep.css('dt:contains("Status") + dd::text').get(),
            }
            yield PepParseItem(data)
