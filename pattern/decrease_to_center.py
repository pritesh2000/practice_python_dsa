
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4   

n = 4
no = n
num = n*2-1 # 7
for i in range(num):    # (0,6) include 6
    for j in range(num):

        # if i + j < (n-1)*2+1 and 0 < i < n and i >= j > 0:
        #     # print("i,j--", (i,j), end=" ")
        #     no -= 1
        # elif i + j >= (n-1)*2+1 and 0 < i < n and i <=j:
        #     # print((i,j), "i,j++", end=" ")
        #     no += 1
        # elif i + j < (n-1)*2 + 1 and i >= n and i > j > 0:
        #     no -= 1
        #     # print((i,j),"i,j--2", end=" ") 
        # elif i + j >= (n-1)*2 + 1 and i >= n and j > i:
        #     no += 1
        #     # print((i,j), "i,j++2", end=" ") 
        
        if i + j < (n-1)*2+1 and (0 < i < n and i >= j > 0 or i >= n and i > j > 0):
            # print("i,j--", (i,j), end=" ")
            no -= 1
        elif i + j >= (n-1)*2+1 and (0 < i < n and i <=j or i >= n and j > i):
            # print((i,j), "i,j++", end=" ")
            no += 1         
        
        # print(no,(i,j), end=" ")
        print(no, end=" ")

    print()