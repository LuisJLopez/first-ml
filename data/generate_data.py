import csv
import random

# Function to generate random insurance data
def generate_insurance_data(num_records):
    data = []
    for _ in range(num_records):
        age = random.randint(18, 70)
        sex = random.choice(['male', 'female'])
        bmi = round(random.uniform(18.0, 40.0), 2)
        children = random.randint(0, 5)
        smoker = random.choice(['yes', 'no'])
        region = random.choice(['northeast', 'northwest', 'southeast', 'southwest'])
        charges = round(random.uniform(1000.0, 60000.0), 2)
        data.append([age, sex, bmi, children, smoker, region, charges])
    return data

# Generate dummy insurance data
num_records = 1000
data = generate_insurance_data(num_records)

# Write data to CSV file
csv_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
csv_file = "insurance.csv"

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for record in data:
        writer.writerow(record)

print(f"Generated {num_records} records of dummy insurance data. Saved to {csv_file}.")
