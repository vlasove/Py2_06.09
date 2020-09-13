# Структура - заименованыый набор полей
class Film:
    title = ""
    duration = 0
    rating = 0.0
    actors = []
    year = -1


f1 = Film()
#print("F1:", type(f1))
print("f1 title(before):", f1.title)
f1.title = "HP:1"
print("f1 title(after):", f1.title)
f1.duration = 240
f1.rating = 10.0
f1.actors = ["x", "y", "z"]
f1.year = 2001

f2 = Film()
print("f2 title(before):", f2.title)
f2.title = "LOTR:1"
print("f2 title(after):", f2.title)
f2.duration = 300
f2.rating = 10.0 
f2.year = 2002
f2.actors = ["a", "b", "c"]

films = [f1, f2]

for film in films:
    print("Title:", film.title, "Rating:", film.rating)



