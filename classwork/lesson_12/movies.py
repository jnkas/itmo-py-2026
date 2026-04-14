movies = [
    {"title": "Inception", "rating": 8.8, "year": 2010},
    {"title": "Interstellar", "rating": 8.8, "year": 2014},
    {"title": "The Matrix", "rating": 8.7, "year": 1999},
    {"title": "Tenet", "rating": 7.3, "year": 2020},
    {"title": "Memento", "rating": 8.4, "year": 2000},
    {"title": "Dunkirk", "rating": 7.8, "year": 2017},
    {"title": "The Prestige", "rating": 8.5, "year": 2006},
    {"title": "Batman Begins", "rating": 8.2, "year": 2005},
    {"title": "Oppenheimer", "rating": 8.7, "year": 2023},
]

# рейтинг выше 8
def filter_by_raiting(raiting):
    res = []

    res = list(filter(lambda mv: mv["rating"] >= raiting, movies))
    return res

r8 = filter_by_raiting(8)
print(r8)

def sort_movies(mode):

    res = []

    if mode == 1:
        #по Алфавиту
        # res = sorted(movies, key = lambda item: item["title"]) 
        res = sorted(movies, key = lambda item: item["year"])   



    #отсортировать по Алфавиту, Рейтингу, году
    return res



print(sort_movies(1))