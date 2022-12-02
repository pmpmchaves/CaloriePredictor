import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open('C:/Users/Pedro/CalorieCounterProject/trained_model.pkl', 'rb'))


def calorie_prediction(user_input):
    # Adjusting our model prediction framework to work with out loaded model
    user_input = (0,27,176,76,25,120,40)
    # Transforming user input data into a numpy array
    user_input_array = np.asarray(user_input)
    # We need to reshape the array so that we can use it in our model
    user_input_reshaped = user_input_array.reshape(1,-1)
    # Calculating prediction based on user input
    user_input_prediction = loaded_model.predict(user_input_reshaped)
    return user_input_prediction


def main():
    # Giving a title
    st.title("Calorie Prediction Web App")
    # Getting the input from the user
    Gender = st.text_input("Gender (M/F)")
    Age = st.number_input("Age in years")
    Height = st.number_input("Height in cm")
    Weight = st.number_input("Weight in kg")
    Duration = st.number_input("Workout Duration in minutes")
    HeartRate = st.number_input("Heart Rate in bpm")
    BodyTemperature = st.number_input("Body Temperature in Celsius")
    # Code for prediction
    prediction = ""
    #Creating a button for prediction
    if st.button("Predict my calories burnt"):
        prediction = calorie_prediction([Gender, Age, Height, Weight, Duration, HeartRate, BodyTemperature])

    st.success(prediction)


if __name__ == "__main__":
    main()
