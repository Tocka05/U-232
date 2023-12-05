def f(x,n):
    def fac(n):
        if n<1:
            return 1
        else:
            return n * fac(n-1)
    return x**n/fac(n)

x = int(input("Введите значение X: "))
n = int(input("Введите значение N: "))

result = f(x, n)
print(f"Результат вычисления: {result}")
