n=5
num = n*2-1

for i in range(num):
    for j in range(num):
        if i==j or i+j==n+3:
            print(i+1, end=" ")
        else:
            print("*", end=" ")
    print()