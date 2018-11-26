list1 = ["아스날","에메리"]
list2 = ["리그우승","FA컵우승","유로파우승"]
list3=[]
for i in  range(len(list1)):
    for j in range(len(list2)):
        list3.append([list1[i],list2[j]])

print(list3)


