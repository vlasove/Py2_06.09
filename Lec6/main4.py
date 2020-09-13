class SortedStrings: 
    def __init__(self): 
        self.__strings = [] # набор слов
 
    def AddString(self, new_string : str) -> None: 
        current = new_string.lower() # превращаю в нижний регистр
        self.__strings.append(current) # добавляю очередное слово в коллекцию слов
        self.__strings.sort() # поддерживаю коллекцию в отсортированном виде
 
    def GetSortedStrings(self) -> list: 
        return self.__strings  # возвращаю всегда отсортированный набор слов

#milk, shake, snake, BreakER, GREAT, joBBBB
words = input().split(sep=', ')

ss = SortedStrings()
for word in words:
    ss.AddString(word)
print(" ".join(ss.GetSortedStrings()))