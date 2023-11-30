
m1 = [1, 2, 3, 4, 5]
m2 = [6, 8, 14]
m3 = [8, 6, 4, 2]

def F(M):
    summ= sum(M)
    return summ

def R(M):
    sr = sum(M) // len(M)
    return sr

summ1 = F(m1)
sr1 = R(m1)

summ2 = F(m2)
sr2 = R(m2)

summ3 = F(m3)
sr3 = R(m3)

print("Массив 1: Сумма =", summ1, "Среднее арифметическое =", sr1)
print("Массив 2: Сумма =", summ2, "Среднее арифметическое =", sr2)
print("Массив 3: Сумма =", summ3, "Среднее арифметическое =", sr3)
