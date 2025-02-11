class task1(object):
    def __init__(self):
        self.s=""

    def getString(self):
        self.s=input()
    
    def printString(self):
        print(self.s.upper())

strObj =task1()
strObj.getString()
strObj.printString()