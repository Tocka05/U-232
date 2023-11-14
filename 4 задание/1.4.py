#1
'''a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
for i in range(a, b + 1):
    print(i)'''

#2
'''a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)'''

#3
'''a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
if a > b:
    for i in range(a, b + -1, -1):
        if i % 2 != 0:
            print(i)
else:
    print('Число A должно быть больше чем число B')'''

#4
'''s = 0
n = int(input('Введите кол-во чисел: '))
for i in range(n):
    a = int(input(f'Введите число №{i+1}: '))
    s += a
print(s)'''

#5
'''s = 0
n = int(input('Введите число n: '))
for i in range(1, n + 1):
    s += i**3
print(s)'''

#6
'''s = 1
n = int(input('Введите число n: '))
for i in range(1, n + 1):
    s *= i
print(s)'''

#7
'''a = 1
s = 0
n = int(input('Введите число n: '))
for i in range(1, n + 1):
    a *= i
    s += a
print(s)'''

#8
'''n = int(input('Введите число n: '))
for i in range(1, n + 1):
    for x in range(1, i + 1):
        print(x, sep='', end='')
    print()'''

#9
'''n = int(input('Введите число n: '))
fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])
print(sum(fib))'''

#10
'''n = int(input('Введите число n: '))
k = int(input('Введите число k: '))
fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])
print(sum(fib[k-1:]))'''





    




