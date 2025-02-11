# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def highly_rated(movie):
    return movie["imdb"] > 5.5


def high_rated_movies(movies):
    return [movie for movie in movies if highly_rated(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies) if movies else 0

def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)

movie_example = {"name": "We Two",
"imdb": 7.2,
"category": "Romance"}
print(highly_rated(movie_example))

top_movies = high_rated_movies(movies)
print(top_movies)

category = "Crime"
crime = movies_by_category(movies, category)
print(crime)

avg_imdb_score = average_imdb(movies)
print(avg_imdb_score)

avg_cat_score = average_imdb_by_category(movies, category)
print(avg_cat_score)