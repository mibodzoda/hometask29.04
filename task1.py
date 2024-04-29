list1 = input().split()
list2 = input().split()

list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)