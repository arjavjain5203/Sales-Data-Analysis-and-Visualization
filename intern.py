import pandas as pd
import matplotlib.pyplot as plt

# taking random data 
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'] * 25,
    'Quantity': [5, 3, 2, 4, 1, 6, 7, 2, 3, 5] * 10,
    'Price': [100, 200, 150, 300] * 25
}


df = pd.DataFrame(data)


df['Total Revenue'] = df['Quantity'] * df['Price']


daily_sales = df.groupby('Date')['Total Revenue'].sum().reset_index()


total_revenue = df['Total Revenue'].sum()
total_orders = df['Quantity'].sum() 
average_order_value = total_revenue / total_orders


cost_of_goods_sold = 0.6  
df['Cost'] = df['Total Revenue'] * cost_of_goods_sold
df['Profit'] = df['Total Revenue'] - df['Cost']
profit_margin = (df['Profit'].sum() / total_revenue) * 100


print(f"Total Revenue: ₹{total_revenue:.2f}")
print(f"Average Order Value (AOV): ₹{average_order_value:.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")


plt.figure(figsize=(12, 6))
plt.plot(daily_sales['Date'], daily_sales['Total Revenue'], marker='o')
plt.title('Daily Sales Revenue')
plt.xlabel('Date')
plt.ylabel('Total Revenue (₹)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

product_sales = df.groupby('Product')['Total Revenue'].sum().reset_index()


plt.figure(figsize=(8, 5))
plt.bar(product_sales['Product'], product_sales['Total Revenue'], color='skyblue')
plt.title('Sales Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue (₹)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()