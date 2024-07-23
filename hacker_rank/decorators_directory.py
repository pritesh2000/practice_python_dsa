# people = ["Steve smith Alaska M".split()]
people = [
    "Steve smith Alaska M".split(),
    "Jane doe California F".split(),
    "Alice Johnson NewYork F".split(),
    "Bob Brown Texas M".split()
]

global i
i = 0

def person_lister(f):
    global i
    i += 1
    print(i, "----------inside person_lister f:", f)
    def inner(people):
        global i
        # complete the function
        i += 1
        print(i, "-----------inside inner people:",people)
        return [f(i) for i in sorted(people, key=lambda l:l[2])]
    return inner
    # return [f(i) for i in sorted(people, key=lambda l:l[2])]

@person_lister
def name_format(person):
    global i
    i += 1
    print(i, "-----inside name_format person:", person)
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


# people = [input().split() for _ in range(int(3))]
i += 1
print(i,people, "after all")
# this *function will execute according to objects store in list 
print(*name_format(people), sep='\n')

# don't know why flow of this program goes this way
# 1 ----------inside person_lister f: <function name_format at 0x000001B2D1965090>
# 2 [['Steve', 'smith', 'Alaska', 'M'], ['Jane', 'doe', 'California', 'F'], ['Alice', 'Johnson', 'NewYork', 'F'], ['Bob', 'Brown', 'Texas', 'M']] after all
# 3 -----------inside inner people: [['Steve', 'smith', 'Alaska', 'M'], ['Jane', 'doe', 'California', 'F'], ['Alice', 'Johnson', 'NewYork', 'F'], ['Bob', 'Brown', 'Texas', 'M']]
# 4 -----inside name_format person: ['Steve', 'smith', 'Alaska', 'M']
# 5 -----inside name_format person: ['Jane', 'doe', 'California', 'F']
# 6 -----inside name_format person: ['Alice', 'Johnson', 'NewYork', 'F']
# 7 -----inside name_format person: ['Bob', 'Brown', 'Texas', 'M']
# Mr. Steve smith
# Ms. Jane doe
# Ms. Alice Johnson
# Mr. Bob Brown


#######################
# # Correctly initialize the people list
# people = [
#     "Steve smith Alaska M".split(),
#     "Jane doe California F".split(),
#     "Alice Johnson NewYork F".split(),
#     "Bob Brown Texas M".split()
# ]
# print(people, "people original")

# def person_lister(f):
#     def inner(people):
#         # Sort people by the third element (state) and return formatted names
#         return [f(person) for person in sorted(people, key=lambda l: l[2])]
#     return inner

# @person_lister
# def name_format(person):
#     # Format the name based on gender
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# # Print the formatted names
# print(people, "before *name_format")
# print(*name_format(people), sep='\n')