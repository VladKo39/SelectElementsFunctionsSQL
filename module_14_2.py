import sqlite3
import module_14_1


def module_avg():
    connection = sqlite3.connect('not_telegram.db')
    # подключение к базе данных not_telegram.db с помощью библиотеки sqlite3
    cursor = connection.cursor()
    # создаю объект cursor для выполнения SQL-запросов и операций с базой данных.

    id_ = 6
    cursor.execute('DELETE FROM Users WHERE id=?',
                   (id_,))
    # Удаляю из базы данных not_telegram.db запись с id = 6.

    cursor.execute("SELECT COUNT(*) FROM Users")
    total_user = cursor.fetchone()[0]
    # Подсчитать общее количество записей.

    cursor.execute("SELECT SUM(balance) FROM Users")
    total_balance = cursor.fetchone()[0]
    # Подсчитать сумму баланса users.
    print(f'1 вариант:\n\t'
          f'Cредний баланс всех пользователей\n\t'
          f'через сумму пользователей и сумму баланса пользователей:\n\t'
          f' {round(total_balance / total_user, 2)}')
    print()

    cursor.execute("SELECT AVG(balance) FROM Users")
    avg_balance = cursor.fetchone()[0]
    # Подсчитать средний баланс users.
    print(f'2 вариант:\n\t'
          f'Cредний баланс всех пользователей\n\t'
          f'через функцию AVG():\n\t'
          f' {avg_balance}')

    connection.commit()
    # сохраняю состояние базы данных not_telegram
    connection.close()
    # отключение от базы данных not_telegram


if __name__ == "__main__":
    module_14_1.module_start()
    # Выполнение Кода из предыдущего задания
    print(f'{"*" * 15} Pезультат выполнения программы module_14_2: {"*" * 20}\n')
    module_avg()
    # Выполнение Кода задания
