import pandas as pd
import random
from faker import Faker

fake = Faker()

# Qancha yozuv yaratiladi
num_records = 5000

# Mahsulot toifalari
categories = {
    "Electronics": ["Smartphone", "Laptop", "Tablet", "Headphones", "Smartwatch"],
    "Clothing": ["T-shirt", "Jeans", "Jacket", "Shoes", "Hat"],
    "Home Appliances": ["Refrigerator", "Microwave", "Blender", "Oven", "Vacuum Cleaner"],
    "Beauty": ["Perfume", "Shampoo", "Lotion", "Lipstick", "Face Cream"],
    "Sports": ["Football", "Basketball", "Tennis Racket", "Yoga Mat", "Dumbbell"]
}

regions = ["Tashkent", "Samarkand", "Bukhara", "Andijan", "Fergana", "Namangan"]

data = []

for i in range(num_records):
    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])
    quantity = random.randint(1, 10)
    unit_price = random.randint(10, 1000)
    total_price = quantity * unit_price
    
    record = {
        "order_id": fake.uuid4(),
        "order_date": fake.date_between(start_date='-1y', end_date='today'),
        "customer_id": fake.uuid4(),
        "customer_name": fake.name(),
        "region": random.choice(regions),
        "product_id": fake.uuid4(),
        "category": category,
        "product_name": product_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price
    }
    
    data.append(record)

# DataFrame
df = pd.DataFrame(data)

# CSV fayl sifatida saqlash
df.to_csv("ecommerce_sales.csv", index=False)

print("Dataset tayyor bo‘ldi: ecommerce_sales.csv")
print(df.head())
