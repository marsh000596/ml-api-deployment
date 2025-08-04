#This will show whether it's a LinearRegression, RandomForestClassifier, XGBClassifier, etc.
# might even show target class names if they're stored inside.
import pickle

with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

print(type(model))
print(model)
