# Утиная типизация (duck typing)

class Auto:
    """
    здесь может находиться неограниченное количество дополнительные атрибутов/методов
    """
    def beep(self):
        print("BEEP-BEEP")

class Bike:
    def beep(self):
        print("beep-beep")

class RadioAuto:
    def beep(self):
        print('bp-bp')


# В другом модуле существует такая функция:
def make_sound(sound_gen):
    sound_gen.beep()
    print("Type of sound_gen is :", type(sound_gen))

make_sound(Auto())
make_sound(Bike())
make_sound(RadioAuto())
