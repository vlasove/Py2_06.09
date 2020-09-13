# Создадим функцию, которая будет красиво печатать представителей Film()
# Структура - заименованыый набор полей
class Film:
    title = ""
    duration = 0
    rating = 0.0
    actors = []
    year = -1

def print_film(f :Film):
    print("=========================FILM===============")
    print("Title:", f.title)
    print("Rating:", f.rating)
    print("////////Actors///////")
    for actor in f.actors:
        print(actor)
    print("//////////////////")
    print("===========================================")


f1 = Film()
#print("F1:", type(f1))
#print("f1 title(before):", f1.title)
f1.title = "HP:1"
#print("f1 title(after):", f1.title)
f1.duration = 240
f1.rating = 10.0
f1.actors = ["x", "y", "z"]
f1.year = 2001

print_film(f1)
