import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset (House Size vs Price)
data = {
    "Size (sq ft)": [500, 750, 1000, 1250, 1500],
    "Price ($)": [150000, 200000, 250000, 300000, 350000]
}

# Create DataFrame
df = pd.DataFrame(data)
print("✅ Dataset:\n", df)

# Features (X) and Labels (y)
X = df[["Size (sq ft)"]]   # independent variable
y = df["Price ($)"]        # dependent variable

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new house
predicted_price = model.predict([[1800]])
print(f"\nPredicted price for 1800 sq ft house: ${predicted_price[0]:.2f}")

# Plotting
plt.scatter(X, y, color="blue", label="Data Points")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price ($)")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()
