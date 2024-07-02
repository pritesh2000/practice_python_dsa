#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Write your code here
    c = [0]*123
    result = ""
    
    for i in range(len(s)):
        x = ord(s[i])
        c[x] += 1
        
    for i in range(48, 58):
        if c[i]==0:
            result+=chr(i)
    for i in range(97, 123):
        if c[i]==0:
            result+=chr(i)
    return result

s = "829389aohifoir"
print(missingCharacters(s))
