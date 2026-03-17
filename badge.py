class badge:
    def __init__(self,name,description):
        self.name=name
        self.description=description

    @staticmethod
    def create_badge(name,description):
        badgescollection[name]=badge(name,description)
        return badgescollection[name]

badgescollection=dict()
