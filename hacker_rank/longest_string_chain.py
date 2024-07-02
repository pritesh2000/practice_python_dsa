words = ["a","b","ba","bca","bda","bdca"]
# m = max(words)
# l = min(words)
# print(m,l)
dp = {}
for word in words:
    dp[word] = 1
    # print(word)
    for char in range(len(word)):
        prev_word = word[:char] + word[char +1:]
        if prev_word in dp:
            dp[word] = max(dp[word], dp[prev_word] + 1)
print(max(dp.values()))
