import pandas as pd
import random

# Load the CSV file
df = pd.read_csv("bank_transactions_data_2.csv")

# Sample first and last names
first_names = ["Alice", "John", "Maria", "Tom", "Linda", "James", "Emily", "David", "Sophia", "Michael"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Davis", "Miller", "Wilson", "Taylor"]

# Function to generate a random full name
def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Create the new column
df["Customer_Name"] = [generate_name() for _ in range(len(df))]

# Save to a new CSV file
df.to_csv("bank_transactions_data_2_with_names.csv", index=False)

print("Customer_Name column added and file saved as 'bank_transactions_data_2_with_names.csv'")
