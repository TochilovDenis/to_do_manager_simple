# Создаем список форматированных строк чисел от 1 до 49
# Используем списковое включение для компактного создания списка
# где внутри [этого кода это компрехенсия список]
generate_num: list = [str(i) + '\n' for i in range(1, 50)]

# generate_num: list = []
# for i in range(50):
#     generate_num.append(str(i) + '\n')

# записывает в файл
file = open('file.txt', 'w')
# for i in generate_num:
#     file.write(i)
file.writelines(generate_num)
file.close()


# Чтение всего содержимого файла

# Используем read() для чтения всех строк в одну переменную
file_read_1 = open('file.txt', 'r')
line1 = file_read_1.read()
print(line1)
file.close()

# Чтение первой строки файла
# Используем readline() для чтения только первой строки
file_read_2 = open('file.txt', 'r')
print(file_read_2.readline())
file.close()

# Чтение всего содержимого файла как списка строк
# Используем readlines() для получения списка всех строк
file_read_3 = open('file.txt', 'r')
print(file_read_3.readlines())
file.close()

