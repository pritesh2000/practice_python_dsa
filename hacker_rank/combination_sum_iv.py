def combination_sum(nums: list, target:int):
    dp = {0:1}

    for total in range(1,target+1):
        dp[total] = 0
        for j in nums:
            dp[total] += dp.get(total-j,0)

    return dp

nums = [1,2,3]
target = 7
a = combination_sum(nums, target)
print(a)