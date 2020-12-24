import sys
sys.path.append('../')

from src.vops import scraping
from src.vops import graphing

tickerSymbol = 'TSLA'
contractName = 'TSLA201224P00150000'


optionObj = scraping.scrapePutOptions(tickerSymbol)
# optionObj = scraping.scrapeCallOptions(tickerSymbol)
print(optionObj.getChain())
print(scraping.scrapePrice('TSLA'))

# graphing.graphLongPut(optionObj, contractName)
graphing.graphShortPut(optionObj, contractName)
# graphing.graphLongCall(optionObj, contractName)
# # options.graphShortCall(optionObj, contractName)
# graphing.graphCalls(optionObj, contractName, export = False)