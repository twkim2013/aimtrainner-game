list_array = ['apple','banana', 'apple','orange']

dic = {'apple':0, 'banana':0, 'orange':0}

for list in list_array:
    dic[list] += 1
print(dic)


