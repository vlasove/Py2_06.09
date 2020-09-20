class MySuperClass:
    def __init__(self): 
        """
        В чистом ООП принято, что внутри конструктора определяются все атрибуты класса
        Причем, все атрибуты ПРИВАТИЗИРУЮТСЯ
        """
        self.__a = 1
        self.__b = 2
        self.__c = 3
        self.__d = 4

    def get_a(self):
        """ 
        Для получения значения приватизирвоанного атрибута
        используем метод get()
        """
        return self.__a 

    def set_a(self, new_a:int):
        """
        Для изменения значения приватизированного атрибута 
        используем метод set()
        """
        self.__a = new_a

    def __this_is_private(self):
        """
        Для того чтобы создать полуприватную секцию (атрибут/метод) внутри класса
        необходимо начать название с ДВУХ символов нижнего подчеркивания `__`
        """
        print("This is private method!")

    def this_is_not_private(self):
        """
        Здесь метод __this_is_private можно вызвать
        Так как пользователя НАПРЯМУЮ не обращается к __this_is_private
        """
        print('This is not private!')
        self.__this_is_private()


ms = MySuperClass()
#print("a atr:", ms.__a)