from faker import Faker
import pandas as pd
import random

fake = Faker()

rows = []

for i in range(1000):
    rows.append({
        "customer_id": i + 1,
        "customer_name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "sales": round(random.uniform(100, 5000), 2)
    })

df = pd.DataFrame(rows)

df.to_csv("data/raw/sales_data.csv", index=False)

print("Raw dataset generated successfully.")