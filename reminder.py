class reminder:
    def __init__(self,reminderid,goalid,remindertime):
        self.reminderid=reminderid
        self.goalid=goalid
        self.remindertime=remindertime

    def create_reminder(reminderid,goalid,remindertime):
        reminderscollection[reminderid]=reminder(reminderid,goalid,remindertime)
        return reminder(reminderid,goalid,remindertime)

reminderscollection=dict()
