from flask import Flask
app = Flask(__name__)

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14
	results="HEY"
	return results





if __name__ == '__main__':
  app.run()
