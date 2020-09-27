import sqlite3

class User:
    """
    class for USER/Orm functionality
    """
    __tablename__ = 'users'
    def __init__(self, username, password, email):
        """
        """
        self.__username = username 
        self.__password = password
        self.__email = email 

    def __str__(self):
        """
        """
        return "User<name:{} pass:{} email:{}>".format(
            self.__username, self.__password, self.__email
        ) 
    @classmethod
    def check_by_name(cls, username):
        """
        Метод для проверки того, что есть ли в бд КТО-ТО уже с именем username
        """
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_select = 'SELECT * FROM {} WHERE username=?'.format(cls.__tablename__)
        users = list(cur.execute(query_select, (username,)))
        conn.close()
        if len(users) > 0 :
            # как минимум 1 объект с именем username уже есть
            return False 
        return True


    @classmethod 
    def get_all_users(cls):
        """
        Возвращает всех пользователей из бд
        """
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_select = "SELECT * FROM {}".format(cls.__tablename__)
        users = []
        for row  in cur.execute(query_select):
            users.append(cls(row[1], row[2], row[3]))
        conn.close()
        return users 


    def save(self):
        """
        Method for object's saving in database
        """
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_insert = 'INSERT INTO {} VALUES(NULL, ?, ?, ?)'.format(self.__tablename__)
        cur.execute(query_insert, (self.__username, self.__password, self.__email))

        conn.commit()
        conn.close()

    def update_email(self, new_email:str):
        """
        Method for email updating
        """
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_update = 'UPDATE {} SET email=? WHERE username=?'.format(self.__tablename__)
        cur.execute(query_update, (new_email, self.__username))

        conn.commit()
        conn.close()

    def delete(self):
        """
        Метод для удаления объекта из БД
        """
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_delete = 'DELETE FROM {} WHERE username=?'.format(self.__tablename__)
        cur.execute(query_delete, (self.__username, ))

        conn.commit()
        conn.close()

    def my_super_method(self):
        return "Ok"


class NewUser(User):
    pass 


"Relationships" ->
"""
Many to Many
One to Many
Many to One
One to One
"""
