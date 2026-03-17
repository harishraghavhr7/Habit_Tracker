from users import userscollection

class badge:
    def __init__(self,admin_userid,badgeid,name,description,criteria_tyepe,criteria_value):
        self.admin_userid=admin_userid
        self.badgeid=badgeid
        self.name=name
        self.description=description
        self.criteria_type=criteria_tyepe
        self.criteria_value=criteria_value

    @staticmethod
    def create_badge_by_admin(admin_userid,badgeid,name,description,criteria_tyepe,criteria_value):
        if userscollection.get(admin_userid) and userscollection[admin_userid].is_admin:
            badgescollection[badgeid]=badge(admin_userid,badgeid,name,description,criteria_tyepe,criteria_value)
            return badgescollection[badgeid]
        else:
            raise ValueError("Admin user not found or user is not an admin")
    
    @staticmethod
    def get_badge_by_id(badgeid):
        return badgescollection.get(badgeid)
    
    @staticmethod
    def list_badges():
        return list(badgescollection.values())
    
badgescollection=dict()
