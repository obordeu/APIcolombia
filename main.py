from flask import Flask
app = Flask(__name__)

@app.route('/')
def menuMaker():
	region='ANTIOQUIA'
	area='BELLAS ARTES'
	percentile=14
	wb=loadData()
	for i in range(2, len(ws['a'])):
        if (ws.cell(row=i, column=3).value) == region:  #RegionCheck
            if area in (ws.cell(row=i, column=5).value):    #AreaCheck
                try:    #IMPORTANT NOTE: This code disregards the percentiles; many of them are missing in Options_Outcomes
                    if percentile >= (ws.cell(row=i, column=2).value): collegeRow.append(i)
                except TypeError: collegeRow.append(i)

    s, t, a = [], len(collegeRow), 0

    r = len(collegeRow) if len(collegeRow) < 6 else 6
    while a != r:
        p = randint(0, t) - 2
        print (p)
        try:
            s.append(collegeRow.pop(p))
            a += 1
        except: a = a
    for e in s:
        results[r] = (ws.cell(row=e, column=6).value), (ws.cell(row=e, column=7).value), str((ws.cell(row=e, column=8).value))
        r -= 1
    return results


def loadData():
    wb = load_workbook('Options_Outcomes.xlsx')
    ws = wb.get_sheet_by_name('Sheet1')
    return ws


if __name__ == '__main__':
  app.run()
