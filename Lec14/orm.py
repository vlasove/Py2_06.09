"""
ORM - Object-Relational Mapping
"""
import sqlite3 

class Book:
    __tablename__ = 'books'
    def __init__(self, _id:int, author:str, title:str, year:int, rating:float):
        self.__id = _id 
        self.__author = author 
        self.__title = title 
        self.__year = year 
        self.__rating = rating

    def insert(self):
        """
        Метод для сохранения объекта в БД
        """
        pass 

    def delete(self):
        pass 

    def update_year(self, year):
        pass 

    def read_info(self):
        pass 


"""
CRUD --- Create Read Update Delete
"""