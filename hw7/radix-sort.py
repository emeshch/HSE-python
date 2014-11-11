import time
import random


rand_list = random.sample(range(1000), 6)
rand_list.append(1)
# print("rand_list ", rand_list)
str_list = [str(item) for item in rand_list]

start_time = time.clock()   # timer ON
#list_sorted = [0]*len(l)


# modlist = []
# divlist = []
# modlist = [i % 10 for i in rand_list]
# divlist = [i // 10 for i in rand_list]
# print("div= ", divlist, "mod= ", modlist)

maxlength = max(len(i) for i in str_list)
str_list = [item.zfill(maxlength) for item in str_list]
print(str_list)

n = 1
modlist = [item[-1] for item in str_list]
divlist = [item[:-1] for item in str_list]
print(modlist)
print(divlist)

def counting_sort(divlist, modlist):
    sortedlist = []
    temp = [0] * 10       # we could take not 10 but max(modlist)+1
    # print("index", [i for i in range(10)])
    for item in modlist:
        # print(item)
        temp[item] += 1
    # print("temp ", temp)     # temp[i] now contains the number of elements equal to i
    # print("index", [i for i in range(10)])

    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    # print("index", [i for i in range(10)])
    # print("count", temp)    # counted[i] now contains the number of elements <= i

    result = [0]*(len(modlist) + 1)
    div_res = [0]*(len(modlist) + 1)    #2DO rename
    for i in range(0, len(modlist), 1):
        # print(i, modlist[i], temp[modlist[i]])
        result[temp[modlist[i]]] = modlist[i]
        div_res[temp[modlist[i]]] = divlist[i]
        temp[modlist[i]] -= 1
    result.pop(0)
    div_res.pop(0)
    # print("mod= ", modlist)
    # print("div= ", div_res)
    print("sorted ", result)
    sortedlist = [(10*div_res[i] + result[i]) for i in range(len(result))]
    print("! ", sortedlist)
    # return sortedlist
    # print("count ", temp)

# counting_sort(divlist, modlist)

time = time.clock() - start_time
# print("time: {0:.4f} sec".format(time))
#print(list_sorted)


















