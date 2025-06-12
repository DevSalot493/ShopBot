import re

def parse_query(query: str) -> dict:
    query = query.lower()
    products = []
    attributes = []
    prices = []

    # Basic product type detection
    product_keywords = ["laptop", "mobile", "headphone", "fridge", "refrigerator", "tv", "smartphone"]
    for word in product_keywords:
        if word in query:
            products.append(word if word != "fridge" else "refrigerator")

    # Attribute keywords
    attribute_keywords = ["battery", "camera", "gaming", "performance", "storage", "display", "portable"]
    for word in attribute_keywords:
        if word in query:
            attributes.append(word)

    # Price pattern
    price_matches = re.findall(r"₹?\s?[\d,]{4,7}", query)
    prices = [p.replace("₹", "").replace(",", "").strip() for p in price_matches]

    return {
        "products": products,
        "attributes": attributes,
        "prices": prices
    }
