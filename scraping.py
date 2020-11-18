#Python modules
import requests
import bs4
import pandas as pd
import numpy

#Local imports
import option_container


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

	date = webpage.select('section > section > div > span', {'datareactid':'47'})[2].text

	#Scrape data
	tables = webpage.select('table', attrs={'datareactid':'50'})

	callTable = tables[0]
	putTable = tables[1]

	columns = callTable.find('thead').findAll('th')
	columnNames = [c.text for c in columns]


	rows = callTable.find('tbody').findAll('tr')
	optionMatrix = []

	for row in rows:
		tds = row.findAll('td')
		option = [td.get_text() for td in tds]
		optionMatrix.append(option)

	df = pd.DataFrame(optionMatrix, columns=columnNames)

	optionObj = option_container.OptionObj(df, date)

	return optionObj

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

	optionObj = option_container.OptionObj(df, date)

	return optionObj

