from db.mongo import *
import requests
import json
import os
from bson import ObjectId


class Logic():

    def __init__(self, db):
        self.db = db
	    
    def switch(self, message):
        pass
