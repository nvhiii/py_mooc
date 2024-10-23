# Please write a function named sort_by_seasons(items: list) which takes a list of dictionaries as its argument. Each dictionary contains the information of a single TV show. The function should sort this list by the number of seasons each show has, in ascending order. The function should not change the original list, but return a new list instead.

# The function should work as follows:

# shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

# for show in sort_by_seasons(shows):
#     print(f"{show['name']} {show['seasons']} seasons")

# Dexter 9 seasons
# Friends 10 seasons
# Simpsons 32 seasons

def sort_by_seasons(items: list):

    def num_seasons(show: tuple):
        return show["seasons"]
    
    return sorted(items, key=num_seasons)