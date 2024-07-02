a = 2_3_5
print(a*2)

b = 2#3#4
print(b)

c = 233_3
print(c*2)

d = 2_3
print(d*2_3)

if 0:
    print("not error")
elif 1:
   print("no")
else:
 print("error")

def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)