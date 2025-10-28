import pandas as pd

# 1️ Faylni o‘qish
df = pd.read_csv("ecommerce_sales.csv")

# 2️ Dataset haqida umumiy ma’lumot
print("=== Umumiy ma'lumot ===")
print(df.info())
print("\n=== Birinchi 5 qator ===")
print(df.head())

# 3️ Null qiymatlar mavjudmi?
print("\n=== Null qiymatlar soni ===")
print(df.isnull().sum())

# 4️ Dublikatlar soni
duplicates = df.duplicated().sum()
print(f"\n=== Dublikatlar soni: {duplicates} ===")

# 5️ Asosiy statistik ma’lumotlar
print("\n=== Statistik ma’lumotlar ===")
print(df.describe())

# 6️ Eng ko‘p sotilgan toifalar
top_categories = df['category'].value_counts()
print("\n=== Eng ko‘p buyurtma berilgan toifalar ===")
print(top_categories)

# 7️ Umumiy daromad bo‘yicha eng kuchli regionlar
revenue_by_region = df.groupby('region')['total_price'].sum().sort_values(ascending=False)
print("\n=== Regionlar bo‘yicha umumiy daromad ===")
print(revenue_by_region)

# 8️ Eng ko‘p daromad keltirgan mahsulotlar
top_products = df.groupby('product_name')['total_price'].sum().sort_values(ascending=False).head(10)
print("\n=== Eng ko‘p daromad keltirgan mahsulotlar ===")
print(top_products)

# 9️ Buyurtmalar soni bo‘yicha eng faol mijozlar
top_customers = df['customer_name'].value_counts().head(5)
print("\n=== Eng faol mijozlar (buyurtma soni bo‘yicha) ===")
print(top_customers)
