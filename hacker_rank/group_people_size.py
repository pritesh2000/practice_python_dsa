groupSizes = [3,3,3,3,3,1,3]
# groupSizes = [2,1,3,3,3,2]

def groupThePeople(groupSizes):
    list_i = []
    list_sub = {}
    set_sub = set(groupSizes)

    for i in set_sub:
        list_sub[i] = []
    
    for person in range(len(groupSizes)):
    
        for group_size in list_sub:
    
            if groupSizes[person] == group_size:
                list_sub[group_size].append(person)
    
                if len(list_sub[group_size]) == group_size:
                    list_i.append(list_sub[group_size])
                    list_sub[group_size] = []
                

    print(list_sub)
    print(list_i)

groupThePeople(groupSizes)