# import scrapy


# class PostSpider(scrapy.Spider):
#     name = "posts"
#     start_urls = ['https://www.facebook.com/users/login.php']
# 	    for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#     	FormRequest.from_response(response,
#                     formdata={'email': 'ja-roque@hotmail.com', 'pass': 'acmilan18'},
#                     callback=self.after_login)

# //*[@id="email"]