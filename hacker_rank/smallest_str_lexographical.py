s = "cbacdcbc"
# Output: "acdb"

dp = dict()
for i,ch in enumerate(s): # for this dict we can store just the count also and keep decreasing it.
    dp[ch] = i

stack = []
for i, char in enumerate(s):

    if char in stack:
        continue
    
    while stack and stack[-1] > char and i < dp[stack[-1]]:
        stack.pop()
    
    stack.append(char)

print(''.join(stack))
