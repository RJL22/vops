class OptionObj:
	def __init__(self):
		self.chain = None
		self.expiration = None

	def __init__(self, a_chain, a_expiration):
		self.chain = a_chain
		self.expiration = a_expiration

	def getExpiration(self):
		return self.expiration

	def getChain(self):
		return self.chain

	def getAttr(self, contractName, attr):
		colNum = self.chain.columns.get_loc(attr)
		print("Contract name: " + contractName)
		row = self.chain.loc[self.chain['Contract Name'] == contractName]
		# print("----------------------------")
		# print(row)
		# print("----------------------------")
		return row.iloc[0, colNum].replace(',', '')
