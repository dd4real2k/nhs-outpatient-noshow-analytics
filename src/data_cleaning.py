import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Rename columns
    df = df.rename(columns={
        "PatientId": "patient_id",
        "AppointmentID": "appointment_id",
        "Gender": "gender",
        "ScheduledDay": "scheduled_day",
        "AppointmentDay": "appointment_day",
        "Age": "age",
        "Neighbourhood": "neighbourhood",
        "Scholarship": "welfare_support",
        "Hipertension": "hypertension",
        "Handcap": "disability",
        "SMS_received": "sms_received",
        "No-show": "no_show"
    })

    # Convert dates
    df["scheduled_day"] = pd.to_datetime(df["scheduled_day"])
    df["appointment_day"] = pd.to_datetime(df["appointment_day"])

    # Create target variable
    df["no_show"] = df["no_show"].map({"Yes": 1, "No": 0})

    # Feature engineering
    df["waiting_days"] = (df["appointment_day"] - df["scheduled_day"]).dt.days

    # Clean invalid data
    df = df[df["age"] >= 0]
    df = df[df["waiting_days"] >= 0]

    return df

def save_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = load_data("data/raw/noshowappointments.csv")
    df_clean = clean_data(df)
    save_data(df_clean, "data/processed/cleaned_data.csv")
