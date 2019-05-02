# -*- coding: utf-8 -*-
import scrapy


class ApartmentScraperSpider(scrapy.Spider):
    name = 'apartment_scraper'
    allowed_domains = ['http://asuntojen.hintatiedot.fi']
    start_urls = []
    for i in range(1, 27):
        start_urls.append(f'http://asuntojen.hintatiedot.fi/haku/?c=Tampere&cr=1&h=1&t=3&l=0&z={i}&search=1&sf=0&so=a&submit=seuraava+sivu+%C2%BB')

    def parse(self, response):

        for row in response.xpath("//table[@id='mainTable']/tbody[3]/tr"):
            if len(row.xpath("td[@class='neighborhood']//text()").extract()) == 0:
                continue

            try:
                trade = {
                    "Kaupunginosa": row.xpath("td[1]//text()").extract(),
                    "Huoneisto": row.xpath("td[2]//text()").extract(),
                    "Talotyyppi": row.xpath("td[3]//text()").extract(),
                    "Neliömäärä": row.xpath("td[4]//text()").extract(),
                    "Velaton hinta": row.xpath("td[5]//text()").extract(),
                    "Euroa per neliö": row.xpath("td[6]//text()").extract(),
                    "Rakennusvuosi": row.xpath("td[7]//text()").extract(),
                    "Kerros": row.xpath("td[8]//text()").extract(),
                    "Hissi": row.xpath("td[9]//text()").extract(),
                    "Kunto": row.xpath("td[10]//text()").extract(),
                    "Energialuokka": row.xpath("td[11]//text()").extract()
                }

            except:
                pass

            yield trade

        #self.n += 1
        #next_page_url = f'http://asuntojen.hintatiedot.fi/haku/?c=Tampere&cr=1&h=1&t=3&l=0&z={self.n}&search=1&sf=0&so=a&submit=seuraava+sivu+%C2%BB'
        #yield response.follow(next_page_url, self.parse)
