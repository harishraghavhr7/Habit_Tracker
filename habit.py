from datetime import date
class habit:
    def __init__(self,userid,habitid,habitname):
        self.userid=userid
        self.habitid=habitid
        self.habitname=habitname
        self.startdate=date.today()
        habitscollection[habitid]=self

habitscollection=dict()
def create_habit(userid,habitid,habitname):
    return habit(userid,habitid,habitname)

