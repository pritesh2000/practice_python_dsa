s = "abc"
t = "ahbgdc"

# s = "axc"
# t = "ahbgdc"

print(s in t)
sub = list(s)       # there is no need to make list out of string, you can make use of string without changing it to list
listt = list(t)
print(sub)
print(listt)
print(sub in listt)

sub_point = 0
listt_point = 0
number_of_character = 0
cop = list()
while sub_point < len(sub):

    while listt_point < len(listt):
        
        if sub[sub_point] == listt[listt_point] and sub_point <= listt_point:
            cop.append(sub[sub_point])
            number_of_character = listt_point + 1 
            break 

        listt_point += 1
    listt_point = number_of_character
    sub_point += 1

print(number_of_character)
print(sub_point, listt_point)
print(cop)
print(sub)
print(cop == sub)
