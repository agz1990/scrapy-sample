'''
Created on 2015-07-07

@author: jigc
'''

import scrapy


class DomzSpider(scrapy.Spider):
    '''
    classdocs
    '''

    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
