class community:
    def __init__(self,communityid,name,description,createdby):
        self.communityid=communityid
        self.name=name
        self.description=description
        self.createdby=createdby

    def create_community(communityid,name,description,createdby):
        communitycollection[communityid]=community(communityid,name,description,createdby)
        return community(communityid,name,description,createdby)

communitycollection=dict()