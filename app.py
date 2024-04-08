import streamlit as st # type: ignore
import pickle
import time

st.title("Sentimental Analysis on Social Media Platform")

# load model 
model = pickle.load(open('Social_media_sentiment.pkl','rb'))

tweet = st.text_input("Enter your text ")

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write("Prediction time taken:", round(end-start, 2), 'seconds')
    print(prediction[0])
    st.write("Predicted Sentiment is:",prediction[0])
