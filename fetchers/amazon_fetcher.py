def fetch_products(query_data):
    print("[Amazon Fetcher Called]")

    if 'laptop' in query_data['products']:
        return [{
            "source": "Amazon",
            "title": "ASUS TUF Gaming F15",
            "price": 74990,
            "rating": 4.3,
            "url": "https://www.amazon.in/dp/example123",
            "attributes": ["gaming", "battery", "15.6 inch"]
        }]
    
    elif 'phone' in query_data['products']:
        return [{
            "source": "Amazon",
            "title": "Samsung Galaxy S21 FE",
            "price": 49999,
            "rating": 4.2,
            "url": "https://www.amazon.in/dp/example-phone",
            "attributes": ["camera", "display"]
        }]
    
    return []
