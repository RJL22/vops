import options


tickerSymbol = 'AMD'


optionObj = options.scrapeCallOptions('AMD')

print(optionObj.getChain())

# print(optionObj.getAttr('AMD201204C00099000', 'Strike'))
# print(optionObj.getAttr('AMD201204C00099000', 'Last Price'))


options.graphShortCall(optionObj, 'AMD201120C00067500')
