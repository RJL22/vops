import matplotlib.pyplot as plt

#Inputs: x = stock price, strike = strike price, p = premium
#Output: Net Profit or Loss

def longCall(x, strike, p):
	if x < strike:
		return -p
	elif x >= strike:
		return x - strike - p
	else:
		return None

def shortCall(x, strike, p):
	if x < strike:
		return p
	elif x >= strike:
		return p - (x - strike)
	else:
		return None

def longPut(x, strike, p):
	if x < strike:
		return strike - x - p
	elif x >= strike:
		return -p


def shortPut(x, strike, p):
	if x < strike:
		return -p + (x - strike)
	elif x >= strike:
		return p

def graphLongCall(optionObj, contractName):
	x = [i for i in range(0, 150)]
	y = [longCall(i, optionObj.getAttr(contractName, 'Strike'), optionObj.getAttr(contractName, 'Last Price')) for i in x]

	# plt.figure(num='Options Graph', edgecolor='black')
	plt.style.use('dark_background')

	plot_title = contractName
	plt.title(plot_title)
	plt.plot(x, y, ':')
	plt.show()

def graphShortCall(optionObj, contractName):
	x = [i for i in range(0, 150)]
	y = [shortCall(i, float(optionObj.getAttr(contractName, 'Strike')), float(optionObj.getAttr(contractName, 'Last Price'))) for i in x]

	# plt.figure(num='Options Graph', edgecolor='black')
	plt.style.use('dark_background')

	plot_title = contractName
	plt.title(plot_title)
	plt.plot(x, y, ':')
	plt.show()

def graphLongPut(optionObj, contractName):
	x = [i for i in range(0, 150)]
	y = [longPut(i, optionObj.getAttr(contractName, 'Strike'), optionObj.getAttr(contractName, 'Last Price')) for i in x]

	# plt.figure(num='Options Graph', edgecolor='black')
	plt.style.use('dark_background')

	plot_title = contractName
	plt.title(plot_title)
	plt.plot(x, y, ':')
	plt.show()

def graphShortPut(optionObj, contractName):
	x = [i for i in range(0, 150)]
	y = [shortPut(i, optionObj.getAttr(contractName, 'Strike'), optionObj.getAttr(contractName, 'Last Price')) for i in x]

	# plt.figure(num='Options Graph', edgecolor='black')
	plt.style.use('dark_background')

	plot_title = contractName
	plt.title(plot_title)
	plt.plot(x, y, ':')
	plt.show()