class userbadge:
    def __init__(self,userid,badgeid):
        self.userid=userid
        self.badgeid=badgeid
    
    @staticmethod
    def create_userbadge(userid,badgeid):
        userbadgescollection[userid].append(badgeid)
        return userbadge(userid,badgeid)

userbadgescollection=dict()
