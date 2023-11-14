#1
'''a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d=a+b+c
print(d)'''

#2
'''a = int(input('Введите длину первого катета: '))
b = int(input('Введите длину второго катета: '))
s = (1 // 2) * (a * b)
print(s)'''

#3
'''n = int(input('Введите число минут: '))
h = n % (60 * 24) // 60
m = n % 60
print(f'{h}:{m}')'''

#4
'''def main(a,b,l,N):
    length = (2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
    return length
a = int(input('Введите растояние между рядами: '))
b = int(input('Введите расстояние между дырками в ряду: '))
l = int(input('Введите длину свободного конца шнурка: '))
N = int(input('Введите кол-во дырок в ряду: '))
print('Искомая длина шнурка: ', main(a,b,l,N))'''

#5
'''def main(a,b,c):
    numbers = [a,b,c]
    return min(numbers)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('Минимальное число: ', main(a,b,c))'''

#6
'''def nums():
    i = int(input('Введите число от 1 до 8: '))
    if i >= 1 and i <= 8:
        return i
    else:
        print('Неверное число')
        return nums()
def main():
    a = nums() 
    b = nums() 
    c = nums() 
    d = nums() 
    if (a+b+c+d) % 2 == 0:
        return 'Да'
    else:
        return 'Нет'

print(main())'''

#7
'''def main():
    n = int(input('Введите год: '))
    if (n % 4 == 0 and n % 100 != 0) or n % 300 == 0:
        return 'Да'
    else:
        return 'Нет'

print(main())'''

#8
'''def main():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0
print(main())'''

#9
'''def main():
    n = int(input('Введите число n: '))
    m = int(input('Введите число m: '))
    k = int(input('Введите число k: '))
    if k < n * m and (k % n == 0 or k % m == 0):
        return 'Да'
    else:
        return 'Нет'
print(main())'''





