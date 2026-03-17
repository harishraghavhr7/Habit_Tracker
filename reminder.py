class reminder:
    def __init__(self,reminderid,goalid,remindertime):
        self.reminderid=reminderid
        self.goalid=goalid
        self.remindertime=remindertime

    @staticmethod
    def create_reminder(reminderid,goalid,remindertime):
        reminderscollection[reminderid]=reminder(reminderid,goalid,remindertime)
        return reminderscollection[reminderid]
    
    @staticmethod
    def delete_reminder(reminderid):
        if reminderid in reminderscollection:
            del reminderscollection[reminderid]
        else:
            raise ValueError("Reminder not found")
        
    @staticmethod
    def list_reminders_by_goalid(goalid):
        return [reminder for reminder in reminderscollection.values() if reminder.goalid == goalid]

reminderscollection=dict()
