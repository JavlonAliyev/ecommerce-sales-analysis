import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datasetni o‘qish
df = pd.read_csv("ecommerce_sales.csv")

# Order date ustunini datetime formatga o‘tkazamiz
df['order_date'] = pd.to_datetime(df['order_date'])

# Grafiklar stili
sns.set(style="whitegrid")

# 1️ Eng ko‘p buyurtma berilgan toifalar
plt.figure(figsize=(8,5))
sns.countplot(y='category', data=df, order=df['category'].value_counts().index, palette="Blues_r")
plt.title("Eng ko‘p buyurtma berilgan toifalar")
plt.xlabel("Buyurtmalar soni")
plt.ylabel("Toifa nomi")
plt.show()

# 2️ Regionlar bo‘yicha umumiy daromad
revenue_by_region = df.groupby('region')['total_price'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=revenue_by_region.values, y=revenue_by_region.index, palette="Greens_r")
plt.title("Regionlar bo‘yicha umumiy daromad")
plt.xlabel("Daromad (USD)")
plt.ylabel("Region")
plt.show()

# 3️ Oylar bo‘yicha sotuv trendi
df['month'] = df['order_date'].dt.to_period('M')
sales_by_month = df.groupby('month')['total_price'].sum()

plt.figure(figsize=(10,5))
sales_by_month.plot(marker='o')
plt.title("Oylar bo‘yicha umumiy sotuv trendi")
plt.xlabel("Oy")
plt.ylabel("Daromad")
plt.grid(True)
plt.show()

# 4️ Eng ko‘p daromad keltirgan 10 ta mahsulot
top_products = df.groupby('product_name')['total_price'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_products.values, y=top_products.index, palette="Oranges_r")
plt.title("Eng ko‘p daromad keltirgan 10 ta mahsulot")
plt.xlabel("Umumiy daromad")
plt.ylabel("Mahsulot nomi")
plt.show()
