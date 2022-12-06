import numpy as np
import pickle
import streamlit as st
import datetime
from datetime import date
from PIL import Image

# Loading the saved model
loaded_model = pickle.load(open('/mnt/c/Users/Pedro/CalorieCounterProject/CaloriePredictor-main/trained_model.pkl', 'rb'))


def calorie_prediction(user_input):

    # Transforming user input data into a numpy array
    user_input_array = np.asarray(user_input)

    # We need to reshape the array so that we can use it in our model
    user_input_reshaped = user_input_array.reshape(1,-1)

    # Calculating prediction based on user input
    user_input_prediction = loaded_model.predict(user_input_reshaped)

    return user_input_prediction


def main():

    image = Image.open('/mnt/c/Users/Pedro/CalorieCounterProject/CaloriePredictor-main/Woman_Running.jpg')
    new_image = image.resize((500, 320))
    st.image(new_image, use_column_width=False)

    # Giving a title
    st.title("Calorie Prediction Web App")

    # Getting the inputs from the user
    Gender = st.selectbox('Select your gender at birth', ["Male","Female"])
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1

    Age_input = st.date_input("Type your Birthday",min_value=datetime.date(1930, 1, 1),max_value=date.today())
    today = date.today()
    Age = float((today - Age_input)/datetime.timedelta(days=365))

    Height = st.number_input("Type your Height in cm")
    Weight = st.number_input("Type your Weight in kg")
    Duration = st.slider('Select your Workout Duration in minutes', 1, 90, 1)
    HeartRate = st.slider("Select your average Heart Rate in beats per minute",50, 190, 1)
    BodyTemperature = st.number_input("Body Temperature in Celsius")

    # Code for prediction
    prediction = ""

    # Creating a button for prediction
    if st.button("Predict how many calories I burnt"):
        prediction = round(float(calorie_prediction([Gender, Age, Height, Weight, Duration, HeartRate, BodyTemperature])[0]),2)
        st.success(f"You burnt {prediction} calories in this workout session!", icon="✅")



if __name__ == "__main__":
    main()
