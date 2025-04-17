import pandas as pd
import random

# Load your CSV file
df = pd.read_csv("bank_transactions_data_2.csv")  # Replace with your actual filename

# Add a new column 'fraudlabel' with random 0 or 1
df["fraudlabel"] = [random.randint(0, 1) for _ in range(len(df))]

# Save the updated DataFrame back to CSV
df.to_csv("your_file_with_fraudlabel.csv", index=False)
