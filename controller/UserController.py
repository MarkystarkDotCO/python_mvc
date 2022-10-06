from controller.model.User import User
from controller.view.view import View
import jwt


class UserController():

    def __init__(self) -> None:
        self._User = User()
        self._View = View(self._User)

    def setUser(self, User):
        self._User = User
    def getUser(self):
        return self._User

    def getUID(self):
        return self._User.getUID()
    def setUID(self, UID):
        self._User.setUID(UID)

    def getUsername(self):
        return self._User.getUsername()
    def setUsername(self, username):
        self._User.setUsername(username)

    def getSault(self):
        return self._User.getSault()
    def setSault(self, sault):
        self._User.setSault(sault)


    def getHash(self):
        return self._User.getHash()
    def setHash(self, hash):
        self._User.setHash(hash)
    # Hashing
    def generatingHash(self):

        secretKey = "mySecret"
        payload = {"UID": self._User.getUID()}

        encoded_jwt = jwt.encode(payload, secretKey, algorithm="HS256")
        print(encoded_jwt)
        decode_jwt = jwt.decode(encoded_jwt, secretKey, algorithms=["HS256"])
        print(decode_jwt)

    def updateView(self):
        self._View = View(self._User)
    def printView(self):
        self._View.printAll()
    
    def test():
        return 0


#Creating Controller
myUserController = UserController()

#setting information
myUserController.setUID(3000)
myUserController.setUsername("admin")
myUserController.setSault("doedeod))))____222##$$")
myUserController.setHash("dwepodopwedn9393e9339399999999999")

#updating information
myUserController.updateView()
#myUserController._View.printAll()

myUserController.generatingHash()
