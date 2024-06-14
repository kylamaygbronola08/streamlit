import streamlit as st


st.header('Sentiment Analyzer Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code('''
       import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names


# Set up the title and description
st.title("Decoding Your Feelings ")
st.markdown("""
Hey there!This is Broñola's app that can analyze your feelings.  Just tell it how you're feeling in the box below, and it will use data analysis to figure out what's going on!
""")

# Input field for user to enter their feeling
message = st.text_input("Tell me what you feel today: ")

# Load the pre-trained sentiment analysis model
filename = '/pages/KMBRONOLA_SentimentAnalyzer_Model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def word_features(words):
    return dict([(word, True) for word in words])
# Function to extract features from the message


def sayFeeling():

        if message_tone == 'happy_features':
            st.write("You are feeling happy.")
        elif message_tone == 'scared_features':
            st.write("You are feeling scared.")
        elif message_tone == 'angry_features':
            st.write("You are feeling angry.")
        elif message_tone == 'nervous_features':
            st.write("You are feeling nervous.")
        else:
            st.write("You are feeling disappointed.")

# Button to trigger the sayFeeling function

st.button('Say it', on_click=sayFeeling)
message_tone = loaded_model.classify(word_features(message.split()))

    ''')