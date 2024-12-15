import sqlite3

def module_start():
    connection = sqlite3.connect('not_telegram.db')
    # подключение к базе данных not_telegram.db с помощью библиотеки sqlite3
    cursor = connection.cursor()
    # создаю объект cursor для выполнения SQL-запросов и операций с базой данных.

    cursor.execute("DROP TABLE IF EXISTS Users")
    # Удаляю данную таблицу из базы, если она создана.
    # (Для выполнения задачи, что бы исключить при запуске добавления позиций
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')
    # Создаю таблицу Users в базе данных not_telegram

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON Users (username)")
    # создаю индекс idx_username на поле username таблицы Users, если он ещё не существует

    for id_ in range(10):
        cursor.execute('INSERT INTO Users('
                       'username,'
                       'email,'
                       'age,'
                       'balance)'
                       ' VALUES(?,?,?,?)',
                       (
                           f'User{id_ + 1}',
                           f'example{id_ + 1}@gmail.com',
                           (id_ + 1) * 10,
                           1000
                       )
                       )
    # заполнение базы данных по условиям задачи

    cursor.execute("SELECT COUNT(*) FROM Users")
    total_user = cursor.fetchone()[0]
    # подсчитываю количество записей в таблице для прохождения
    # в цикле для
    # UPDATE Users  SET balance=? WHERE username=? и
    # DELETE FROM Users WHERE username=?

    for id_ in range(1, total_user + 1, 2):
        cursor.execute("UPDATE Users  SET balance=? WHERE username=?",
                       (500, f'User{id_}'))
        # Обновляю balance у каждой 2ой записи начиная с 1ой на 500

    for id_ in range(1, total_user + 1, 3):
        cursor.execute('DELETE FROM Users WHERE username=?',
                       (f'User{id_}',))
        # Удаляю каждую 3ую запись в таблице начиная с 1ой

    cursor.execute('SELECT * FROM Users WHERE age<>? ORDER By age ASC', (60,))
    # отбор всех данных при условии age(возраст)<>60 c сортировкой по аолю age(возраст)
    print(f'{"*" * 15} Pезультат выполнения программы module_14_1: {"*" * 20}\n')
    users = cursor.fetchall()
    # Метод fetchall() возвращает массив, содержащий все строки результирующего набора.
    for user in users:
        print(f'{user[1]}'
              f' | Почта: {user[2]}'
              f' | Возраст: {user[3]}'
              f' | Баланс: {user[4]}'
              )
        # вывод на печать результат отбора по полям
        # username(пользователь)
        # email(почта)
        # возраст(age)
        # баланс(balance)

    connection.commit()
    # сохраняю состояние базы данных not_telegram
    connection.close()
    # отключение от базы данных not_telegram

if __name__ == "__main__":
    module_start()
