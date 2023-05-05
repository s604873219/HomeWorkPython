# 1
a = input('Введите ваше имя:')
b = input('Введите пароль:')
c = int(input('Ввeдите ваш возраст:'))
print('Ваши данные для входа в аккаунт: имя', a, 'пароль', b, 'Возраст', c, 'лет')
# 2
sec = int(input('Введите время в секундах:'))
secon = sec % (24 * 3600)
hour = secon // 3600
minut = secon // 60
print('Время в формате ч:м:с-', hour, ':', minut, ':', secon)
# 3
n = int(input("Введите число n:"))
a = str(n)
n2 = a + a
n3 = a + a + a
print('Сумма n+nn+nnn =', n + int(n2) + int(n3))
# 4
rev = int(input('Введите выручку фирмы:'))
exp = int(input('Введите издержки фирмы:'))
staff = int(input('Введите численность сотрудников фирмы: '))
result = (rev - exp)
rent = float(exp / rev)
restaff = float(result / staff)
if result >= 0:
    print('Финансовый результат - Прибыль =', result)
    print('Рентабельность выручки = ', rent)
    print('Прибыль фирмы в расчете на одного сотрудника =', restaff)
else:
    print('Финансовый результат - Убыток =', result)
