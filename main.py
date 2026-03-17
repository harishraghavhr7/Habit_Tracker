from users import users
from habit import create_habit
from goal import create_goal
from goal import goalscollection
from goal import goal


u1=users.create_user(1,"john","hpp","111")
h1=u1.create_habit(1,"Jumping")
g1=create_goal("lose weight",u1.userid,1,h1.habitid,"lose 5 kg in 2 months","weekly")
#    def __init__(self,name,userid,goalid,habitid,description,frequency):
g2=create_goal("lose weight",u1.userid,2,h1.habitid,"lose 5 kg in 3 months","weekly")

g1.mark_done()
g1.mark_done()

print(g1.get_progress())