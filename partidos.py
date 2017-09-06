# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from itertools import izip
import requests

lista_partidos = {}

class PartidoSpider(scrapy.Spider):
	name = 'partidobot'
	start_urls = ['http://filiaweb.tse.jus.br/filiaweb/portal/relacoesFiliados.xhtml']

	def parse(self, response):
		partidos_selector = '//div[@id="textoConteudo"]/p/select[@id="partido"]/option/text()'
		selectors = iter(response.xpath(partidos_selector).extract())
		lista_partidos = { 'partidos' : dict(izip(selectors, selectors)) }

		yield lista_partidos


