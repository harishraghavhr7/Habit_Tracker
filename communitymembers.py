class communitymembers:
    def __init__(self,communityid,userid,role,joined_id):
        
        key=(communityid,userid)
        if key in communitymemberscollection:
            raise ValueError("User is already a member of the community")
        
        self.communityid=communityid
        self.userid=userid
        self.role=role
        self.joined_id=joined_id
        communitymemberscollection[key]=self
    
    @staticmethod
    def list_communitymembers_by_communityid(communityid):
        return [member for member in communitymemberscollection.values() if member.communityid==communityid]


    @staticmethod
    def create_communitymembers(communityid,userid,role,joined_id):
        communitymemberscollection[(communityid,userid)]=communitymembers(communityid,userid,role,joined_id)
        return communitymemberscollection[(communityid,userid)]

    @staticmethod    
    def remove_communitymembers(communityid,userid):
        key=(communityid,userid)
        if key in communitymemberscollection:
            del communitymemberscollection[key]
        else:
            raise ValueError("User is not a member of the community")
    

communitymemberscollection=dict()