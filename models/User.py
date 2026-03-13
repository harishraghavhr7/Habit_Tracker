class User:

    def __init__(self,username,email,password=None,scores=0,level=1):
        self.username = username
        self.email = email
        self.password = password
        self.scores = scores
        self.level = level
    
    def __str__(self):
        return f"User(username={self.username}, email={self.email}, scores={self.scores}, level={self.level})"
    
    def add_score(self,points):
        
        self.scores+=points
        self.level = self.scores // 100 + 1

        print(f"{self.username} earned {points} points! Total score: {self.scores}, Level: {self.level}")
    
    def check_password(self,password):
        return self.password == password
    
    def display_stats(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Scores: {self.scores}")
        print(f"Level: {self.level}")

user=User("harish","harish@gmail.com","password123")

user.display_stats()
user.add_score(50)
user.add_score(60)
user.display_stats()