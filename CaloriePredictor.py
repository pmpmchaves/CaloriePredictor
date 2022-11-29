# Importing the Dependencies
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

# Data Collection and Processing
calories_df = pd.read_csv("/calories.csv")
calories_df.head()
exercise_df = pd.read_csv("/exercise.csv")
exercise_df.head()
df = pd.concat([exercise_df,calories_df["Calories"]],axis=1)
df.head()
df.shape # (15000, 9)
df.info()
df.isnull().sum() # There are 0 columns with null values

