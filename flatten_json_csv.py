import pandas as pd
import json

# Step 1: Load the CSV
df = pd.read_csv(r"C:\Users\HP\Downloads\sales_orders.csv")

# Step 2: Convert JSON strings in the 'line_items' column into Python objects
df["line_items"] = df["line_items"].apply(json.loads)

# Step 3: Explode the list of line items into multiple rows
df_exploded = df.explode("line_items").reset_index(drop=True)

# Step 4: Flatten the dictionary inside each line_item
line_items_flat = pd.json_normalize(df_exploded["line_items"])

# Step 5: Merge the flattened line items with the original (minus the nested column)
final_df = pd.concat([df_exploded.drop("line_items", axis=1), line_items_flat], axis=1)

# Step 6: Save the result as a new CSV
final_df.to_csv(r"C:\Users\HP\Downloads\flattened_sales_orders.csv", index=False)

print("Completed. Check your downloads folder for flattened csv")
