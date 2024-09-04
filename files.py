# Создаем список форматированных строк чисел от 1 до 49
# Используем списковое включение для компактного создания списка
# где внутри [этого кода это компрехенсия список]
generate_num: list = [str(i) + '\n' for i in range(1, 50)]

# generate_num: list = []
# for i in range(50):
#     generate_num.append(str(i) + '\n')

# записывает содержимое в файл
with open('file.txt', 'w') as file:
    file.writelines(generate_num)

# Чтение всего содержимого файла

# Используем read() для чтения всех строк в одну переменную
with open('file.txt', 'r') as file:
    print(file.read())

# Чтение первой строки файла
# Используем readline() для чтения только первой строки
with open('file.txt', 'r') as file:
    print(file.readline())


# Чтение всего содержимого файла как списка строк
# Используем readlines() для получения списка всех строк
with open('file.txt', 'r') as file:
    print(file.readlines())
