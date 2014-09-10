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
    """Opens a pickled DataFrame to give us db connection.
    """
   
    bikedata = pickle.load(open("bikedata.pkl", "rb"))
    ##jsonbikedata = json.dumps(bikedata.values.tolist(), cls=DateEncoder)

    return bikedata


@app.route('/')
def index():
    #data = getData()
    return render_template('index.html')




@app.route('/next_data')
def getdata():
    # get dataset slice
    bikedata = get_db()
    jsonbikedata = bikedata[1:100000].to_json(date_format="iso", orient="records")
    print "this is working ok!"
    return jsonbikedata


if __name__ == '__main__':
    app.run()
