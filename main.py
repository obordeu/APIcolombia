from flask import Flask
app = Flask(__name__)
from openpyxl import load_workbook

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14
	results=area
	return results



if __name__ == '__main__':
  app.run()
