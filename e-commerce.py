import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="****",
    passwd="r*****6"
)

print("MySQL connection established")

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_returns")

print("Database created successfully")

# Load original dataset
df = pd.read_csv(
    r'C:\Users\user\Downloads\archive (5)\Kaggle_Ecommerce Data.csv'
)

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
df['delivered_date'] = pd.to_datetime(df['delivered_date'], dayfirst=True)
df['request_date'] = pd.to_datetime(
    df['request_date'],
    dayfirst=True,
    errors='coerce'
)

# Create derived columns
df['delivery_days'] = (
    df['delivered_date'] - df['order_date']
).dt.days

df['return_days'] = (
    df['request_date'] - df['delivered_date']
).dt.days

df['delivery_group'] = pd.cut(
    df['delivery_days'],
    bins=[0, 3, 5, 7, 10, float('inf')],
    labels=['1-3 days', '4-5 days', '6-7 days',
            '8-10 days', '11+ days']
)

# Export to a NEW file
df.to_csv(
    r'C:\Users\user\Downloads\ecommerce_cleaned.csv',
    index=False
)

print("Cleaned dataset exported successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print(df.dtypes)
print("\nColumns:")
print(df.columns.tolist())



import pandas as pd

df = pd.read_csv(
    r'C:\Users\user\Downloads\ecommerce_cleaned.csv'
)


# ---------------------------------------------------------
# IMPORT CLEANED DATA INTO MYSQL
# ---------------------------------------------------------

cursor = mydb.cursor()
cursor.execute("USE ecommerce_returns")

insert_query = """
INSERT INTO ecommerce_data (
    order_id,
    customer_id,
    product_id,
    category,
    price,
    discount,
    quantity,
    payment_method,
    order_date,
    delivered_date,
    region,
    returned,
    request_date,
    return_reason,
    total_amount,
    shipping_cost,
    profit_margin,
    customer_age,
    customer_gender,
    delivery_days,
    return_days,
    delivery_group
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Convert missing values (NaN / NaT) to None
# MySQL will store None as NULL
df_mysql = df.astype(object).where(pd.notnull(df), None)

# Convert rows into tuples
data = list(df_mysql.itertuples(index=False, name=None))

# Insert 1000 rows at a time
batch_size = 1000

for i in range(0, len(data), batch_size):

    batch = data[i:i + batch_size]

    cursor.executemany(insert_query, batch)
    mydb.commit()

    print(
        f"Inserted {min(i + batch_size, len(data))} "
        f"of {len(data)} rows"
    )

print("\nData imported successfully!")

cursor.close()
mydb.close()





