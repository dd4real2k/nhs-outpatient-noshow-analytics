-- Create cleaned table
SELECT
    PatientId AS patient_id,
    AppointmentID AS appointment_id,
    LOWER(Gender) AS gender,

    CAST(ScheduledDay AS DATE) AS scheduled_day,
    CAST(AppointmentDay AS DATE) AS appointment_day,

    Age AS age,
    LOWER(Neighbourhood) AS neighbourhood,

    Scholarship AS welfare_support,
    Hipertension AS hypertension,
    Diabetes AS diabetes,
    Alcoholism AS alcoholism,
    Handcap AS disability,
    SMS_received AS sms_received,

    CASE
        WHEN "No-show" = 'Yes' THEN 1
        ELSE 0
    END AS no_show,

    -- New Feature: Days between scheduling and appointment
    DATEDIFF(AppointmentDay, ScheduledDay) AS waiting_days

FROM raw_appointments

WHERE Age >= 0
