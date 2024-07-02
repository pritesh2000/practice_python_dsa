flowers = [[1,10],[3,3]]
people = [3,3,2]

flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]

res = []

for i in people:
    max = 0
    for ran in flowers:
        if i in range(ran[0], ran[-1]+1):
            max += 1
    res.append(max)
print(res)

# binary search
numbers = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20,21,22,23]
target = 13
start = 0
end = len(numbers)-1
print(start, end)
while start <= end:
    mid = (start+ end)//2
    print(start, mid, end)
    if numbers[mid] < target:
        start = mid + 1
        print(start, mid, 'in if less', end)
    elif numbers[mid] > target:
        end = mid - 1
        print(start, 'in if greater', mid, end)
    else:
        start = mid + 1
        # end = mid - 1 
        print(start, mid, end, 'in equal')
print(start)
print(mid)
print(end)