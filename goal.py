from math import ceil
from datetime import date
from badge import badgescollection
from goal import goalscollection
from userbadge import userbadge
class goal:
    def __init__(self,name,userid,goalid,habitid,description,frequency):
        self.userid=userid
        self.habitid=habitid
        self.name=name
        self.goalid=goalid
        self.description=description
        self.frequency=frequency
        self.completed_dates=set()
        self.startdate=date.today()
        goalscollection[goalid]=self


    @staticmethod
    def get_by_id(goalid):
        return goalscollection.get(goalid)
    

    @staticmethod
    def list_goals_by_userid(userid):
        return [goal for goal in goalscollection.values() if goal.userid == userid]
    
    @staticmethod
    def update_goal(goalid,name=None,description=None,frequency=None):
        goal=goalscollection.get(goalid)
        if not goal:
            raise ValueError("Goal not found")
        if name:
            goal.name=name
        if description:
            goal.description=description
        if frequency:
            goal.frequency=frequency
        return goal
    
    @staticmethod
    def delete_goal(goalid):
        if goalid in goalscollection:
            del goalscollection[goalid]
        else:
            raise ValueError("Goal not found")
        
    def mark_done(self,done_date=None):
        if not done_date:
            done_date=date.today()
        self.completed_dates.add(done_date)
        self.evaluate_and_award_badge()


    def unmark_done(self,done_date=None):
        if not done_date:
            done_date=date.today()
        self.completed_dates.discard(done_date)

    def get_progress(self):
        linked_goal=self

        days_elapsed=(date.today()-linked_goal.startdate).days+1

        if days_elapsed<1:
            days_elapsed=1
        
        if self.frequency=="daily":
            expected=days_elapsed
        
        elif self.frequency=="weekly":
            expected=ceil(days_elapsed/7)

        elif self.frequency=="monthly":
            expected=ceil(days_elapsed/30)
        else:
            expected=1
            
        completed=len(linked_goal.completed_dates)
        progress=(completed/expected)*100 if expected>0 else 0
        return {
            "habitid":self.habitid,
            "goalid":self.goalid,
            "completed":completed,
            "expected":expected,
            "progress_percentage":progress
        }

        
    
    def evaluate_and_award_badge(self):
        awareded_badges=[]
        existing_badges=userbadge.list_userbadges_by_userid(self.userid)
        progress_data=self.get_progress()
        progress_percentage=progress_data["progress_percentage"]
        completed=progress_data["completed"]

        for badgeid,current_badge in badgescollection.items():
            if badgeid in existing_badges:
                continue
            if current_badge.criteria_type=="progress_percentage":
                if progress_percentage >= current_badge.criteria_value:
                    userbadge.award_badge_to_user(self.userid,badgeid)
                    awareded_badges.append(badgeid)
            elif current_badge.criteria_type=="completed_count":
                if completed >= current_badge.criteria_value:
                    userbadge.award_badge_to_user(self.userid,badgeid)
                    awareded_badges.append(badgeid)
            
        return awareded_badges
        
        
    
def create_goal(name,userid,goalid,habitid,description,frequency):
        goalscollection[goalid]=goal(name,userid,goalid,habitid,description,frequency)
        return goalscollection[goalid]


goalscollection=dict()


