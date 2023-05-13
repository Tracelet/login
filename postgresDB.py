import psycopg2
from psycopg2 import Error
from config import DB_pg_password

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password=DB_pg_password,
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    cursor.execute('''CREATE TABLE SOME_TABLE
                    (ID     INT PRIMARY KEY NOT NULL ,
                    TITLE   TEXT    NOT NULL);
                    
                    INSERT INTO SOME_TABLE VALUES(1, 'some text');
                    INSERT INTO SOME_TABLE VALUES(2, 'some text');
                    INSERT INTO SOME_TABLE VALUES(3, 'some text');
                    INSERT INTO SOME_TABLE VALUES(4, 'some text');
                    SELECT * FROM SOME_TABLE;''')
    connection.commit()
    # Получить результат
    record = cursor.fetchall()
    print("Строки таблицы: ", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")