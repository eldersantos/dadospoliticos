#!/usr/bin/python

import json
import requests


def load_partidos():
	with open('partidos.json') as json_data:
		file = json.load(json_data)

	return file

def load_estados():
	with open('estados.json') as json_data:
		file = json.load(json_data)

	return file


def download_file():
	partidos = load_partidos()
	estados = load_estados()

	url = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/'

	for uf in estados:
		for partido in partidos:
			partido['partido'] = partido['partido'].replace(' ', '_')
			url = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf'
			url = url + '/filiados_'+ partido['partido'].lower() +'_'+ uf['estado'].lower() +'.zip'

			r = requests.get(url)

			with open('data/' + uf['estado'].lower() + '_' + partido['partido'].lower() + '.zip', 'wb') as fd:
				fd.write(r.content)


if __name__ == "__main__":
	download_file()
