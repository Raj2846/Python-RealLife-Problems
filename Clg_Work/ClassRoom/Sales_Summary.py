"""
regional_sales.csv has columns
date, region, product, units_sold, revenue. Generate a per-region summary
(total_revenue, total_units, best_selling_product by units_sold, alphabetical
tie-break) and write it to regional_summary.csv, sorted by total_revenue
descending.
"""

import pandas as pd
def pandas_(df):
    # Read the input CSV
    df = pd.read_csv("reginal_sales.csv")

    # Total revenue and units sold per region
    summary = df.groupby("region").agg(
        total_revenue=("revenue", "sum"),
        total_units=("units_sold", "sum")
    ).reset_index()

    # Find best-selling product for each region
    # First sort by region, units_sold descending, product alphabetically
    product_sales = (
        df.groupby(["region", "product"], as_index=False)["units_sold"]
        .sum()
        .sort_values(
            ["region", "units_sold", "product"],
            ascending=[True, False, True]
        )
    )

    # Pick the first product for each region
    best_products = (
        product_sales
        .drop_duplicates("region")
        .rename(columns={"product": "best_selling_product"})
        [["region", "best_selling_product"]]
    )

    # Combine the summaries
    summary = summary.merge(best_products, on="region")

    # Sort by total revenue descending
    summary = summary.sort_values("total_revenue", ascending=False)

    # Write to CSV
    summary.to_csv("regional_summary.csv", index=False)

    print(summary)
    
    
    
import csv
def generate_summary(input_file, output_file):
    regions = {}

    with open(input_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Ignore completely blank rows
            if not row.get("region"):
                continue

            region = row["region"]
            product = row["product"]

            try:
                units = int(row["units_sold"])
                revenue = float(row["revenue"])
            except (ValueError, TypeError):
                continue

            # Create aggregation state for a new region
            if region not in regions:
                regions[region] = {
                    "total_revenue": 0,
                    "total_units": 0,
                    "products": {}
                }

            regions[region]["total_revenue"] += revenue
            regions[region]["total_units"] += units

            # Track units by product
            products = regions[region]["products"]
            products[product] = products.get(product, 0) + units

    # Build final summary
    summary = []

    for region, data in regions.items():
        products = data["products"]

        # Highest units; alphabetical product wins ties
        best_product = min(
            products,
            key=lambda p: (-products[p], p)
        )

        summary.append({
            "region": region,
            "total_revenue": data["total_revenue"],
            "total_units": data["total_units"],
            "best_selling_product": best_product
        })

    # Required output ordering
    summary.sort(
        key=lambda x: x["total_revenue"],
        reverse=True
    )

    # Write output CSV
    with open(output_file, "w", newline="") as file:
        fieldnames = [
            "region",
            "total_revenue",
            "total_units",
            "best_selling_product"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary)


generate_summary(
    "reginal_sales.csv",
    "regional_summary.csv"
)