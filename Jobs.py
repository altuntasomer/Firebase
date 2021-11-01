from datetime import datetime
from datetime import timedelta
class Jobs():

    def __init__(self, info):
        self.info = info
        self.start_time = self.calculate_start_time()

    def calculate_start_time(self):
        end_date = datetime.strptime(self.info["date"], "%d.%m.%Y,%H:%M")
        try:
            time = int(self.info["time"])
            return(end_date, end_date - timedelta(minutes=time))
        except:
            time = 0
            return(end_date,end_date)


