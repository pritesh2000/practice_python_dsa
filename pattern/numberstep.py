n = 5 

print('numbers in column')

for i in range(n):
    for j in range(n):
        print(i+1, end=" ")
    print()

print('numbers in rows')

for i in range(n):
    for j in range(n):
        print(j+1, end=" ")
    print()

print('step top to down, left to right')

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

print('reverse of above(symmatric)')

for i in range(n):
    for j in range(n-i,0,-1):
        print("*", end=" ")
    print()

print('step top to down, right to left')

for i in range(n):
    for j in range(i+1,n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

print('reverse of above(symmatric)')

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n-i):
        print("*", end=" ")
    print()

print()
