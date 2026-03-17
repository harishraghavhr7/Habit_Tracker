class community:
    def __init__(self,communityid,name,description,createdby):
        self.communityid=communityid
        self.name=name
        self.description=description
        self.createdby=createdby

    @staticmethod
    def create_community(communityid,name,description,createdby):
        communitycollection[communityid]=community(communityid,name,description,createdby)
        return communitycollection[communityid]
    
    @staticmethod
    def get_by_id(communityid):
        return communitycollection.get(communityid)
    
    @staticmethod
    def update_community(communityid,name=None,description=None):
        community=communitycollection.get(communityid)
        if not community:
            raise ValueError("Community not found")
        if name:
            community.name=name
        if description:
            community.description=description
        return community

communitycollection=dict()