# NHS Outpatient Appointment No-Show Prediction & Capacity Analytics

## Project Overview
This project predicts the likelihood of patients missing outpatient appointments using healthcare appointment data. The aim is to support NHS-style capacity planning, reduce missed appointments, improve clinic utilisation, and support better patient access to care.

## Problem Statement
Missed outpatient appointments create wasted clinical time, longer waiting lists, reduced service efficiency, and delays in patient care. This project uses data analytics and machine learning to identify patterns linked to non-attendance and predict patients at risk of missing appointments.

## Objectives
- Clean and prepare outpatient appointment data using SQL
- Analyse trends in attendance and missed appointments
- Identify key factors linked to appointment no-shows
- Build a machine learning model to predict no-show risk
- Create a Power BI dashboard for operational insights
- Deploy a Streamlit app for simple no-show prediction

## Tools Used
- SQL
- Python
- Pandas
- Scikit-learn
- Power BI
- Streamlit
- Matplotlib
- Seaborn

## Business Impact
This project can help healthcare teams:
- Reduce missed appointments
- Improve clinic scheduling
- Support better staff and resource planning
- Improve patient follow-up
- Reduce pressure on waiting lists

By identifying patients at higher risk of missing appointments, healthcare teams can prioritise reminder calls, improve clinic utilisation, reduce wasted appointment slots, and support better outpatient capacity planning.

## Data Cleaning

Data cleaning was performed using SQL-style transformations and Python.

Key steps:
- Renamed columns for clarity
- Converted date columns to proper datetime format
- Created binary target variable (`no_show`)
- Engineered new feature: `waiting_days`
- Removed invalid records (negative age, invalid dates)

## Exploratory Data Analysis

Key insights:

- A significant proportion of patients miss appointments, impacting healthcare efficiency
- Longer waiting times are associated with higher no-show rates
- Patients who did not receive SMS reminders are more likely to miss appointments
- Certain locations show higher non-attendance patterns

These insights highlight opportunities for improving appointment management and patient engagement.

## Machine Learning Model

A machine learning model was developed to predict whether a patient is likely to miss an outpatient appointment.

Two models were tested:

- Logistic Regression
- Random Forest Classifier

The Random Forest model was selected because it can capture non-linear relationships between appointment factors and no-show behaviour.

## Model Features

The model used the following features:

- Gender
- Age
- Neighbourhood
- Welfare support status
- Hypertension
- Diabetes
- Alcoholism
- Disability
- SMS reminder status
- Waiting days between booking and appointment

## Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Recall is particularly important in this project because the aim is to identify patients at higher risk of missing appointments.

## Project Status
In progress.
