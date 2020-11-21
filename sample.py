import options


tickerSymbol = 'AMZN'
contractName = 'AMZN201127C01860000'


optionObj = options.scrapeCallOptions(tickerSymbol)
options.graphLongCall(optionObj, contractName)
