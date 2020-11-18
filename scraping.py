#Python modules
import requests
import bs4
import pandas as pd
import numpy


class OptionObj:

	def __init__(self):
		self.chain = None
		self.expiration = None

	def __init__(self, a_chain, a_expiration):
		self.chain = a_chain
		self.expiration = a_expiration

	def getExpiration(self):
		return self.expiration

	def getChain(self):
		return self.chain


def scrapePrice(tickerSymbol):
	r = requests.get('https://finance.yahoo.com/quote/' + tickerSymbol)
	soup = bs4.BeautifulSoup(r.text, 'lxml')
	price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find('span').text

	print(soup.find('div', {'class':'D(ib) Mend(20px)'}).find('span'))

	return price

def scrapeOptionStrike(tickerSymbol):
	r = requests.get('https://finance.yahoo.com/quote/' + tickerSymbol + 'A/options?p=' + tickerSymbol) 
	soup = bs4.BeautifulSoup(r.content, features='lxml')

	print(soup.prettify())

	# bid = soup.find('div', {'class':'wrap-meta-item'})

	bid = soup.findAll('t', {'id':'summary-bid'})

	print(bid)

	return 0


def scrapeCallOptions(tickerSymbol):
	#Load the webpage content
	url = 'https://finance.yahoo.com/quote/' + tickerSymbol + '/options?p=' + tickerSymbol
	r = requests.get(url) 

	#Convert to bs object
	webpage = bs4.BeautifulSoup(r.content, features='lxml')

	#Scrape data
	tables = webpage.select('table', attrs={'datareactid':'50'})

	callTable = tables[0]
	putTable = tables[1]

	columns = callTable.find('thead').findAll('th')
	columnNames = [c.text for c in columns]


	trs = callTable.find('tbody').findAll('tr')
	optionMatrix = []

	for tr in trs:
		tds = tr.findAll('td')
		row = [td.get_text() for td in tds]
		optionMatrix.append(row)

	df = pd.DataFrame(optionMatrix, columns=columnNames)

	return df

def scrapePutOptions(tickerSymbol):
	#load the webpage content
	url = 'https://finance.yahoo.com/quote/' + tickerSymbol + '/options?p=' + tickerSymbol
	r = requests.get(url)

	webpage = bs4.BeautifulSoup(r.content, features='lxml')

	date = webpage.select('section > section > div > span', {'datareactid':'47'})[2].text

	tables = webpage.select("table", attrs={'datareactid':'50'})

	putTable = tables[1]

	columns = putTable.find('thead').findAll('th')
	columnNames = [c.get_text() for c in columns]

	rows = putTable.find('tbody').findAll('tr')
	optionMatrix = []

	for row in rows:
		tds = row.findAll('td')
		option = [td.get_text() for td in tds]
		optionMatrix.append(option)

	df = pd.DataFrame(optionMatrix, columns=columnNames)

	optionObj = OptionObj(df, date)

	return optionObj

