import streamlit as st


st.header('Prediction Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
 # Notes
# do a "pip install streamlit" first 
# to run on terminal issue this command
# python -m streamlit run streamlit_test.py


import streamlit as st
import pickle
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import apply_features

# Load the trained Naive Bayes classifier from the saved file
filename = '/content/dengue1.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("🦟 Dengue Cases Predictor 🦟")
st.subheader("Enter levels of different factors to predict the likelihood of Dengue:")

# User inputs for different factors
mosquito_population_input = st.slider("Mosquito Population (per sq km): ", 0, 100)
temperature_input = st.slider("Temperature (°C): ", 0, 40)
humidity_input = st.slider("Humidity (%): ", 0, 100)
rainfall_input = st.slider("Rainfall (mm): ", 0, 500)

# Function to make a prediction
def predict_dengue_likelihood(mosquito_population, temperature, humidity, rainfall):
    # Features function to convert inputs into a dictionary format expected by NLTK NaiveBayesClassifier
    def features(mosquito_population, temperature, humidity, rainfall):
        return {
            'mosquito_population': mosquito_population,
            'temperature': temperature,
            'humidity': humidity,
            'rainfall': rainfall
        }

    # Apply features function to user inputs
    test_data = features(mosquito_population, temperature, humidity, rainfall)

    # Use NLTK's classify method to get the classification label
    prediction = loaded_model.classify(test_data)
    return prediction

# Display button and result
if st.button('Predict'):
    likelihood = predict_dengue_likelihood(mosquito_population_input, temperature_input, humidity_input, rainfall_input)
    st.text("The predicted likelihood of Dengue based on the given factors is:")
    st.text_area(label="", value=str(likelihood), height=100)

''')