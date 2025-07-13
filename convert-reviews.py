import csv
import json
from collections import defaultdict

# Input and output file paths
input_csv = "davidaustinroses-dev-all-published-reviews-in-judgeme-format-2025-07-10-1752157453.csv"
output_json = "reviews_by_product.json"

# Base URL for David Austin Roses products
base_url = "https://www.davidaustinroses.co.uk/products/"

# Initialize a defaultdict to group reviews by product_handle
reviews_by_product = defaultdict(list)

# Read the CSV file
try:
    with open(input_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Add the review to the corresponding product_handle
            product_handle = row['product_handle']
            reviews_by_product[product_handle].append({
                "title": row['title'],
                "body": row['body'],
                "rating": int(row['rating']),
                "review_date": row['review_date'],
                "source": row['source'],
                "curated": row['curated'],
                "reviewer_name": row['reviewer_name'],
                "reviewer_email": row['reviewer_email'],
                "product_id": row['product_id'],
                "product_handle": row['product_handle'],
                "reply": row['reply'],
                "reply_date": row['reply_date'],
                "picture_urls": row['picture_urls'],
                "ip_address": row['ip_address'],
                "location": row['location'],
                "metaobject_handle": row['metaobject_handle']
            })
except FileNotFoundError:
    print(f"Error: The file {input_csv} was not found.")
    exit(1)
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit(1)

# Convert to the desired JSON structure
json_output = {}
for product_handle, reviews in reviews_by_product.items():
    json_output[product_handle] = {
        "product_url": f"{base_url}{product_handle}",
        "reviews": reviews
    }

# Write the output to a JSON file
try:
    with open(output_json, mode='w', encoding='utf-8') as file:
        json.dump(json_output, file, indent=2, ensure_ascii=False)
    print(f"Successfully wrote JSON output to {output_json}")
except Exception as e:
    print(f"Error writing JSON: {e}")
    exit(1)