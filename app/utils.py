import os
import pandas as pd
import requests
from src.utils import load_file

def get_poster(tmdb_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=46f8adb9d779c9609315eaec82c0eb9a&language=en-US".format(tmdb_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_poster_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    original_title = data['original_title']
    movie_overview = data['overview']

    return original_title, full_poster_path, movie_overview

def get_movies():
    user_item = load_file(os.path.join('artifacts','user_item.pkl'))
    return list(user_item.index)

def get_tmdb_id(movie_names): 
    movies_df = pd.read_csv(os.path.join('artifacts','movies.csv'))
    movie_id_list = movies_df[movies_df['title'].isin(movie_names)]['movieId'].to_list()
    
    links = pd.read_csv(os.path.join('artifacts','links.csv'))
    tmdb_id_list = links[links['movieId'].isin(movie_id_list)]['tmdbId'].to_list()

    return tmdb_id_list

def get_movie_info(tmdb_id_list):
    movie_posters = []
    movie_names = []
    movie_info = []

    for recommended_movie_id in tmdb_id_list:
        movie_name, movie_poster, movie_overview = get_poster(recommended_movie_id)
        movie_posters.append(movie_poster)
        movie_names.append(movie_name)
        movie_info.append(movie_overview)

    return movie_names, movie_posters, movie_info
