my_dict = {'x':500,'y':5874,'z':560}
a = -100000000000000000
for key,value in my_dict.items():
    if value > a:
        a = value
print(f'maximum number:{a}')