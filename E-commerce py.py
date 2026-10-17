import pandas as pd
import matplotlib.pyplot as plt

#Data Loading
df=pd.read_csv(r'C:\Users\user\Downloads\archive (5)\Kaggle_Ecommerce Data.csv')

#Basic Data Inspection

print(df.head()) #Display Top Rows

print(df.tail()) #Display Bottom Rows

print("Dataset Shape:", df.shape)

print(df.dtypes) #Display data type

print(df.describe()) #Summary Statistics

print(df.info()) #Display Index,Column,Data

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

#Column names
print("\nColumn Names:")
print(df.columns.tolist())

#Unique values in categorical columns
print("\nReturn Status:")
print(df['returned'].value_counts())

print("\nReturned Reason:")
print(df['return_reason'].value_counts())

print("\nProduct Categories:")
print(df['category'].value_counts())

#check the data column
print("\nDate Columns:")
print(df['order_date'],df['delivered_date'],df['request_date'])

#Number of unique values
print("\nUnique values per column:")
print(df.nunique())

print("\nPayment Methods:")
print(df['payment_method'].value_counts())

# Convert date columns from DD/MM/YYYY format

df['order_date'] = pd.to_datetime(
    df['order_date'],
    dayfirst=True
)

df['delivered_date'] = pd.to_datetime(
    df['delivered_date'],
    dayfirst=True
)

df['request_date'] = pd.to_datetime(
    df['request_date'],
    dayfirst=True
)

print("\nDate Data Types:")
print(df[['order_date', 'delivered_date', 'request_date']].dtypes)

print("\nSample Dates:")
print(df[['order_date', 'delivered_date', 'request_date']].head())

# Calculate delivery time in days
df['delivery_days'] = (
    df['delivered_date'] - df['order_date']
).dt.days


# Calculate number of days between delivery and return request
df['return_days'] = (
    df['request_date'] - df['delivered_date']
).dt.days


print("\nFEATURE ENGINEERING OUTPUT")
print(df[['delivery_days', 'return_days']].head(10))

print("\nDATA TYPES")
print(df[['delivery_days', 'return_days']].dtypes)

print("\nRETURNED ORDERS — FEATURE ENGINEERING")
print(
    df.loc[
        df['returned'] == 'Yes',
        ['delivery_days', 'return_days']
    ].head(10).to_string(index=False)
)

df['delivery_group'] = pd.cut(
    df['delivery_days'],
    bins=[0, 3, 5, 7, 10, float('inf')],
    labels=['1-3 days', '4-5 days', '6-7 days',
            '8-10 days', '11+ days']
)

print("\nDELIVERY TIME GROUPS")
print(
    df[['delivery_days', 'delivery_group']]
    .head(10)
    .to_string(index=False)
)

print("\nNUMBER OF ORDERS BY DELIVERY GROUP")
print(df['delivery_group'].value_counts().sort_index())

print("\nDelivery Days:")
print(df['delivery_days'].describe())

print("\nReturn Days:")
print(df['return_days'].describe())

# Return analysis by product category

category_analysis = df.groupby('category').agg(
    total_orders=('order_id', 'count'),
    returned_orders=('returned', lambda x: (x == 'Yes').sum())
)

category_analysis['return_rate'] = (
    category_analysis['returned_orders']
    / category_analysis['total_orders']
) * 100

print("\nReturn Analysis by Category:")
print(category_analysis.sort_values('return_rate', ascending=False))

# Return reasons Analysis

return_reasons = (
    df[df['returned'] == 'Yes']['return_reason']
    .value_counts()
)

print("\nReturn Reasons:")
print(return_reasons)

# Return analysis by region

region_analysis = df.groupby('region').agg(
    total_orders=('order_id', 'count'),
    returned_orders=('returned', lambda x: (x == 'Yes').sum())
)

region_analysis['return_rate'] = (
    region_analysis['returned_orders']
    / region_analysis['total_orders']
) * 100


print("\nReturn Analysis by Region:")
print(region_analysis.sort_values('return_rate', ascending=False))

# Regional return and shipping cost analysis

region_cost_analysis = df.groupby('region').agg(
    total_orders=('order_id', 'count'),
    returned_orders=('returned', lambda x: (x == 'Yes').sum()),
    total_shipping_cost=('shipping_cost', 'sum'),
    average_shipping_cost=('shipping_cost', 'mean')
)

print(region_cost_analysis.to_string())

region_cost_analysis['return_rate'] = (
    region_cost_analysis['returned_orders']
    / region_cost_analysis['total_orders']
) * 100

