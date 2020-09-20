class Radio:
    def __init__(self):
        # Эти атрибуты безболезненно могут редактироваться пользователем
        self.knob_sound = 0
        self.knob_waving = 0
        self.turn_on = False 
        self.turn_off = True 
        # Эти атрибуты ОКАЗЫВАЮТ КРИТИЧЕСКОЕ ВОЗДЕЙСТВИЕ НА РАБОТОСПОСОБНОСТЬ
        # ОБЪЕКТОВ КЛАССА Radio
        self.__whos_made = "China"
        self.__total_R = 2500
        self.__total_Q = 0.02
        self.__counter_length = 12.5
        self.__capacity_N = 250 
