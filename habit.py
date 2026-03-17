from datetime import date
from math import ceil

class habit:
    def __init__(self,userid,habitid,habitname):
        self.userid=userid
        self.habitid=habitid
        self.habitname=habitname
        self.startdate=date.today()
        habitscollection[habitid]=self

    @staticmethod
    def get_by_id(habitid):
        return habitscollection.get(habitid)
    
    @staticmethod
    def list_habits_by_userid(userid):
        return [habit for habit in habitscollection.values() if habit.userid == userid]
    
    

        
        
        

habitscollection=dict()
def create_habit(userid,habitid,habitname):
    habitscollection[habitid]=habit(userid,habitid,habitname)
    return habitscollection[habitid]
