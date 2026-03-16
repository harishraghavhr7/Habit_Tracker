class journal:
    def __init__(self,entryid,userid,habitid,goalid,date,entry):
        self.entryid=entryid
        self.userid=userid
        self.habitid=habitid
        self.goalid=goalid
        self.date=date
        self.entry=entry

def create_journal(entryid,userid,habitid,goalid,date,entry):
    journalscollection[entryid]=journal(entryid,userid,habitid,goalid,date,entry)
    return journal(entryid,userid,habitid,goalid,date,entry)

journalscollection=dict()