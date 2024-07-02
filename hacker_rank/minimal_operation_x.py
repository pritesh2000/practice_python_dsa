nums = [1,1,4,2,3]
# nums = [3,2,20,1,1,3]   
x = 5

min_oper = float("inf")
total_sum = sum(nums)
target_sum = total_sum - x

left = 0
right = 0
n = len(nums)

current_sum = 0

while right < n:
    current_sum += nums[right]
    right += 1
    print(current_sum, 'outer')
    while left < n and target_sum < current_sum:
        current_sum -= nums[left]
        left += 1
        print(current_sum, 'inner')
    print(right, left)
    if current_sum == target_sum:
        min_oper = min(min_oper, n-right+left)
        print(n-(right - left))
    
    print()
print(n-right+left)
print(min_oper)