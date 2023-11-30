#f-фигура,a-стороны
def N(f,a):
    if f=='круг':
        print(a[0])
        result=3.14*(a[0]**2)
    if f == 'квадрат':
        A,B=a
        result=A*B
    if f=='треугольник':
        A,B=a
        result=(A*B)//2
    return ' Площадь {} = {}'.format(f, result)
    
f = input('фигура >>>  ')
a=[float(i) for i in input('данные через пробел >>> ').split()]
print(N(f,a))

