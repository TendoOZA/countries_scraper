import scrapy, re
from quotesscraper.items import CountryItem

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    ]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS": 1,
        "FEED_EXPORT_ENCODING": "utf-8",
    }

    def parse(self, response):
        # We find the table that has a header containing the words 'Country' and 'Population'
        target_table = None
        for t in response.xpath('//table[contains(@class,"wikitable")]'):
            headers = [h.xpath('string(.)').get('').strip().lower() for h in t.xpath('.//tr[1]//th')]
            if any('country' in h for h in headers) and any('population' in h for h in headers):
                target_table = t
                header_list = headers
                break

        if target_table is None:
            self.logger.error("Could not find the expected wikitable on the page.")
            return

        # A simple function to find the column index using keywords
        def find_idx(keywords):
            for kw in keywords:
                for i, h in enumerate(header_list):
                    if kw in h:
                        return i
            return None

        country_idx = find_idx(['country', 'country or area'])
        pop_idx     = find_idx(['population', 'population (1 july', 'population (1 july 2023)'])
        cont_idx    = find_idx(['region', 'continent', 'un continental', 'subregion'])

        rows = target_table.xpath('.//tr')[1:]  # Skip the header
        for row in rows:
            tds = row.xpath('./td')
            if not tds:
                continue

            def td_text(idx):
                if idx is None or idx >= len(tds):
                    return None
                return tds[idx].xpath('string(.)').get('').strip()

            country = td_text(country_idx)
            population = td_text(pop_idx)
            continent = td_text(cont_idx)

            # Remove references [1] and footnote markers
            if country:
                country = re.sub(r'\[\w+\]', '', country).strip()
            if population:
                population = re.sub(r'\[.*?\]', '', population).strip()

            if country and population:
                item = CountryItem()
                item['country'] = country
                item['population'] = population
                item['continent'] = continent or ""
                yield item
