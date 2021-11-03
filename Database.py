import pyrebase

class Database():

    def __init__(self, config):

        self.firebase = pyrebase.initialize_app(config)
        self.storage = self.firebase.storage()
        self.database = self.firebase.database()

    def getAllFiles(self):
        pass

    def getAllData(self):
        return self.database.get().val()

    def getChildData(self, child):
        return self.database.child(child).get().val()
