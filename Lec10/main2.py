# Инкапсуляция - свойство объекта, сохранять целостность и защищать критически важные
# параметры от непредвиденного пользовательского изменения.

# .cpp
# class MySuperClass {
#     public:
#         int a = 1;
#         int b = 2;

#     private:
#         int c = 3;
#         int d = 4;
# }

# ///
#     auto ms = MySuperClass()
#     ms.a + ms.b + ms.c + ms.d


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
print("atr a:", ms.a)
print("atr b:", ms.b)
print("atr c:", ms.c)
print("atr d:", ms.d)
ms.this_is_not_private()