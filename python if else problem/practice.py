import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Example dataset (simplified)
data = {
    "Age": [25, 30, 45, 50, 60],
    "BMI": [22, 28, 31, 29, 35],
    "Glucose": [90, 120, 150, 160, 200],
    "Diabetes": [0, 0, 1, 1, 1]  # 1 = diabetic, 0 = not
}

df = pd.DataFrame(data)

# Features and label
X = df[["Age", "BMI", "Glucose"]]
y = df["Diabetes"]

# Train a model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict for a new patient
new_patient = [[40, 30, 145]]  # Age=40, BMI=30, Glucose=145
prediction = model.predict(new_patient)

print("Prediction:", "Diabetic" if prediction[0] == 1 else "Not Diabetic")
