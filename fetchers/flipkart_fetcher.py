def fetch_products(query_data):
    print("[Flipkart Fetcher Called]")

    if 'laptop' in query_data['products']:
        return [{
            "source": "Flipkart",
            "title": "HP Victus Ryzen 5 Gaming Laptop",
            "price": 79990,
            "rating": 4.5,
            "url": "https://www.flipkart.com/item456",
            "attributes": ["battery", "gaming", "144Hz"]
        }]
    
    elif 'phone' in query_data['products']:
        return [{
            "source": "Flipkart",
            "title": "Redmi Note 13 Pro+ 5G",
            "price": 27999,
            "rating": 4.4,
            "url": "https://www.flipkart.com/item789",
            "attributes": ["camera", "battery", "display"]
        }]
    
    return []
