numIndex = 3

initial = [1]
for i in range(1, numIndex+1):
    row = [0]*(i+1)
    print(initial, 'initial', row, 'row')
    for j in range(i+1):
        # print(j)
        if j == 0 or j == len(row)-1:
            row[j] = 1
        else:
            row[j] = initial[j-1] + initial[j] 
    initial = row

print(initial)
