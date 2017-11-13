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
        createClass(idnum)

    def getClassId(self):
        return idnum

    def createClass(self, idnum):
        self.idnum = idnum
        if idnum == 0:
            self.name = allClasses[0]
        elif idnum == 1:
            self.name = allClasses[1]
        elif idnum == 2:
            self.name = allClasses[2]
        elif idnum == 3:
            self.name = allClasses[3]

    def getClassName(self):
        return allClasses[self.idnum]
