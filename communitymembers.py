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

    def create_communitymembers(communityid,userid,role,joined_id):
        communitymemberscollection[(communityid,userid)]=communitymembers(communityid,userid,role,joined_id)
        return communitymembers(communityid,userid,role,joined_id)

communitymemberscollection=dict()