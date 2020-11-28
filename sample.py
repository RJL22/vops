import options

tickerSymbol = 'AMZN'
contractName = 'AMZN201204C01800000'


# optionObj = options.scrapePutOptions(tickerSymbol)
optionObj = options.scrapeCallOptions(tickerSymbol)
print(optionObj.getChain())

# options.graphLongPut(optionObj, contractName)
# #options.graphShortPut(optionObj, contractName)
# options.graphLongCall(optionObj, contractName)
# # options.graphShortCall(optionObj, contractName)
options.graphCalls(optionObj, contractName)

