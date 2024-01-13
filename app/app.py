import streamlit as st
from utils import get_movies,get_tmdb_id,get_movie_info
from src.utils import recommender


def main():
    st.title("Movie Recommendation System")
    st.write(
        "Choose a movie to get recommendations based on collaborative filtering which"
        "recommends movie based on movies liked by users who watched this movie."
    )
    movie_titles = get_movies()
    movie = st.selectbox("Select a movie:", movie_titles)

    explore_button = st.button("Explore!")
    
    if explore_button:
        recommendations = recommender(movie)
        tmdb_id_list = get_tmdb_id(recommendations)
        recommended_movies, recommended_movie_posters, movie_descriptions = get_movie_info(tmdb_id_list)

        st.subheader("Users who watched {} also liked:".format(movie))

        for rec_movie, poster_path, description in zip(recommended_movies, recommended_movie_posters, movie_descriptions):
            st.write(f"**{rec_movie}**")
            st.image(poster_path, caption=rec_movie, use_column_width=False, width=150)
            st.text_area("Overview:", description, height=100)

if __name__ == "__main__":
    main()
    










