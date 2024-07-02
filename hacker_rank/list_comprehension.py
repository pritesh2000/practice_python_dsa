x = int(input())
y = int(input())
z = int(input())
n = int(input())

# l = list()
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k == n:
#                 pass
#             else:
#                 l.append([i,j,k])

# print(l)

list1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(list1)