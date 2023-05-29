#26

def step(n, m):
    res = 1
    for _ in range(m):
        res *= n
    return res

n = int(input('Введите число'))
m = int(input('Введите степень'))
res = step(n, m)
print(n, 'в', m, 'степени', ' = ', res)

#28

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
res = sum(a, b)
print(a, '+', b, ' = ', res)
