nums = [1,2,3,5,6]          # result should look like [1,2,3,5,4]
nums.sort()
print(nums)

n = len(nums)
differ = 0

for i, num in enumerate(nums):
    print(i, num)

    search = num + n -1
    start = 0
    end = len(nums)-1
    while start <= end:
        # mid = start + (end- start)//2
        mid = (start+ end)//2

        if nums[mid] <= search:
            index = mid
            start = mid + 1
            print('less', i)
        else:
            end = mid - 1
            print('greater', i)
    print(index, 'index', index-i+1)
    differ = max(index-i+1, differ)
    print(differ)


print(n - differ)