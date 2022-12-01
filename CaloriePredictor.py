from ensurepip import version
import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open('Users/Pedro/OneDrive/Ambiente de Trabalho/CalorieCounterProject/trained_model.pkl', 'rb'))

# Adjusting our model prediction framework to work with out loaded model
user_input = (0,27,176,76,25,120,40)

# Transforming user input data into a numpy array
user_input_array = np.asarray(user_input)


# We need to reshape the array so that we can use it in our model
user_input_reshaped = user_input_array.reshape(1,-1)

# Calculating prediction based on user input
user_input_prediction = loaded_model.predict(user_input_reshaped)


print(user_input_prediction)
