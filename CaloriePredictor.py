import numpy as np
import pickle
from xgboost import XGBRegressor

## Different options to load the model:
# Option 1: Loading the saved model as json file
#loaded_model = XGBRegressor()
#loaded_model.load_model('/mnt/c/Users/Pedro/CalorieCounterProject/CaloriePredictor-main/trained_model1.json')
# Option 2: Loading the saved j.sav model
#import joblib
#loaded_model = joblib.load("/mnt/c/Users/Pedro/CalorieCounterProject/CaloriePredictor-main/trained_model2.sav")


# Option 3: Loading the saved pickle model
loaded_model = pickle.load(open('/mnt/c/Users/Pedro/CalorieCounterProject/CaloriePredictor-main/trained_model.pkl', 'rb'))

# Adjusting our model prediction framework to work with out loaded model
user_input = (0,27,176,76,25,120,40)

# Transforming user input data into a numpy array
user_input_array = np.asarray(user_input)

# We need to reshape the array so that we can use it in our model
user_input_reshaped = user_input_array.reshape(1,-1)

# Calculating prediction based on user input
user_input_prediction = loaded_model.predict(user_input_reshaped)

print(user_input_prediction)
