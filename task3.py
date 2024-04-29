list = input().split()

for i in range(len(list)):
    if list[i]=="":
        del list[i]
print(list)