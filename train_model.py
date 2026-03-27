import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# 1. Create a simple dataset (Features: Bedrooms, Sq_Ft, Age -> Target: Price)
data = {
    'bedrooms': [3, 4, 3, 5, 2, 4],
    'sq_ft': [2000, 2500, 1800, 3000, 1200, 2800],
    'age': [10, 5, 20, 2, 15, 8],
    'price': [300000, 400000, 250000, 500000, 180000, 450000]
}
df = pd.DataFrame(data)

X = df[['bedrooms', 'sq_ft', 'age']]
y = df['price']

# 2. Train the Multiple Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 3. Save the trained model to a file so our API can use it
joblib.dump(model, 'house_model.pkl')
print(" Model trained successfully and saved as 'house_model.pkl'")