import options


tickerSymbol = 'AMD'
contractName = 'AMD201120C00067500'


optionObj = options.scrapeCallOptions('AMD')
options.graphShortCall(optionObj, 'AMD201120C00067500')
