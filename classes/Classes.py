class Classes:
    #this class contains information only about the classes, not about the user
    #who chose this class.
    #an object of this class would be what the class actually is
    #eg swordsman is object of this class

    allClasses = ["No class", "Warrior", "Ranger", "Mage"]
    
    #variables
    name = None
    idnum = None

    def __init__(self, idnum):#the constructor is basically the createClass function
        self.createClass(idnum)

    def getClassId(self):
        return idnum

    def createClass(self, idnum):
        self.idnum = idnum
        if idnum == 0:
            self.name = self.allClasses[0]
        elif idnum == 1:
            self.name = self.allClasses[1]
        elif idnum == 2:
            self.name = self.allClasses[2]
        elif idnum == 3:
            self.name = self.allClasses[3]

    def getClassName(self):
        return self.allClasses[self.idnum]

    #this should be a class method, but something is calling it right now
    #fix later
    def getAllClasses(self):
        return self.allClasses
