# class GeekforGeeks:

# 	# default constructor
# 	def __init__(self):
# 		self.geek = "GeekforGeeks in OOPS"
        

# 	# a method for printing data members
# 	def print_Geek(self):
# 		print(self.geek)


# # creating object of the class
# obj = GeekforGeeks()

# # calling the instance method using the object obj
# obj.print_Geek()


class Test:
    def __init__(self):
        self.x=10

    def method1(Self):      ##public method
        print("It is public Method")

    def method2(self):
        print(self.x)
        self.method1()

t = Test()
print(t.x)  ##accessing public member
t.method1()      ##accessing public method outside of the class