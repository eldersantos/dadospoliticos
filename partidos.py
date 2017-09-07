# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from itertools import izip
import requests
import json

lista_partidos = {}

class Partido(scrapy.Item):
    partido = scrapy.Field(serializer=str)

class PartidoSpider(scrapy.Spider):
	name = 'partidobot'
	start_urls = ['http://filiaweb.tse.jus.br/filiaweb/portal/relacoesFiliados.xhtml']

	def parse(self, response):
		partidos_selector = '//div[@id="textoConteudo"]/p/select[@id="partido"]/option/text()'
		for par in response.xpath(partidos_selector).extract():
			yield {'partido' : par}



