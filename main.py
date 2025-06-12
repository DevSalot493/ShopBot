from query_parser import parse_query
from fetch_all_products import fetch_all_products

if __name__ == "__main__":
    # 🔧 Replace input() with test string
    test_query = "gaming laptop under 80000 with good battery"
    parsed = parse_query(test_query)

    print(f"\n🔍 Parsed Query: {parsed}\n")
    print("🔎 Searching Amazon...\n")

    results = fetch_all_products(parsed)

    if not results:
        print("❌ No results found.")
    else:
        for i, product in enumerate(results[:10], start=1):  # Show top 10
            print(f"{i}. 🛍️ {product['title']}")
            print(f"   💰 {product['price']} | ⭐ {product['rating']}")
            print(f"   🔗 {product['url']}\n")
