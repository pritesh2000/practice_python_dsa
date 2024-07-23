for i in range(6):
    # print((i+1)*"*")
    for j in range(i + 1):
        print(i, end=" ")
    print()

    
for i in range(6):
    for k in range(i+1, 6):
        print(" ", end=" ")   
    for j in range(i+1):
        print(j, end=" ") 
    print()

s = 0
for i in range(1, 6):
    for j in range(1, i+1):
        s += 1
        print(s, end=" ")
        if i == j:
            break
    print()
    

for i in range(6):
    # print((i+1)*"*")
    a = 65
    for j in range(i + 1):
        print(chr(a), end=" ")
        a += 1
    print()

for i in range(6):
    for j in range(6):
        if i == 0 or j == 0 or i == 5 or j== 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
