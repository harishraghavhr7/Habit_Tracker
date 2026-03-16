class goal:
    def __init__(self,name,userid,goalid,habitid,description,frequency):
        self.userid=userid
        self.habitid=habitid
        self.name=name
        self.goalid=goalid
        self.description=description
        self.frequency=frequency
        goalscollection[goalid]=self
    
def create_goal(name,userid,goalid,habitid,description,frequency):
        return goal(name,userid,goalid,habitid,description,frequency)

goalscollection=dict()


for key in goalscollection:
    print(goalscollection[key].description)