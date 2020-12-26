import sys
sys.path.append('../')

from src.vops import scraping
from src.vops import graphing

tickerSymbol = 'AMD'
contractName = 'AMD201231C00060000'


# optionObj = scraping.scrapePutOptions(tickerSymbol)
optionObj = scraping.scrapeCallOptions(tickerSymbol)


# graphing.graphLongPut(optionObj, contractName)
# graphing.graphShortPut(optionObj, contractName)
# graphing.graphLongCall(optionObj, contractName)
# graphing.graphShortCall(optionObj, contractName)
graphing.graphCalls(optionObj, contractName, export = True)