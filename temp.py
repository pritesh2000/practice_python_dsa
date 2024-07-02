"""
dict1 = {'id' : 1, "name" : 'raj', 'role_id' : 2, 'student_email' : 'raj@gmail.com'}
dict2 = {'id' : 2, "name" : 'harshil', 'role_id' : 4, 'student_email' : 'harshil@gmail.com'}

studentData = []

for i,j in dict1.items():
    studentData.append(f"{i} : {j}")
    
print(studentData)
"""

"""
tup1 = (1,2,3,4)
tup2 = (3,5,6,6)
res = tup1 + tup2
print(tup1)
print(tup2)
print(res)
print(type(res))
"""


# for i in range(8):
#     for j in range(i,-1, -1):
#         print(2**j, end=" ")
#     print()

"""
def fibo(num):
  a,b = 0, 1
  for i in range(0, num):
    yield "{}:: {}".format(i + 1,a)
    a, b = b, a + b
for item in fibo(10):
  print(item)
"""
# dict_a = {'name': "pritesh", 'name': 'tadvi', }
# print(dict_a)
"""
# while doing "for list[-2] in list:" you actually iterate over the list and store the value of current element into list[-2]
list1 = [0,1,2,3]
for list1[-2] in list1:		# it is like assigning value dict['key'] and list[0] 
	# print(list1[2])
	print(list1[-2], end=" ")
	print(list1)
"""


# CHAR = 26
# countChars1 = [0] * CHAR

# print(countChars1)
# print(ord('a'))
# print(ord('b'))
# print(ord('c'))
# print(ord('A'))
# print(ord('%'))
"""
class Solution:
    def __init__(self,num):
        self.num=num
        
    def isPalindrome(self) :
        no1=0
        temp=self.num
        print(temp)
        while(self.num>0):
            print(self.num, "number")
            x=self.num%10
            no1=no1*10 + x
            self.num=self.num//10
        
        if(temp==no1):
               print("palindrome")
        else:
               print("not palindrome")
                    
                     
        
      
num=121
p1=Solution(num)
p1.isPalindrome()
  # num=123321
"""

dict1 = {'name':'Pritesh', 'surname': 'Tadvi'}
print(dict1)
dict1.pop('surname')
print(dict1)
dict1.clear()
print(dict1)

list1 = [1,2,3,4,5]
list1.pop()
print(list1)

set1 = {1,2,3,4,'pritesh'}
set1.pop()
print(set1)

tuple1 = (1,2,3,4,'pritesh',1)
print(tuple1.count(1))
print(tuple1.index(2))
print(tuple1)

a = 10.323290329032
b = 29.98329329
c = a+ b
print(round(c, 2))