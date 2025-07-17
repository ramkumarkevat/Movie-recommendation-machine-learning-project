import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommender System")

# Load pickled data
movies = pickle.load(open('movie_list.pkl', 'rb'))  # This is the DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))  # This is a similarity matrix

movie_list = movies['title'].values  # Dropdown options


# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:  # Top 5 (excluding the same movie)
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Dropdown for user selection
select_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movie_list
)

# Button to get recommendations
if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i)
