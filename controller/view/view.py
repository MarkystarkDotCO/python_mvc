#import sys
 
# setting path
#sys.path.append('../controller')
 
#from model.User import User
class View():

    def __init__(self, User):
        self.User = User
        
    def printUID(self):
        print(self.User.getUID())

    def printUsername(self):
        print(self.User.getUsername())
    
    def printSault(self):
        print(self.User.getSault())

    def printHash(self):
        print(self.User.getHash())
    
    
    def printAll(self):
        print(self.User.getUID())
        print(self.User.getUsername())
        print(self.User.getSault())
        print(self.User.getHash())
    

"""
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


"""

#myUser = User()

#myUser.setUID(3000)


#myView = View(myUser)

#myView.printAll()