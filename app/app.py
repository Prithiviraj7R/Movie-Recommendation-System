import streamlit as st
from utils import get_movies,get_tmdb_id,get_movie_info
from src.utils import recommender


def main():
    st.title("Home")
    st.write(
        "Welcome to the Movie Recommendation System!"
    )
    movie_titles = get_movies()
    movie = st.selectbox("Select a movie:", movie_titles)
    
    recommendations = recommender(movie)
    tmdb_id_list = get_tmdb_id(recommendations)
    recommended_movies, recommended_movie_posters, movie_descriptions = get_movie_info(tmdb_id_list)

    st.subheader("Recommendations:")
    
    for rec_movie, poster_path, description in zip(recommended_movies, recommended_movie_posters, movie_descriptions):
        st.write(f"**{rec_movie}**")
        st.image(poster_path, caption=rec_movie, use_column_width=False, width=150)
        st.text_area("Overview:", description, height=100)


if __name__ == "__main__":
    main()
    










