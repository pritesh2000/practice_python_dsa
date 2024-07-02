n = 10
num = n*2-1

for i in range(num):
    for j in range(num):
        if i < n:    
            if i==j or i+j==n*2-2:
                print(i+1, end=" ")
            else:
                print(" ", end=" ")
        if i >= n:
            l= num-i
            if i==j or i+j==n*2-2:
                print(l, end=" ")
            else:
                print(" ", end=" ")
    print()