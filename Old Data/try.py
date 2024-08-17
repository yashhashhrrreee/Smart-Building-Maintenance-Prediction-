import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


df = pd.read_csv('data_no_outliers.csv')

positive_features = ['co2', 'light', 'pir']

df['co2'] = np.log(df['co2'])

def detect_outliers_z_score(data):
    threshold = 3
    z_scores = (data - data.mean()) / data.std()
    return np.abs(z_scores) > threshold

outliers = detect_outliers_z_score(df[positive_features])
df_cleaned = df[~outliers.any(axis=1)]


X = df_cleaned[positive_features]
y = df_cleaned['temperature']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)
