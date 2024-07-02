# import math

# def pascal_triangle_raw(n):
#     for i in range(n+1):
#         print(math.comb(n, i), end=' ')

# m = 9
# for i in range(m):
#     pascal_triangle_raw(i)
#     print()

a = [1,2,3,4,5]
b = a[::-1]
print(a == b)
c = [2,3,4]
a = c
print(a, c)

print(a[:])

c.append(a)
print(c,'yt')
print(c[3])
print(c[3][3])
print(c[3][3][3])

print('------------------l----------------')
l = []
l.append(a)
print(l)

print('-----------------sd-----------------')
s = [1,2,3]
d = [4,5,6]
s.append(d)
print(s)

print('-----------------rh-----------------')
r = [9,8,7]
# h = [6,5,4]
h = r

print(r, h)
r.append(h)
print(r, 'r')
print(h, 'h')
print(r[3][3][3])

print(h, 'h')
print(h[3][3][3])