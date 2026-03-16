from habit import create_habit
from goal import create_goal
from goal import goalscollection

class users:
    def __init__(self,userid,username,email,password):
        self.userid=userid
        self.username=username
        self.email=email
        self.password=password
        userscollection[userid]=self
    
    @staticmethod
    def create_user(userid,username,email,password):
        return users(userid,username,email,password)
    
    def create_habit(self,habitid,habitname):
        return create_habit(self.userid,habitid,habitname)
    

userscollection=dict()
u1=users.create_user(1,"john","hpp","111")
h1=u1.create_habit(1,"Jumping")
g1=create_goal("lose weight",u1.userid,1,h1.habitid,"lose 5 kg in 2 months","weekly")
#    def __init__(self,name,userid,goalid,habitid,description,frequency):
g2=create_goal("lose weight",u1.userid,2,h1.habitid,"lose 5 kg in 3 months","weekly")

for key in goalscollection:
    print(goalscollection[key].description)
