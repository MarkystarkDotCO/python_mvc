from controller.UserController import UserController

mockDatabase = {"username":"mememe",
                "password":"3838338ej",
                "UID":"3000"
                }


username = str(input("please enter your username"))
password = str(input("please enter your password"))

#Creating Controller
myUserController = UserController()
#setting information

myUserController.setUID(3000)
myUserController.setUsername(username)
myUserController.setSault("doedeod))222##$$")
myUserController.setHash(password)

#updating information
myUserController.updateView()
myUserController.printView()

#generatin hash 
#myUserController.generatingHash()







