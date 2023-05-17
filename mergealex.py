import json
import pandas as pd

#Ler e Normalizar Filmes
filename_movies = r'movies.json'
with open(filename_movies, 'r') as file:
    data = json.load(file)

movie_data = [movie['data']['movie'] for movie in data.values()]

flat_data_movies = pd.json_normalize(movie_data)

flat_data_movies.head()



filename_movies = r'albums.json'
with open(filename_albums, 'r') as file:
    data = json.load(file)

album_data = [movie['data']['album'] for album in data.values()]

flat_data_albums = pd.json_normalize(album_data)

flat_data_albums.head()