filename = "'Васильев_Дмитрий_Сергеевич_У-232_vvod_t2.txt'"
with open('Васильев_Дмитрий_Сергеевич_У-232_vvod_t2.txt', "r") as file:
    lines = file.readlines()
    data = [[int(num) for num in line.split()] for line in lines]


for i in range(len(data)):
    a = data[i]
    maxx = max(a)
    minn = min(a)
    a[0], a[-1] = minn, maxx  

# Выводим результаты в файл
output_filename = "Васильев_Дмитрий_Сергеевич_У-232_vivod_t2.txt"
with open('Васильев_Дмитрий_Сергеевич_У-232_vivod_t2.txt', "w") as file:
    for a in data:
        file.write(" ".join(str(num) for num in a) + "\n")

print("Результаты успешно записаны в файл", output_filename)
