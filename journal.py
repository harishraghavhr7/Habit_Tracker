class journal:
    def __init__(self,entryid,userid,habitid,goalid,date,entry):
        self.entryid=entryid
        self.userid=userid
        self.habitid=habitid
        self.goalid=goalid
        self.date=date
        self.entry=entry

    @staticmethod
    def list_journals_by_userid(userid):
        return [journal for journal in journalscollection.values() if journal.userid == userid]

def create_journal(entryid,userid,habitid,goalid,date,entry):
    journalscollection[entryid]=journal(entryid,userid,habitid,goalid,date,entry)
    return journalscollection[entryid]

journalscollection=dict()