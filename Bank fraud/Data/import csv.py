import csv

# Path to your CSV file
csv_file_path = "JoinedData.csv"

# Column headers from the image
headers = [
    "Customer_Name", "TransactionID", "AccountID", "TransactionAmount",
    "TransactionDate", "TransactionType", "Location", "MerchantID", "Channel",
    "CustomerAge", "CustomerOccupation", "AccountBalance", "fraudlabel", "MerchantCatagory"
]

# Write only the header to the file, clearing all existing data
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

print("CSV file cleared and headers written successfully.")
