# Enter your code here. Read input from STDIN. Print output to STDOUT
# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

b = "Pritesh123098"
print(*sorted(b,key=lambda a:(a.islower(),a in '98765', a)), sep="")
print(*sorted(b), sep="")
print()
print(sorted(b, key=lambda a:a.islower()), sep="")
print()
print(*sorted(b, key=lambda a:a.islower()), sep="")
print(*sorted(b, key=lambda a:a.isdigit()), sep="")
print(*sorted(b, key=lambda a:a.isalpha()), sep="")
print()
print(*sorted(b, key=lambda a:(a.isdigit(),a.islower())), sep="")
print(*sorted(b, key=lambda a:(a.isdigit()-a.islower())), sep="")
print()
print(*sorted(b, key=lambda a:(a.islower(), a)), sep="")

