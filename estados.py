# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from itertools import izip
import requests

lista_uf = {}

class PartidoSpider(scrapy.Spider):
	name = 'partidobot'
	start_urls = ['http://filiaweb.tse.jus.br/filiaweb/portal/relacoesFiliados.xhtml']

	def parse(self, response):
		estados_selector = '//div[@id="textoConteudo"]/p/select[@id="uf"]/option/text()'
		selectors = iter(response.xpath(estados_selector).extract())
		lista_uf = { 'estados' : dict(izip(selectors, selectors)) }

		yield lista_uf