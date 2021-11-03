from datetime import datetime
from datetime import timedelta
class Jobs():

    def __init__(self, info, user):
        self.info = info
        #self.info["start_time"] = self.calculate_start_time()
        self.info["username"] = user



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