print("\nRegional Return and Shipping Cost Analysis:")
print(region_cost_analysis.sort_values('return_rate', ascending=False))'''


'''# Shipping cost: Returned vs Non-returned

shipping_analysis = df.groupby('returned').agg(
    total_orders=('order_id', 'count'),
    total_shipping_cost=('shipping_cost', 'sum'),
    average_shipping_cost=('shipping_cost', 'mean')
)

print("\nShipping Cost Analysis:")
print(shipping_analysis)

# Profit margin: Returned vs Non-returned

profit_analysis = df.groupby('returned').agg(
    total_orders=('order_id', 'count'),
    average_profit_margin=('profit_margin', 'mean'),
    total_profit_margin=('profit_margin', 'sum')
)

print("\nProfit Margin Analysis:")
print(profit_analysis)

# Category-wise return and cost analysis

category_cost = df.groupby('category').agg(
    total_orders=('order_id', 'count'),
    returned_orders=('returned', lambda x: (x == 'Yes').sum()),
    total_shipping_cost=('shipping_cost', 'sum'),
    average_shipping_cost=('shipping_cost', 'mean'),
    average_profit_margin=('profit_margin', 'mean')
)

category_cost['return_rate'] = (
    category_cost['returned_orders']
    / category_cost['total_orders']
) * 100

print("\nCategory Cost Analysis:")
print(category_cost.sort_values('return_rate', ascending=False))

#Return Reason Analysis

return_reason_analysis=df[df['returned']=='Yes']['return_reason'].value_counts()

print("\nReturn Reason analysis:")
print(return_reason_analysis)

#Return Reason Percentage

return_reason_percentage=(
    df[df['returned']=='Yes']['return_reason']
    .value_counts(normalize=True)*100
    )

print("\nReturn Reason Percentage:")
print(return_reason_percentage)

# Category vs Return Reason

category_reason = pd.crosstab(
    df[df['returned'] == 'Yes']['category'],
    df[df['returned'] == 'Yes']['return_reason']
)

print("\nCategory vs Return Reason:")
print(category_reason.to_string())

#Discount Vs Return

discount_analysis=df.groupby('returned').agg(
    total_orders=('order_id','count'),
    average_discount=('discount','mean')
    )

print("\nDiscount Analysis:")
print(discount_analysis)

discount_groups = pd.cut(
    df['discount'],
    bins=[-0.01, 0, 0.05, 0.10, 0.20, 0.30],
    labels=['0%', '1-5%', '6-10%', '11-20%', '21-30%']
)

discount_return_analysis = pd.crosstab(
    discount_groups,
    df['returned'],
    normalize='index'
) * 100

print("\nDiscount Level vs Return:")
print(discount_return_analysis)

price_analysis=df.groupby('returned').agg(
    total_orders=('order_id','count'),
    avaerage_price=('price','mean'),
    median_price=('price','median'),
    )
print("\nPrice analysis:")
print(price_analysis)

discount_groups = pd.cut(
    df['discount'],
    bins=[-0.01, 0, 0.05, 0.10, 0.20, 0.30],
    labels=['0%', '1-5%', '6-10%', '11-20%', '21-30%']
)

discount_return_analysis = pd.crosstab(
    discount_groups,
    df['returned'],
    normalize='index'
) * 100

print("\nDiscount Level vs Return:")
print(discount_return_analysis)

#price Vs Return

price_analysis= df.groupby('returned').agg(
    total_orders=('order_id','count'),
    average_price=('price','mean'),
    median_price=('price','median'),
    )

print("\nPrice Analysis:")
print(price_analysis)

price_groups = pd.cut(
    df['price'],
    bins=[0, 50, 100, 200, 500, float('inf')],
    labels=['0-50', '51-100', '101-200', '201-500', '500+']
)

price_return_analysis = pd.crosstab(
    price_groups,
    df['returned'],
    normalize='index'
) * 100

print("\nPrice Range vs Return:")
print(price_return_analysis)

#Delivery Time Vs Return

df['delivery_days'] = (
    df['delivered_date'] - df['order_date']
).dt.days

print(df['delivery_days'])

delivery_analysis = df.groupby('returned').agg(
    total_orders=('order_id', 'count'),
    average_delivery_days=('delivery_days', 'mean'),
    median_delivery_days=('delivery_days', 'median')
)

print("\nDelivery Time Analysis:")
print(delivery_analysis)


#Quatity Vs Return

quantity_analysis = df.groupby('returned').agg(
    total_orders=('order_id', 'count'),
    average_quantity=('quantity', 'mean'),
    median_quantity=('quantity', 'median')
)

