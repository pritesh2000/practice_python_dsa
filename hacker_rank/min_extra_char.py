def minExtraChar(s: str, dictionary:list[str]) -> int:
    dictionary = set(dictionary)
    n,dp = len(s),[0]
    max_word_len = len(max(dictionary, key=len))

    for i in range(1,n+1):
        dp.append(dp[-1]+1)
        print(len(dp))
        print(i-1, max(i-max_word_len-1,-1), 'i-1, maxworldlen')
        for j in range(i-1,max(i-max_word_len-1,-1),-1):
            print(j, i, 'ji')

            if s[j:i] in dictionary:
                dp[i] = min(dp[i],dp[j])
                print(dp[i], dp[j])
                print(s[j:i])
        print(dp)
        
    return dp[-1]

s = "leetscode"
dictionary = ["leetcode", "leet", "code"]
s = "sayhelloworld"
dictionary = ["hello","world"]

print(minExtraChar(s, dictionary))