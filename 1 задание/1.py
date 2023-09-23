#1
'''a='Курс Основы программирования начался'
print('Курс Основы программирования начался')'''
#2
'''a=16823
b=12302
c=3092
print((a * b) // c)'''
#3
'''name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
def check(age, name):
    if name != 'Иван':
        if age > 0 and age < 75:
            if age > 16:
                print('Поздравляем вы поступили в ВГУИТ')
            else:
                print(f'Сначала нужно окончить школу!\nВам осталось учиться: {16 - age}')
        else:
            print('Вы ввели недействительный возраст')
    else:
        print('У нас уже достаточно Иванов')
check(age,name)'''
#4
'''seconds = int(input('Введите число секунд: '))
days = seconds // 86400
sec= seconds //1
minutes = seconds // 60
hours = seconds // 3600
print(days,minutes,hours,sec)'''
#5
'''n = int(input('Введите число: '))
a=n + n ** 2 + n ** 3 + n ** 4 + n ** 5
print(a)'''
#6
'''x = input('Введите x: ')
y = input('Введите y: ')
x,y=y,x
print(f'x = {x}\ny = {y}')'''

#7
'''number = int(input('Введите ваше число: '))
if number % 2 == 0:
    print ('Ваше число четное')
else:'''
#8
'''name = input('Ваши фамилия, имя?:')
age = input('Сколько вам лет?:')
place = input('Где вы живёте?:')
print(name)
print(age)
print(place)'''









