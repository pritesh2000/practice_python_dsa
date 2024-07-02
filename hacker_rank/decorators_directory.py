def person_lister(f):
    # def inner(people):
        # complete the function
        # return [f(i) for i in sorted(people, key=lambda l:l[2])]
    # return inner
    return [f(i) for i in sorted(people, key=lambda l:l[2])]

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for _ in range(int(input()))]
    # this *function will execute according to objects store in list 
    print(*name_format(people), sep='\n')