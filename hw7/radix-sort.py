import random

rand_list = random.sample(range(100), 6)
print("l=", rand_list)

#list_sorted = [0]*len(l)

#n=10
modlist = []
modlist = [i % 10 for i in rand_list]
print("mod= ", modlist)


def counting_sort(modlist):
    temp = [0] * 10         # we could take not 10 but max(modlist)+1
    print("index", [i for i in range(10)])
    for item in modlist:
        # print(item)
        temp[item] += 1
    print("temp ", temp)     # temp[i] now contains the number of elements equal to i
    print("index", [i for i in range(10)])

    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    print("counted", temp)    # counted[i] now contains the number of elements <= i

    result = [0]*(len(modlist) + 1)
    for num in modlist:
        # print(i, modlist[i], temp[modlist[i]])
        result[temp[num]] = num
        temp[num] -= 1
    print("sorted ", result)
    # print("count ", temp)
counting_sort(modlist)

#print(list_sorted)


















