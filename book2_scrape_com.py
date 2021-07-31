from scrapy import Request, Spider


class BookSpider(Spider):
	name = 'books_toscrape_com'
	start_urls = ['http://books.toscrape.com/']

	def parse(self, response):
		books = response.css("ol.row > li")
		for book in books:
			item = dict()
			item['title'] = book.css("h3 > a::attr(title)").get()
			item['product_url'] = book.css("h3 > a::attr(href)").get()
			item['product_url'] = response.urljoin(item['product_url'])
			item['price'] = book.css("p.price_color::text").get()

			yield item
			
			next_url = response.css("li.next > a::attr(href)").get()
			if next_url:
				next_url = response.urljoin(next_url)
				yield Request(next_url, callback=self.parse)

	





		






