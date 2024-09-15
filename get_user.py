from files  import read_users_file

def get_user(users_filename: str) -> str:
    # прочитать файл с пользователями
    # если его нет, то создать
    users =  read_users_file(users_filename)
    # запросить имя пользователя
    user = input("Введите имя пользователя: ")
    if user in users:
        # если имя есть - запросить пароль
        password = input("Введите пароль: ")
        if password == users[user]:
            # если пароль верный - вернуть имя
            return user
        else:
            # если не верный - запросить ещё и вернуть имя если будет верный
            print("Неверный пароль. Попробуем ещё раз.")
    #  или исчерпать количество попыток
    # если нет такого имени - то создать - записать имя и новый пароль
