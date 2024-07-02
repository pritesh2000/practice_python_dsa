nums = [1,3,4,2,2]
nums = [3,1,10,11,12,13,3,4,2,5,6,7,8,9]

slow = 0
fast = 0

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    print(slow, fast)
    if slow == fast:
        break

fast = 0
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
    if slow == fast:
        print(slow)
