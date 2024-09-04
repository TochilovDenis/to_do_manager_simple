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