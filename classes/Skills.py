class Skills:
    allSkills = ["Charge"]

    multiplier = None
    name = None

    def __init__(self, multiplier, name):
        self.multiplier = multiplier
        self.name = name

    def getAllSkills(self):
        return self.allSkills
