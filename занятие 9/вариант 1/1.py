def F(M):
    summ = 0
    pl = 0
    f = len(M)
    for i in range(f):
        for j in range(i + 1, f):  
            if M[i][j] > 0:  
                summ += M[i][j]  
                pl += 1  
    return summ, pl
A = [
    [1, 2, -3],
    [-4, 5, 6],
    [7, -8, 9]
]
summ, pl = F(A)
print("Сумма элементов над главной диагональю:", summ)
print("Количество положительных элементов над главной диагональю:", pl)
