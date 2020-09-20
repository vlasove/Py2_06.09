"""
статики, классовые методы и duck typing
"""

## Классовые методы
class Book:
    books = []

    def __init__(self, new_title:str, new_author:str):
        self.__title = new_title
        self.__author = new_author
        self.__is_read = False 
        self.books.append(self)

    def get_all(self):
        for book in self.books:
            print("Current:", book)


    def read(self):
        if not self.__is_read:
            print("Reading Starting!")
            self.__is_read = True 
        else:
            print("This book already was readed")

    def __str__(self):
        return "Book<Title:{} Author:{}>".format(self.__title, self.__author)

class Journal(Book):
    pass 


b1 = Book("LOTR", "JJ.Talkin") 
b2 = Book("HP:1", "Rawling")
b1.read()
b1.read()

b1.get_all()