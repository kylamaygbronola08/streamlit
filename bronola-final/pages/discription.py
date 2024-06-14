import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Simple Sentiment Analyzer App')
st.image("./pictures/emotionanalyzer.png")

with st.expander("🔮Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
An emotion analyzer, driven by machine learning, interprets human emotions exclusively from text inputs. By analyzing linguistic patterns, it categorizes emotions like happiness, sadness, anger, dissapointment or fear, thereby deepening our comprehension of emotional nuances in written communication. 
             If you input your feelings, it will automatically analyze them. For example, "Rain falls quietly, regret blending with each drop," might indicate that you are feeling disappointed.


                
    """, unsafe_allow_html=True)

st.header('𓍢ִImage Classification')
st.image("pictures/imageclassifier.png")

with st.expander("Flower Image Classification Project"):
    st.markdown("""
    
    #
                Image Classification
    My image classification project focuses on accurately identifying different types of butterflies and moths, specifically the Cabbage White, Blue Spotted Crow, Brookes Birdwing, Brown Argus, and Brown Siproeta. 
                The project aims to utilize machine learning techniques to analyze and classify images of butterflies and moths based on distinctive features. 
                It uses a large dataset with hundred  of labeled images of butterflies and moths, ensuring a wide variety of examples to train and test the model effectively.

                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./pictures/predict1.png")
st.image("./pictures/predict2.png")

with st.expander("Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
Dengue Outbreak Predictor is a vital tool for predicting the chances of Dengue outbreaks based on important environmental factors. Dengue, which spreads mainly through Aedes mosquitoes, thrives in warm, humid areas. 
                In my app, users can enter data such as mosquito numbers, temperature, humidity, and rainfall levels using easy sliders. The app uses an advanced Naive Bayes classifier trained on past data to quickly estimate the likelihood of Dengue outbreaks. This predictive tool helps health officials, researchers, and communities plan ahead for mosquito control and public health actions, potentially reducing Dengue outbreaks.
                
    """, unsafe_allow_html=True)