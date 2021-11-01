import types
import Jobs
import pyrebase
import json

firebase_config = {

        "serviceAccount": "serviceAccountKey.json"
    }
firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()
database = firebase.database()
jobs_collection = database.child("Jobs").get().val()

joblist = list()

for i in jobs_collection:
    if type(i) is dict:
        #print(i["date"])
        joblist.append(Jobs.Jobs(i))


