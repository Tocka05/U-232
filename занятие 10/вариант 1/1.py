filename = "Васильев_Дмитрий_Сергеевич_У-232_vvod_t1.txt"
with open('Васильев_Дмитрий_Сергеевич_У-232_vvod_t1.txt', "r") as file:
    lines = file.readlines()
    data = [[int(num) for num in line.split()] for line in lines]
    
summ = 0
pl = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i][j] > 0:
            summ += data[i][j]
            pl += 1

output_filename = "Васильев_Дмитрий_Сергеевич_У-232_vivod_t1.txt"
with open('Васильев_Дмитрий_Сергеевич_У-232_vivod_t1.txt', "w") as file:
    file.write("Сумма элементов над главной диагональю: {}\n".format(summ))
    file.write("Количество положительных элементов над главной диагональю: {}\n".format(pl))

print("Результаты успешно записаны в файл", output_filename)
