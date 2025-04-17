import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Constants
NUM_CUSTOMERS = 400
NUM_TRANSACTIONS = 20000
ACCOUNT_TYPES = ['Checking', 'Savings', 'Credit']
TRANSACTION_TYPES = ['Online', 'In-Store', 'Mobile App']
MERCHANT_CATEGORIES = ['Grocery', 'Electronics', 'Clothing', 'Restaurant', 'Travel', 'Health']
DEVICE_TYPES = ['Mobile', 'Desktop', 'Tablet', 'ATM']
CURRENCIES = ['USD', 'EUR', 'GBP']
STATES = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
BANK_BRANCHES = ['North', 'South', 'East', 'West', 'Central']

# Generate 400 customers
customers = []
for i in range(NUM_CUSTOMERS):
    customer_id = f"CUST{1000 + i}"
    name = fake.name()
    gender = random.choice(['Male', 'Female'])
    age = random.randint(18, 80)
    state = random.choice(STATES)
    city = fake.city()
    branch = random.choice(BANK_BRANCHES)
    acc_type = random.choice(ACCOUNT_TYPES)
    email = fake.email()
    contact = fake.phone_number()
    job = fake.job()
    customers.append({
        'Customer_ID': customer_id,
        'Customer_Name': name,
        'Gender': gender,
        'Age': age,
        'State': state,
        'City': city,
        'Bank_Branch': branch,
        'Account_Type': acc_type,
        'Customer_Email': email,
        'Customer_Contact': contact,
        'Job': job
    })

# Generate transactions
rows = []
for i in range(NUM_TRANSACTIONS):
    cust = random.choice(customers)
    transaction_id = f"TXN{100000 + i}"
    txn_date = fake.date_between(start_date='-2y', end_date='today').strftime('%d/%m/%Y')
    txn_time = fake.time()
    txn_amount = round(random.uniform(5.0, 5000.0), 2)
    merchant_id = f"M{random.randint(10000, 99999)}"
    txn_type = random.choice(TRANSACTION_TYPES)
    category = random.choice(MERCHANT_CATEGORIES)
    balance = round(random.uniform(100.0, 100000.0), 2)
    device = random.choice(DEVICE_TYPES)
    location = fake.city()
    is_fraud = random.choices([0, 1], weights=[97, 3])[0]  # 3% fraud rate
    currency = random.choice(CURRENCIES)
    description = fake.sentence()

    rows.append([
        cust['Customer_ID'],
        cust['Customer_Name'],
        cust['Gender'],
        cust['Age'],
        cust['State'],
        cust['City'],
        cust['Bank_Branch'],
        cust['Account_Type'],
        transaction_id,
        txn_date,
        txn_time,
        txn_amount,
        merchant_id,
        txn_type,
        category,
        balance,
        device,
        location,
        device,
        is_fraud,
        currency,
        cust['Customer_Contact'],
        description,
        cust['Customer_Email'],
        cust['Job']
    ])

# Write to CSV
with open('transactions_powerbi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Customer_ID', 'Customer_Name', 'Gender', 'Age', 'State', 'City',
        'Bank_Branch', 'Account_Type', 'Transaction_ID', 'Transaction_Date',
        'Transaction_Time', 'Transaction_Amount', 'Merchant_ID', 'Transaction_Type',
        'Merchant_Category', 'Account_Balance', 'Transaction_Device',
        'Transaction_Location', 'Device_Type', 'Is_Fraud', 'Transaction_Currency',
        'Customer_Contact', 'Transaction_Description', 'Customer_Email', 'Job'
    ])
    writer.writerows(rows)

print("CSV file 'transactions_powerbi.csv' created successfully.")
