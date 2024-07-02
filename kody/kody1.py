# 1 Write a program to print numbers having exactly 3 factors between 6 and 986
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))


def fact_3(num):
    fact = 0
    for i in range(1, num+1):
        if num%i==0:
            fact+=1
    if fact!=3:
        return
    else:
        return fact

for i in range(a, b+1):
    if fact_3(i) ==3:
        print(i)

# print(fact_3(7))