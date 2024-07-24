def f(x):
    return x*x

a = f
print(a(5))

#

def calk1(a, b):    # calk1 = lambda a,b: a + b
    return a + b

def calk2(a):
    return a*a

def math(op, x):
    print(op(x))

math(calk2, 5)      # math(lambda a, b: a + b, 5, 45)

#

data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)

#


data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)

#

list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))

#

data = '15 136 234 324 12 123 4 5 3'

data = list(map(int, data.split()))
print(data)

#

data = [15, 136, 234, 324, 12, 123, 4, 5, 3]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

#

# zip - функция дает возможность обьеденения кортежей из нескольких списков по каждому элементу списсков
# enumerate - нумерует обьекты из списков в кортеж 

# 

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
print()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
