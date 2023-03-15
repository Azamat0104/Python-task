n = int(input('Введите число: '))
a = n // 100
b = n % 100 // 10
c = n % 10
print(f'{a + b + c} ({a} + {b} + {c})')
