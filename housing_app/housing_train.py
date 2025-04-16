import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle

# Load dataset
df = pd.read_csv(
    "/Users/suchanatratanarueangrong/KMUTT/Year 3 Semester 2/MLOps/Lab10/mldeployment-cpe393/Housing.csv"
)

# Preprocessing: Convert categorical columns to numeric (e.g., "mainroad", "guestroom")
df["mainroad"] = df["mainroad"].map({"yes": 1, "no": 0})
df["guestroom"] = df["guestroom"].map({"yes": 1, "no": 0})
df["basement"] = df["basement"].map({"yes": 1, "no": 0})
df["hotwaterheating"] = df["hotwaterheating"].map({"yes": 1, "no": 0})
df["airconditioning"] = df["airconditioning"].map({"yes": 1, "no": 0})
df["prefarea"] = df["prefarea"].map({"yes": 1, "no": 0})
df["furnishingstatus"] = df["furnishingstatus"].map(
    {"furnished": 1, "unfurnished": 0, "semi-furnished": 2}
)

# Define features and target
X = df.drop("price", axis=1)
y = df["price"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the model to a file using pickle
with open("model_house.pkl", "wb") as f:
    pickle.dump(model, f)
