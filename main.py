from flask import Flask
app = Flask(__name__)
import json

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14


	data=open('Options_Outcomes.txt' , 'r').read().split('\n')
	collegeRow=[]
	for i in range(0,len(data)):
		row=data[i]
		row=row.split(';')
		if len(row)>1:
			if row[2]==region:
				if len(area)>0:
					if area in row[4]:
						try:
							p=int(row[1])
							if percentile>=p:
								collegeRow.append(i)
						except:
							collegeRow.append(i)
				else:
					try:
						p=int(row[1])
						if percentile>=p:
							collegeRow.append(i)
					except:
						collegeRow.append(i)
	results=collegeRow
	return json.dumps(results)



if __name__ == '__main__':
  app.run()
