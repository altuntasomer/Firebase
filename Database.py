import pyrebase
from pathlib import Path
from os.path import exists
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

    def downloadImage(self, path):
        Path(path).mkdir(parents=True, exist_ok=True)

        for i in range(0,4):
            try:
                pathT = path + "/" + str(i) + ".jpg"
                print(pathT)
                if not exists(pathT):
                    print("indirdi")
                    self.storage.child(pathT).download(pathT)

            except Exception as e:
                print(e)

    def getAllFilePaths(self, child):
        return self.storage.child(child).list_files()

    def downloadAllImages(self):
        pass
