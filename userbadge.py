class userbadge:
    def __init__(self,userid,badgeid):
        self.userid=userid
        self.badgeid=badgeid
        userbadgescollection.setdefault(userid,[]).append(badgeid)
    
    @staticmethod
    def add_userbadge(userid,badgeid):
        return userbadge(userid,badgeid)
    
    @staticmethod
    def list_userbadges_by_userid(userid):
        return userbadgescollection.get(userid,[])
    
userbadgescollection=dict()
