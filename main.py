from flask import Flask
app = Flask(__name__)

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14
	try:
		data=open('Options_Outcomes.txt' , 'r').read().split('\n')
		results=data[0]
	except: results="NO FUNCIONA EL EXCEL"
	
	return results



if __name__ == '__main__':
  app.run()
