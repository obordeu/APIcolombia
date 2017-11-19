from flask import Flask
app = Flask(__name__)
from openpyxl import load_workbook

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14
	ws=loadData()
	results=len(ws['a'])
	return results


def loadData():
	wb = load_workbook('Options_Outcomes.xlsx')
	ws = wb.get_sheet_by_name('Sheet1')
	return ws


if __name__ == '__main__':
  app.run()
