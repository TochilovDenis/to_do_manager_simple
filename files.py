generate_num: list = []

for i in range(50):
    generate_num.append(str(i) + '\n')


file = open('file.txt', 'w')
for i in generate_num:
    file.write(i)
file.close()