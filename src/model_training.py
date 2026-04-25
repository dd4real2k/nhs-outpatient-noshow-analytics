import pandas as pd

df = pd.read_csv("data/processed/cleaned_data.csv")

# Select features
features = [
    "age",
    "welfare_support",
    "hypertension",
    "diabetes",
    "alcoholism",
    "disability",
    "sms_received",
    "waiting_days"
]

X = df[features]
y = df["no_show"]

