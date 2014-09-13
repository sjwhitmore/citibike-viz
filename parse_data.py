import cPickle as pickle
import pandas as pd
import json
import csv

#bikedata = pd.DataFrame.from_csv("2013-07 - Citi Bike trip data.csv", header=0, index_col=False)
    #print bikedata
    
def pdconvert(dte):
#datestring = pd.datetools.parse(dte).strftime('%Y%m%dT%H:%M%SZ')
    return pd.datetools.parse(dte)

csvfile = open("modifiedfeb.csv", 'rU')
jsonfile = open('febdata.json', 'w')

fieldnames = ("tripduration","starttime","stoptime","startstationid","startstationname","startstationlatitude","startstationlongitude","endstationid","endstationname","endstationlatitude","end stationlongitude","bikeid","usertype","birthyear","gender")
reader = csv.DictReader( csvfile, fieldnames)
linenum = 0
for row in reader:
	if linenum != 0:
		json.dump(row, jsonfile)
		jsonfile.write(',')
		linenum != 1
	else:
		linenum += 1


csvfile.close()
jsonfile.close()
with open('febdata.json', 'rb+') as f:
    f.seek(0,2)                 # end of file
    size=f.tell()               # the size...
    f.truncate(size-1)          # truncate at that size - how ever many characters