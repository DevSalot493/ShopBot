import re

def parse_query(query: str) -> dict:
    product_keywords = {
        "laptop": ["laptop", "notebook", "macbook", "chromebook"],
        "phone": ["phone", "smartphone", "mobile", "cellphone"],
        "television": ["tv", "television", "smart tv"],
        "refrigerator": ["refrigerator", "fridge"],
        "oven": ["oven", "microwave", "microwave oven"],
        "ac": ["ac", "air conditioner", "aircon"],
        "speaker": ["speaker", "bluetooth speaker", "sound system"],
        "smartwatch": ["smartwatch", "watch", "fitness band", "fitbit"],
        # add more products and synonyms here
    }

    attribute_keywords = [
        "camera", "battery", "display", "screen", "fitness", "tracking", "bluetooth",
        "capacity", "ton", "gaming", "processor", "ram", "storage", "ssd", "hdd",
    ]

    query_lower = query.lower()

    found_products = []
    for product, synonyms in product_keywords.items():
        for syn in synonyms:
            if re.search(r'\b' + re.escape(syn) + r'\b', query_lower):
                found_products.append(product)
                break

    found_attributes = []
    for attr in attribute_keywords:
        if re.search(r'\b' + re.escape(attr) + r'\b', query_lower):
            found_attributes.append(attr)

    for attr in attribute_keywords:
        if attr in found_products:
            found_products.remove(attr)

    price_pattern = r'(?:\₹|rs|rupees)\s?[\d,]+'
    prices_found = re.findall(price_pattern, query_lower, flags=re.IGNORECASE)

    return {
        "products": list(set(found_products)),
        "attributes": list(set(found_attributes)),
        "prices": prices_found
    }
