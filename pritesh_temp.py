people = [input().split() for i in range(int(input()))]
print(people)

print(sorted(people, key=lambda l : l[2]))
[print(i) for i in sorted(people, key=lambda l:l[2])]
