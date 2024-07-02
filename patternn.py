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
