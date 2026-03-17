class communitypost:
    def __init__(self,postid,communityid,userid,content):
        self.postid=postid
        self.userid=userid
        self.content=content
        self.communityid=communityid
        communitypostscollection.setdefault(communityid,[]).append(self)
        
    @staticmethod
    def create_communitypost(postid,communityid,userid,content):
        return communitypost(postid,communityid,userid,content)
    
    @staticmethod
    def list_communityposts_by_communityid(communityid):
        return communitypostscollection.get(communityid,[])
    
communitypostscollection=dict()