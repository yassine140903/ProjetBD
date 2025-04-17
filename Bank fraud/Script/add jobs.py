import pandas as pd
import random

# Load your CSV file
df = pd.read_csv("Bank_Transaction_Fraud_Detection.csv")  # Replace with your actual file path

# List of possible jobs
jobs = ['engineer', 'student', 'doctor', 'retired']

# Add a new column 'job' with random job values
df["job"] = [random.choice(jobs) for _ in range(len(df))]

# Save the updated DataFrame back to CSV
df.to_csv("your_file_with_jobs.csv", index=False)
