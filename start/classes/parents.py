# 基类
class Father(object):
    def __init__(self, house):
        self.house = house

    def setHouse(self, house):
        self.house = house

    def getHouse(self):
        return self.house

    def myFather(self):
        print('I`m your father Joho Snow~')

class Mother(object):
    def __init__(self, sister):
        self.sister = sister

    def setSister(self, sister):
        self.sister = sister

    def getSister(self):
        return self.sister

    def myMother(self):
        print('I`m your monther Jojo :)')
