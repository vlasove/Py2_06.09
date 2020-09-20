"""
Решение задачи B /D2
"""

class Queue:
    """
    Класс для имитации жизни очереди
    """
    def __init__(self):
        self.peoples = []

    def add_to_head(self, message:str):
        """
        Достать из message человека
        и поместить в начало очереди
        """
        #message = "Я только спросить! Я - Иванова."
        messages = message.split(' - ') #['Я только спросить! Я', 'Иванова.']
        lastname = messages[-1].split('.')[0] #['Иванова',''][0]
        self.peoples.insert(0, lastname)

    def add_to_tail(self, message:str):
        """
        Достать из message человека
        и поместить в начало очереди
        """
        #message = "Кто последний? Я - Кузнецов."
        messages = message.split(' - ') #['Кто последний? Я', 'Кузнецов.']
        lastname = messages[-1].split('.')[0] #['Кузнецов',''][0]
        self.peoples.append( lastname)
    
    def __analyze(self):
        """
        Возвращает True если в очереди кто-то есть
        False в противном случае.
        """
        if len(self.peoples) > 0:
            return True 
        return False 
    def get_answer(self):
        """ 
        Отдает ответ на задачу
        В случае, если в self.people никого нет - возвращает "В очереди никого нет"
        В случае, если в self.poeple кто-то есть - отдает последнего
        По сути работает как реакция на "Следующий!
        """
        if self.__analyze():
            return "Заходит {}!".format(self.peoples.pop(0))
        return "В очереди никого нет"


queue = Queue()
n = int(input()) # Количество команд
for _ in range(n):
    command = input().strip() # "Кто последний? Я - Кузнецов.\n"
    if "Я только спросить" in command:
        queue.add_to_head(command)
    elif "Кто последний" in command:
        queue.add_to_tail(command)
    else:
        print(queue.get_answer())




