import os
import json
import cPickle as pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import flash
from flask import send_from_directory
from flask import jsonify

# create our little application :)
app = Flask(__name__, static_url_path="/client", static_folder="client")
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    #DATABASE=os.path.join(app.root_path, 'offers.db'),
    #disable DEBUG before production!!
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
# define DASHBOARD_SETTINGS if we want to config file, silent means don't complain
app.config.from_envvar('DASHBOARD_SETTINGS', silent=True)


class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return obj
        return json.JSONEncoder.default(self, obj)

#gets a database connection if one does not already exist
def get_db():
    """Opens a csv to give us db connection.
    """
    bikedata = pd.DataFrame.from_csv("test.csv", index_col=11, header=0,infer_datetime_format=False)
    #print bikedata
    # fix headers
    '''bikedata["startstationid"] = bikedata["start station id"]
    bikedata["startstationname"] = bikedata["start station name"]
    bikedata["startstationlat"] = bikedata["start station latitude"]
    bikedata["startstationlong"] = bikedata["start station longitude"]
    bikedata["endstationid"] = bikedata["end station id"]
    bikedata["endstationname"] = bikedata["end station name"]
    bikedata["endstationlat"] = bikedata["end station latitude"]
    bikedata["endstationlong"] = bikedata["end station longitude"]
    bikedata["birthyear"] = bikedata["birth year"]
    del bikedata["start station id"]
    del bikedata["start station name"]
    del bikedata["start station latitude"]
    del bikedata["start station longitude"]
    del bikedata["end station id"]
    del bikedata["end station name"]
    del bikedata["end station latitude"]
    del bikedata["end station longitude"]
    del bikedata["birth year"]'''
    
    def pdconvert(dte):
        #datestring = pd.datetools.parse(dte).strftime('%Y%m%dT%H:%M%SZ')
        return pd.datetools.parse(dte)


    start = list(bikedata.starttime)
    end = list(bikedata.stoptime)
    bikedata['start'] = map(pdconvert,start)
    bikedata['end'] = map(pdconvert,end)
    del bikedata['starttime']
    del bikedata['stoptime']


    print bikedata

    ##jsonbikedata = json.dumps(bikedata.values.tolist(), cls=DateEncoder)
    jsonbikedata = bikedata.to_json(date_format="iso", orient="records")
    #print jsonbikedata
    return jsonbikedata


@app.route('/')
def index():
    #data = getData()
    return render_template('index.html')




@app.route('/next_data')
def getdata():
    # get dataset slice
    bikedata = get_db()
    print "this is working ok!"
    return bikedata


if __name__ == '__main__':
    app.run()
