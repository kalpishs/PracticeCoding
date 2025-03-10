import os
import csv
import random
import datetime
from faker import Faker
import string

# Initialize the Faker instance
fake = Faker()

# Specify the date and hours
date = "12-Oct-2023"
hours = ["00","01","02","03","04","05", "06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
limit_cols=20
app_ids = []

merchant_ids = []
merchant_names = ["Amazon", "reliance", "imapaz", "Doordash", "uber"]
currencies = ["USD", "EUR", "INR", "GBP", "JPY"]
countries = ["USA", "IND", "CAN", "AUS", "GBR"]
merchant_ids_name={}
# Function to generate a random merchant ID
def generate_merchant_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


def make_merchant_id_names_map():
    for name in merchant_names:
        merchant_ids_name[name]= generate_merchant_id()

# Function to generate a random currency value
def generate_currency_value():
    return round(random.uniform(1, 1000), 2)

# Define the directory where you want to save the folders
base_directory = "output_data"

# Create the base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.mkdir(base_directory)

# Convert the date to the desired format
formatted_date = datetime.datetime.strptime(date, "%d-%b-%Y").strftime("%d%m%Y")


make_merchant_id_names_map()
# Loop through the specified hours
for hour in hours:
    # Create the directory path
    folder_path = os.path.join(base_directory, f"{formatted_date}/{hour}")


    # Create the directory if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate and write data to a CSV file
    csv_filename = os.path.join(folder_path, f"part-{hour}.csv")
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["AppID","merchant_id","merchant_name", "currency","country", "report_dt", "category", "timestamp", "currency_value", "info2", "info3"])

        # Generate and write fake data
        for _ in range(limit_cols):  # You can change the number of rows as needed
            if random.choice([True, False]):
                app_id = random.choice(app_ids) if app_ids else fake.uuid4()
            else:
                app_id = fake.uuid4()
                app_ids.append(app_id)

            merchant_name = random.choice(merchant_names)
            merchant_id = merchant_ids_name[merchant_name]
            currency = random.choice(currencies)
            country = random.choice(countries)
            data_type = fake.word() if random.choice([True, False]) else None  # Random string or "string"
            category = fake.random_element(elements=("iPhone", "macbook", "watch", "ipad")) if random.choice([True, False]) else None
            if len(hour.split(':')) == 1:
                hour += ':00:00'
            datetime_obj = datetime.datetime.strptime(f"{date} {hour}", "%d-%b-%Y %H:%M:%S")
            timestamp = datetime_obj.strftime("%Y-%m-%dT%H:%M:%S")
            currency_value = generate_currency_value()
            other_column_1 = fake.word()  if random.choice([True, False]) else None
            other_column_2 = fake.word()  if random.choice([True, False]) else None

            csv_writer.writerow([app_id,merchant_id, merchant_name, currency,country, date, category, timestamp,currency_value, other_column_1, other_column_2])

    print(f"Generated data for {date}/{hour} in {csv_filename}")
