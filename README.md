# 🧾 Flatten Nested JSON Column

This Python project transforms a CSV file with a nested JSON column (`line_items`) into a flat table where each nested item is unpacked into its own row — perfect for analysis and visualisation.

The data simulates **sales orders** where multiple products are stored in a single row as a JSON array. The script extracts each product into a clean row format with associated metadata like order number, date, and fulfillment channel.

---

## 📊 Overview

Built using **Python** and **Pandas**, this mini ETL tool does the following:

- 📥 Reads raw CSV with nested JSON column
- 🧹 Parses and expands the JSON list items
- 🔄 Replicates order metadata for each product row
- 📤 Exports a flattened CSV for analysis

---

### 🔍 Key Transformations

| From Column | Type          | Description                            |
|-------------|---------------|----------------------------------------|
| `line_items`| JSON (array)  | Each order includes multiple products  |
| →           | Flat rows     | Each product becomes a new row         |
| Meta Fields | Copied        | Order details stay the same per row    |

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `sales_orders.csv` | Input CSV with a nested `line_items` column |
| `flatten_json_csv.py` | Python script to flatten the data |
| `flattened_sales_orders.csv` | Output file with each product on a separate row |
| `README.md` | Project documentation |

---

## 💡 Example

### 🎯 Sample Input

A single row from `sales_orders.csv`:

```json
[
  {
    "product": {
      "product_name": "WWI Desktop PC1.80 E1801 Silver",
      "product_price": 269.9
    },
    "quantity": 1
  },
  ...
]
## 🛠️ Tools Used

- **Microsoft Excel**
  - PivotTables & Charts
  - Slicers
  - Conditional Formatting
- **VBA Macros**
  - Automatically highlights highest revenue month
  - Works in sync with slicer selection

### 🔄 Becomes:

| order_number | order_date | fulfillment | product_name                    | product_price | quantity |
|--------------|------------|-------------|----------------------------------|---------------|----------|
| 387005       | 1/22/2016  | In store    | WWI Desktop PC1.80 E1801 Silver | 269.9         | 1        |
---

## ⚙️ How to Run

```bash
git clone https://github.com/OjAy-stack/Flatten-Nested-JSON-Column.git
cd Flatten-Nested-JSON-Column
pip install pandas
python flatten_json_csv.py
