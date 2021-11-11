from datetime import datetime
from datetime import timedelta

class Jobs():

    def __init__(self, info, user, campus):
        self.info = info
        self.info["start_time"] = self.calculate_start_time()
        self.info["username"] = user
        self.info["campus"] = campus



    def calculate_start_time(self):
        end_date = datetime.strptime(self.info["date"], "%d.%m.%Y,%H:%M")
        try:
            time = int(self.info["time"])
            return(end_date - timedelta(minutes=time)).strftime("%d.%m.%Y,%H:%M")
        except:
            time = 0
            return(end_date.strftime("%d.%m.%Y,%H:%M"))


    def get_info(self):
        return self.info

    def get_single_info(self, field):
        return self.info[field]

    def get_filepath(self, mode):
        if mode == 'r':
            local_path = self.info["username"] + "/" + self.info["id"]
        elif mode == 'f':
            local_path = "is/" + self.info["id"]

        return local_path

    def report(self):
        mark = "X"
        csut = ""
        ckuc = ""
        if self.info["campus"] == "S":
            csut = mark
        else:
            ckuc = mark
        contex = {
            'p': self.info["username"],
            'time': self.info["time"],
            'description': self.info["description"],
            'date': self.info["start_time"],
            'mark': mark,
            'cS': csut,
            'cK': ckuc,
            'place': self.info["place"]
        }
        return contex