print("\nQuantity Analysis:")
print(quantity_analysis)

quantity_return_analysis = pd.crosstab(
    df['quantity'],
    df['returned'],
    normalize='index'
) * 100

print("\nQuantity vs Return:")
print(quantity_return_analysis)

# EDA SUMMARY
# --------------------------------------------

total_orders = len(df)
returned_orders = (df['returned'] == 'Yes').sum()
return_rate = (returned_orders / total_orders) * 100

category_return_rate = (
    df.groupby('category')['returned']
    .apply(lambda x: (x == 'Yes').mean() * 100)
    .sort_values(ascending=False)
)

return_reasons = (
    df[df['returned'] == 'Yes']['return_reason']
    .value_counts()
)

shipping_analysis = (
    df.groupby('returned')['shipping_cost'].mean()
)

price_analysis = (
    df.groupby('returned')['price'].mean()
)

print("\n" + "=" * 50)
print("         EXPLORATORY DATA ANALYSIS SUMMARY")
print("=" * 50)

print("\nOVERALL RETURN PERFORMANCE")
print("Total Orders:", total_orders)
print("Returned Orders:", returned_orders)
print(f"Return Rate: {return_rate:.2f}%")

print("\nPRODUCT CATEGORY")
print("Highest Return Rate:",
      category_return_rate.index[0],
      f"({category_return_rate.iloc[0]:.2f}%)")

print("\nRETURN REASONS")
print("Most Common Reason:",
      return_reasons.index[0],
      f"({return_reasons.iloc[0]} returns)")

print("\nAVERAGE RECORDED SHIPPING COST")
print(f"Returned Orders: {shipping_analysis['Yes']:.2f}")
print(f"Non-Returned Orders: {shipping_analysis['No']:.2f}")

print("\nAVERAGE PRODUCT PRICE")
print(f"Returned Orders: {price_analysis['Yes']:.2f}")
print(f"Non-Returned Orders: {price_analysis['No']:.2f}")

print("\n" + "=" * 50)

#visualisation
# Return Rate by Category

category_return_rate = (
    df.groupby('category')['returned']
    .apply(lambda x: (x == 'Yes').mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))
category_return_rate.plot(kind='bar')

