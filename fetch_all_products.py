from fetchers.amazon_fetcher import fetch_products as fetch_amazon
from fetchers.flipkart_fetcher import fetch_products as fetch_flipkart

def fetch_all_products(query_data):
    amazon_results = fetch_amazon(query_data)
    flipkart_results = fetch_flipkart(query_data)
    return amazon_results + flipkart_results

