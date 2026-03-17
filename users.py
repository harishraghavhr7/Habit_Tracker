from habit import create_habit


class users:
    def __init__(self,userid,username,email,password):
        self.userid=userid
        self.username=username
        self.email=email
        self.password=password
        userscollection[userid]=self
    
    @staticmethod
    def create_user(userid,username,email,password):
        return users(userid,username,email,password)
    
    def create_habit(self,habitid,habitname):
        return create_habit(self.userid,habitid,habitname)
    
    @staticmethod
    def get_by_id(userid):
        return userscollection.get(userid)
    
    @staticmethod
    def  update_user(userid,username=None,email=None,password=None):
        user=userscollection.get(userid)
        if not user:
            raise ValueError("User not found")
        if username:
            user.username=username
        if email:
            user.email=email
        if password:
            user.password=password
        return user

userscollection=dict()
