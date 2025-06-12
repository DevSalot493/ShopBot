from fetchers.amazon_fetcher import fetch_amazon_products

def fetch_all_products(parsed_query: dict) -> list:
    amazon_results = fetch_amazon_products(parsed_query)
    return amazon_results
