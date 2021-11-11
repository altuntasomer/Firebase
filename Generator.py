class Generator():

    def __init__(self, info):
        self.info = info

    def get_info(self):
        return self.info

    def get_single_info(self,field):
        return self.info[field]

    def report(self):
        pass