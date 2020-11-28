#Python modules
from datetime import date
from fpdf import FPDF
import requests
import bs4
import matplotlib.pyplot as plt

#Local imports
import scraping
import option_container
import option_graphs

WIDTH = 210
HEIGHT = 297


def createTitle(pdf, tickerSymbol = 'Stock'):
	pdf.set_font('Arial', '', 24)
	pdf.ln(60)
	pdf.cell(w=0, h=30, txt='General Analysis: ' + tickerSymbol, align='C', ln=2)

	pdf.image('logo.png', (WIDTH / 2) - (WIDTH / 8), HEIGHT / 2, WIDTH / 4)
	pdf.ln((WIDTH / 4))

	pdf.set_font('Arial', '', 15)
	pdf.ln(40)
	pdf.cell(w=0, h=30, txt=str(date.today()), border=0, ln=2, align='C')

def createOverview(pdf, tickerSymbol):
	pdf.set_font('Arial', '', 24)
	pdf.cell(w=0, h=30, txt='Current Price: ' + scraping.getPrice(tickerSymbol), align='C', ln=2)
	pdf.ln(60)



if __name__ == '__main__':
	tickerSymbol = 'AMD';
	# pdf = FPDF()

	# pdf.add_page()
	# createTitle(pdf, tickerSymbol)



	# pdf.add_page()
	# createOverview(pdf, tickerSymbol)

	# pdf.output('analysis.pdf', 'F')
	# scraping.getPrice(tickerSymbol)

	optionObj = scraping.scrapeCallOptions('AMD')

	print(optionObj.getExpiration())

	print(optionObj.getChain())


	# strike = float(optionObj.getChain()['Strike'][71])
	# lp = float(optionObj.getChain()['Last Price'][71])

	# x = [i for i in range(70, 120)]
	# y = [option_graphs.shortCall(i, strike, lp) for i in x]

	# # plt.figure(num='Options Graph', edgecolor='black')
	# plt.style.use('dark_background')

	# plot_title = tickerSymbol
	# plt.title(plot_title)
	# plt.plot(x, y, ':')
	# plt.show()

	option_graphs.graphShortCall(optionObj, 'AMD201120C00050000')

