# Но мы до сих пор не храним фильмы.

titles = ["HP:1" , "LOTR:1"]
durations = [240, 300]
ratings = [10.0, 10.0]
actors = [["Ron", "Hermione", "Harry"], ["x", "y", "z"]]
years = [2001, 2002]

for i in range(0, 2):
    print(i, "th film info:", titles[i], durations[i], actors[i])