plt.title('Return Rate by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Return Reasons

return_reasons = (
    df[df['returned'] == 'Yes']['return_reason']
    .value_counts()
)

plt.figure(figsize=(9, 5))
return_reasons.plot(kind='bar')

plt.title('Major Reasons for Product Returns')
plt.xlabel('Return Reason')
plt.ylabel('Number of Returns')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

#Return Rate by Region

region_return_rate = (
    df.groupby('region')['returned']
    .apply(lambda x:(x=='Yes').mean()*100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
region_return_rate.plot(kind='bar')

plt.title('Return Rate by Region')
plt.xlabel('Region')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

# Average Shipping Cost by Return Status

shipping_cost_status = (
    df.groupby('returned')['shipping_cost']
    .mean()
)

plt.figure(figsize=(6, 5))
shipping_cost_status.plot(kind='bar')

plt.title('Average Shipping Cost by Return Status')
plt.xlabel('Return Status')
plt.ylabel('Average Shipping Cost')
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

#Return Rate by Price Range

price_groups = pd.cut(
    df['price'],
    bins=[0, 50, 100, 200, 500, float('inf')],
    labels=['0-50', '50-100', '100-200', '200-500', '500+']
)

price_return_rate=(
    df.groupby(price_groups,observed=True)['returned']
    .apply(lambda x:(x=='Yes').mean()*100)
    )

price_return_rate.plot(kind='bar')

plt.title('Return Rate by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

# Create delivery days
df['delivery_days'] = (
    df['delivered_date'] - df['order_date']
).dt.days

# Create return days
df['return_days'] = (
    df['request_date'] - df['delivered_date']
).dt.days

# Create Delivery Time Groups
df['delivery_group'] = pd.cut(
    df['delivery_days'],
    bins=[0, 3, 5, 7, 10, float('inf')],
    labels=['1-3 days', '4-5 days', '6-7 days', '8-10 days', '11+ days']
)

print(df[['delivery_days', 'delivery_group']].head())

# Return Rate by Delivery Time
delivery_return_rate = (
    df.groupby('delivery_group', observed=False)['returned']
    .apply(lambda x: (x == 'Yes').mean() * 100)
)

print(delivery_return_rate)

plt.figure(figsize=(8, 5))
delivery_return_rate.plot(kind='bar')

plt.title('Return Rate by Delivery Time')
plt.xlabel('Delivery Time')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

print("\nNumber of Orders by Delivery Group:")
print(df['delivery_group'].value_counts().sort_index())


# COMBINED EDA VISUALIZATIONS
# --------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# 1. Return Rate by Product Category
category_return_rate = (
    df.groupby('category')['returned']
    .apply(lambda x: (x == 'Yes').mean() * 100)
    .sort_values(ascending=False)
)

category_return_rate.plot(
    kind='bar', ax=axes[0, 0], color='steelblue'
)
axes[0, 0].set_title('Return Rate by Product Category')
axes[0, 0].set_xlabel('Product Category')
axes[0, 0].set_ylabel('Return Rate (%)')
axes[0, 0].tick_params(axis='x', rotation=35)


# 2. Major Reasons for Product Returns
return_reasons = (
    df[df['returned'] == 'Yes']['return_reason']
    .value_counts()
)

return_reasons.plot(
    kind='bar', ax=axes[0, 1], color='cornflowerblue'
)
axes[0, 1].set_title('Major Reasons for Product Returns')
axes[0, 1].set_xlabel('Return Reason')
axes[0, 1].set_ylabel('Number of Returns')
axes[0, 1].tick_params(axis='x', rotation=35)


# 3. Return Rate by Region
region_return_rate = (
    df.groupby('region')['returned']
    .apply(lambda x: (x == 'Yes').mean() * 100)
    .sort_values(ascending=False)
)

region_return_rate.plot(
    kind='bar', ax=axes[1, 0], color='royalblue'
)
axes[1, 0].set_title('Return Rate by Region')
axes[1, 0].set_xlabel('Region')
axes[1, 0].set_ylabel('Return Rate (%)')
axes[1, 0].tick_params(axis='x', rotation=0)


# 4. Average Shipping Cost by Return Status
shipping_cost_status = (
    df.groupby('returned')['shipping_cost'].mean()
)

shipping_cost_status = shipping_cost_status.reindex(['No', 'Yes'])

shipping_cost_status.plot(
    kind='bar', ax=axes[1, 1], color='skyblue'
)
axes[1, 1].set_title('Average Shipping Cost by Return Status')
axes[1, 1].set_xlabel('Return Status')
axes[1, 1].set_ylabel('Average Recorded Shipping Cost')
axes[1, 1].tick_params(axis='x', rotation=0)

# Final Layout
fig.suptitle(
    'E-Commerce Returns - Exploratory Data Analysis',
    fontsize=16, fontweight='bold'
)
plt.subplots_adjust(
    left=0.08,
    right=0.97,
    top=0.88,
    bottom=0.10,
    hspace=0.65,
    wspace=0.25
)

plt.show()



# SUMMARY OF KEY FINDINGS
#**************************************************

# 1. Overall Return Performance
# Total orders analyzed: 34,500
# Returned orders: 1,903
# Overall return rate: 5.52%

# 2. Product Category
# Fashion had the highest return rate (8.28%),
# followed by Electronics (7.30%).
# Grocery had the lowest return rate (1.31%).

# 3. Regional Performance
# East had the highest return rate (5.91%),
# while Central had the lowest (5.10%).
# Regional differences were relatively small.

# 4. Return Reasons
# The major return reasons were:
# - Not as described: 25.75%
# - No longer needed: 25.28%
# - Defective: 24.44%
# - Missing/Wrong item: 23.07%
# - Slow delivery: 1.47%

# 5. Shipping Cost
# Returned orders had a higher average shipping cost (6.63)
# than non-returned orders (6.12).

# 6. Profit Margin
# Returned orders had an average profit margin of 32.48,
# compared with 27.86 for non-returned orders.
# Grocery had a negative average profit margin (-2.26).

# 7. Discount
# Discount levels showed no clear relationship with returns.
# Average discounts were similar for returned and non-returned orders.

# 8. Product Price
# Returned orders had a higher average product price (145.12)
# than non-returned orders (117.89).
# Return rate increased from 4.57% for products priced 0-50
# to 7.09% for products priced above 500.

# 9. Delivery Time
# Average delivery time was almost identical for returned
# and non-returned orders (4.84 vs 4.81 days).
# Delivery time did not show a strong relationship with returns.

# 10. Quantity
# Order quantity showed no strong relationship with returns.
# Average quantity was almost identical for returned
# and non-returned orders.

# Overall Finding:
# Product category, product price, return reasons, and shipping cost
# were the more notable factors associated with return logistics
# performance in this dataset.






























































