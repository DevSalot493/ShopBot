from query_parser import parse_query
from fetch_all_products import fetch_all_products

# 🔧 Your test query (change this line to test other inputs)
query = "I want a gaming laptop under ₹80,000 with good battery life"

parsed = parse_query(query)
print("🔍 Parsed Query:", parsed)

results = fetch_all_products(parsed)

print("\n🛍️ Product Results:")
for product in results:
    print(f"{product['source']} - {product['title']}")
    print(f"Price: ₹{product['price']}, Rating: {product['rating']}")
    print(f"URL: {product['url']}")
    print(f"Attributes: {product['attributes']}")
    print("-" * 40)
