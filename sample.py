import options

tickerSymbol = 'AMZN'
contractName = 'AMZN201127C01880000'


# optionObj = options.scrapePutOptions(tickerSymbol)
optionObj = options.scrapeCallOptions(tickerSymbol)


# # options.graphLongPut(optionObj, contractName)
# #options.graphShortPut(optionObj, contractName)
# # options.graphLongCall(optionObj, contractName)
# # options.graphShortCall(optionObj, contractName)
options.graphCalls(optionObj, contractName)

