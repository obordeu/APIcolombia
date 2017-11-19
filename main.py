from flask import Flask
app = Flask(__name__)

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14
	wb=loadData()
	results="HEY"
	return results


def loadData():
	wb = load_workbook('Options_Outcomes.xlsx')
	ws = wb.get_sheet_by_name('Sheet1')
	return ws


if __name__ == '__main__':
  app.run()
