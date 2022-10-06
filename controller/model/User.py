#User Model
class User():

    def __init__(self) -> None:
        self.UID = ''
        self.username = ''
        #self.password = ''
        #self.startDate = ''
        #self.endDate = ''
        self.sault_pwd = '' 
        self.hash_pwd = ''
        #self.personalInformation = {}
    def getUID(self):
        return self.UID
    def setUID(self, UID):
        self.UID = UID
    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username = username
    def getSault(self):
        return self.sault_pwd
    def setSault(self, sault):
        self.sault_pwd = sault
    def getHash(self):
        return self.hash_pwd
    def setHash(self, hash):
        self.hash_pwd = hash


#user_A = User()

#user_A.setUID(3000)

#print(user_A.getUID())