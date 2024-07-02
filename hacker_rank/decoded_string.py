s = "leet2code3"
s = 'dee2coejk'
k = 10
# k = 15
# leetleetcodeleetleetcodeleetleetcode

# s = "cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
# k = 480551547

count = 0
i = 0
while count < k :
    if s[i].isdigit():
        count *= int(s[i])
    else:
        count += 1
    print(count, i, s[i])
    i += 1
print()
print(count, i, s[i-1], 'char')

for j in range(i-1, -1, -1):
    if s[j].isdigit():
        count //= int(s[j])
        k %= count
        print('pritesh', count)
    else:
        print(j, 'in else', s[j], count)
        if k == 0 or k == count:
            print(s[j])
        count -= 1 