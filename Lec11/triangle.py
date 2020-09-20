"""
пример статика
"""
class Triangle:
    def __init__(self, a_int:int, b_int:int, c_int:int):
        self.__a = a_int
        self.__b = b_int 
        self.__c = c_int 

    def perimeter(self):
        return self.__a + self.__b + self.__c 

    def area(self):
        """
        Это ошибочная формула. Исправить на формулу Герона
        """
        return self.__a * self.__b * self.__c 

    @staticmethod
    def figure_logger():
        file_name = "file.txt"
        print("log for this file is on:", file_name)
        with open(file_name, "w") as fhand:
            fhand.write(".....")
