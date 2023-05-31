def summ(a, b):
    print(f'a = {a}, b = {b}')
    if b != 0:
        return summ(a + 1, b - 1)
    return a
print(summ(2, 2))


def step(A, B):
    if B == 1:
        return A
    if ( B != 1):
        return (A * step(A, B - 1))
A = int(input('Введите число'))
B = int(input('Введите степень'))
print(A, 'в', B, 'степени', ' = ', step(A, B))

