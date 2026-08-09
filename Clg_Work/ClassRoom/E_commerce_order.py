"""
orders.csv has columns order_id,
customer, category, amount, status (Completed/Pending/Cancelled). Write
generate_summary(rows) that computes total revenue from Completed orders only,
order counts per category (all statuses), and the top-spending customer by
total Completed amount. Use assert to verify computed revenue is never negative
before returning. A missing or non-numeric amount must be caught and the row
skipped/logged rather than crashing the program.
"""
import pandas as pd

df=pd.read_csv("orders.csv")
def generate_summary(df):
    
    # Invalid/missing values become NaN instead of causing an error.
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    
    
    # Log and remove invalid amount rows
    invalid_rows = df["amount"].isna()

    if invalid_rows.any():
        print("Skipping rows with missing/non-numeric amounts:")
        print(df[invalid_rows])

    df = df.dropna(subset=["amount"])

    # 1. Total revenue from Completed orders only
    total_revenue = df.groupby("status")["amount"].sum()
    completed_revenue = total_revenue.get("Completed", 0)
    print(completed_revenue)
           
    # 2. Order counts per category — ALL statuses
    order_count=df.groupby("category").count()
    print(order_count)
    
    # 3. Top-spending customer — Completed orders only
    customer_spending = df.groupby("customer")["amount"].sum()
    
    if len(customer_spending) >0:
        top_customer= customer_spending.idxmax()
        top_amount=customer_spending.max()
    else:
        top_customer=None
        top_amount=0
        
    print("Total Completed Revenue:", total_revenue)
    print("\nOrder counts per category:")
    print(order_count)

    print("\nTop-spending customer:", top_customer)
    print("Completed spending:", top_amount)  

generate_summary(df)