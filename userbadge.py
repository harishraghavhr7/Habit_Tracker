from badge import badge
from badge import badgescollection

class userbadge:
    def __init__(self,userid,badgeid):
        self.userid=userid
        self.badgeid=badgeid
        userbadgescollection.setdefault(userid,[]).append(badgeid)
    
    @staticmethod
    def award_badge_to_user(userid,badgeid):
        if badgeid in badgescollection:
            userbadge(userid,badgeid)
        else:
            raise ValueError("Badge not found")
    
    @staticmethod
    def list_userbadges_by_userid(userid):
        return userbadgescollection.get(userid,[])
    
userbadgescollection=dict()
