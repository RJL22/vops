import sys
sys.path.append('../')

from src.vops import scraping
from src.vops import graphing

tickerSymbol = 'TSLA'
contractName = 'TSLA201224C00020000'


# optionObj = options.scrapePutOptions(tickerSymbol)
optionObj = scraping.scrapeCallOptions(tickerSymbol)
print(optionObj.getChain())

# options.graphLongPut(optionObj, contractName)
# #options.graphShortPut(optionObj, contractName)
# options.graphLongCall(optionObj, contractName)
# # options.graphShortCall(optionObj, contractName)
graphing.graphCalls(optionObj, contractName, export = True)