def find_max():
    num = int(input("Введите число(0 для окончания): "))

    if num == 0:
        return 0

    max_num = find_max()
    return max(num, max_num)


max_value = find_max()
print(f"Наибольшее значение: {max_value}")
