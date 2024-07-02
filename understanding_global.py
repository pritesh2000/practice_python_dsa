class PracticeGlobal:
    global n
    def __init__(self, var):
        self.var = 55
        
        return None

    def changer(self, n):
        self.var = n
        n = 99
        return self.var, n

    def doubleChanger(self, varri,n):
        
        self.var = varri
        varri = n
        n = self.var
        print('self.var, varri, n', self.var, varri, n)

number = PracticeGlobal(22)
print(number.changer(3))
print(number.doubleChanger(7, 9))
