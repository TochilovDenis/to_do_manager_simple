from files  import read_users_file, add_users_file
from errors import NoMoreAttempts, RefuseToCreateNewUser
from hashlib import md5

def hashed(s:str) -> str:
    return md5(s.encode()).hexdigest()

def get_user(users_filename: str) -> str:
    # прочитать файл с пользователями
    # если его нет, то создать
    users =  read_users_file(users_filename)
    # запросить имя пользователя
    user = input("Введите имя пользователя: ")
    if user in users:
        attempts = 5
        for _ in range(attempts):
            # если имя есть - запросить пароль
            password = input("Введите пароль: ")
            if hashed(password) == users[user]:
                # если пароль верный - вернуть имя
                return user
            else:
                # если не верный - запросить ещё и вернуть имя если будет верный
                print("Неверный пароль. Попробуем ещё раз.")
        else:
            #  или исчерпать количество попыток
            raise NoMoreAttempts("Больше никаких попыток. До свидания.")


    choice = input("Нет такого пользователя. Создаем? [Да/Нет]\n_:")
    if choice == 'Нет':
        raise RefuseToCreateNewUser("Нельзя продолжать не создав этого пользователя. До свидания.")

    # если нет такого имени - то создать - записать имя и новый пароль
    attempts = 5
    for _ in range(attempts):
        password = input("Введите пароль: ")
        password_again = input("Введите пароль еще раз: ")
        if password == password_again:
            users[user] = hashed(password)
            add_users_file(users_filename, user, hashed(password))
            break
        print(f"Введённые пароли не совпадают, попробуйте ещё раз")
    else:
        raise NoMoreAttempts("Больше никаких попыток. До свидания.")