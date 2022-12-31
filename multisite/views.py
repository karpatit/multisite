from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from firebase.models import FirebaseConfig
import configparser
import os.path
import json
import pyrebase

###########################################################
#### for a file based config, use the following code...
###########################################################

def get_config():
    # setting the config dictionary for the connection
    config_location = os.path.join(os.path.dirname(__file__), './config.ini')
    config = configparser.ConfigParser()
    # read and get features from config file
    config.read(config_location)
    return config

def firebase_connect(config,site):
    ## reading the values from the config.ini file
    apiKey = config.get(site, 'apiKey')
    authDomain = config.get(site, 'authDomain')
    databaseURL = config.get(site, 'databaseURL')
    storageBucket = config.get(site, 'storageBucket')
    config = {
        "apiKey": apiKey,
        "authDomain": authDomain,
        "databaseURL": databaseURL,
        "storageBucket": storageBucket
    }
    # initialing the connection to the firebase db
    firebase = pyrebase.initialize_app(config)
    # reference to the database
    db = firebase.database()
    return db

#############################################################################
### For a databses-based config (recommended), use the following code...
#############################################################################

def firebase_db(site):
    try:
        fbconfig = FirebaseConfig.objects.filter(site=site)
        config = {
            "apiKey": fbconfig.values_list('apiKey')[0][0],
            "authDomain": fbconfig.values_list('authDomain')[0][0],
            "databaseURL": fbconfig.values_list('databaseURL')[0][0],
            "storageBucket": fbconfig.values_list('storageBucket')[0][0]
        }
        #print(config)
        firebase = pyrebase.initialize_app(config)
        # reference to the database
        db = firebase.database()
    except:
        db = None
    return db

def getDB(request):
    current_site = str(get_current_site(request))
    db = firebase_db(current_site)
    return db

####################################################################
###  Calling the correct config based on the current site url
####################################################################

def showsite(request):
    db = getDB(request)
    if db != None:
        json = db.child('test').child('clinic').get().val()
        return HttpResponse(json)
    else:
        return HttpResponse('site was not reached')
        #return HttpResponse(current_site)

    #return HttpResponse('Failed to show your site...'+current_site)
    return HttpResponse(current_site)
