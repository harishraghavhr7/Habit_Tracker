class communitypost:
    def __init__(self,postid,communityid,userid,content):
        self.postid=postid
        self.userid=userid
        self.content=content
        self.communityid=communityid
        
    def create_communitypost(postid,communityid,userid,content):
        communitypostscollection[communityid].append(communitypost(postid,communityid,userid,content))
        return communitypost(postid,communityid,userid,content)
    
communitypostscollection=dict()