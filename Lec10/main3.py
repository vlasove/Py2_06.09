class MySuperClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

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

# Object._<ClassName><Private Method>
ms._MySuperClass__this_is_private()