n = int(input())
student = []
[student.append([input(), float(input())]) for i in range(n)]
print(student)
print(type(student))

list1 = [j for i,j in student]
sorted_set = sorted(list(set(list1)))
print(sorted_set)
print(sorted_set[1])
second_lowest = sorted_set[1]

name = [i for i,j in student if second_lowest == j]
final = [i for i in sorted(name)]
for i in final:
    print(i)
