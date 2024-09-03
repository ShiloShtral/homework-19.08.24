import random
from os import remove

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}

dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}

avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
                   "Chris Hemsworth", "Jeremy Renner"}

iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}

legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}

actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}

movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}


oscar_winners.add("Emma Watson")
print(oscar_winners)

#################################################

oscar_winners.clear()
print(oscar_winners)

#################################################

oscar_winners.copy()
print(oscar_winners.copy())

#################################################

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
oscar_winners.remove("Meryl Streep")
print(f"Oscar winners after removing Meryl Streep {oscar_winners}")

#################################################

common_actors = titanic_actors & dark_knight_actors
print(common_actors)

common_actors = set()
for i in titanic_actors:
    if i in dark_knight_actors:
        common_actors.add(i)
print(common_actors)

##################################################
common_iron_man_avangers = set()
for i in  iron_man_actors:
    if i in avengers_actors:
        common_iron_man_avangers.add(i)
print(common_iron_man_avangers)

##################################################
all_won_oscar = all(actor in oscar_winners for actor in actor_list)
print(all_won_oscar)

##################################################

all_actor_avangers = all(actor in actor_list for actor in avengers_actors)
print(all_actor_avangers)

##################################################

movie_cast.pop()
print(movie_cast)

##################################################

movie_cast.discard("Matt Damon")
print(movie_cast)

##################################################

not_won_oscar_titanic = titanic_actors - oscar_winners
print(not_won_oscar_titanic)

##################################################

not_common_titanic_dark_night = titanic_actors.symmetric_difference(dark_knight_actors)
print(not_common_titanic_dark_night)

##################################################

oscar_winners.update({"Cate Blanchett", "Daniel Lewis-Day"})
print(oscar_winners)

##################################################

titanic_plus_dark_knight_actors = titanic_actors.union(dark_knight_actors)
print(titanic_plus_dark_knight_actors)

##################################################

dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",
"Tom Hardy", "Joseph Gordon-Levitt"}

dark_knight_rises_and_dark_knight = dark_knight_rises_actors >= dark_knight_actors
print(dark_knight_rises_and_dark_knight)

##################################################

legendary_oscar_winners_actors = legendary_actors >= oscar_winners
print(legendary_oscar_winners_actors)

##################################################

avengers_iron_man_uncommon_actors = avengers_actors - iron_man_actors
print(avengers_iron_man_uncommon_actors)

##################################################

dark_knight_avangers_uncommon_actors = dark_knight_actors ^ avengers_actors
print(dark_knight_avangers_uncommon_actors)

##################################################

dark_knight_iron_man_common_actors = (dark_knight_actors | iron_man_actors)
print(dark_knight_iron_man_common_actors)

##################################################

legendary_actors_frozenset = frozenset(legendary_actors)
print(legendary_actors_frozenset)

##################################################

#מדוע לדעתך אין להשתמש במיקום לפי אינדקס ב- set
# מכיוון שset מבוסס על אוסף לא מסודר כלומר הפריטים אינם מסודריפ בסדר קבוע או במקום קבוע

#כיצד set ו - dict דומים? )רמז חשוב על ה- key )
#הם דומים מכיוון שלשניהם יש פקודות ייחויות רק להם (keys) ואפשר להוסיף ולהסיר פריטים
###################################################

numbers_set = {x for x in range(1, 101)}
print(numbers_set)

###################################################

random_numbers = [random.randint(100, 500) for _ in range(50)]

unique_numbers_count = len(set(random_numbers))

print("List of random numbers:", random_numbers)
print("Number of unique numbers:", unique_numbers_count)







