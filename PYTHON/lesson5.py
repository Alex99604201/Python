stroka = input().split() # функция деления строки в массив где в скобках указывается разделитель
res = {}

for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}', end=' ')
    else:
        print(i, end=' ')
    
    res[i] = res.get(i, 0) + 1 


stroka = input().split()

set_1 = set()
for i in stroka:
    set_1.add(i.lower())

print(len(set_1))


