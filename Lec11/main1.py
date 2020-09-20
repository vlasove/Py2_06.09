class Book:
    books = []
    def __init__(self, new_title:str, new_author:str):
        self.__title = new_title
        self.__author = new_author
        self.__is_read = False 
        self.books.append(self)

    @classmethod 
    def find_and_change_author(cls, title, author):
        return cls(title, author) 


class Journal(Book):
    pass 
b = Book("A", "b")
j = Journal("B", "c")

print("b type:", type(b))
print("j type:", type(j))

NEW_B = Book.find_and_change_author("A", "BBBBBBB")
NEW_J = Journal.find_and_change_author("B", "JJJJJJJJJJ")


print("NEW B type:", type(NEW_B))
print("NEW J type:", type(NEW_J))