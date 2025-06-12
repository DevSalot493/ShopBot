from playwright.sync_api import sync_playwright
import time

def fetch_amazon_products(parsed_query):
    print("\n🔎 Searching Amazon...")

    search_query = " ".join(parsed_query['attributes'] + parsed_query['products'])  # e.g., "gaming laptop"
    price_limit = None

    if parsed_query['prices']:
        try:
            price_limit = int(parsed_query['prices'][0].replace("₹", "").replace(",", "").strip())
        except:
            pass

    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        
        for page_num in range(1, 3):
            print(f"🔁 Fetching Amazon page {page_num}...")

            url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}&page={page_num}"
            page.goto(url, timeout=60000)

            try:
                page.wait_for_selector("div.s-main-slot", timeout=60000)
            except:
                print("⏳ Timeout: Amazon page took too long to load or was blocked.")
                print("🧪 Saving page for inspection...")
                with open(f"amazon_failed_page_{page_num}.html", "w", encoding="utf-8") as f:
                    f.write(page.content())
                continue

            product_elements = page.query_selector_all("div.s-main-slot > div[data-component-type='s-search-result']")
            page_results = 0

            for element in product_elements:
                try:
                    title_el = element.query_selector("h2")
                    title = title_el.inner_text().strip() if title_el else "No title"

                    link_el = title_el.query_selector("a") if title_el else None
                    url = "https://www.amazon.in" + link_el.get_attribute("href") if link_el else "#"

                    price_el = element.query_selector(".a-price .a-offscreen")
                    price = price_el.inner_text().strip() if price_el else "Price not found"

                    rating_el = element.query_selector(".a-icon-alt")
                    rating = rating_el.inner_text().strip() if rating_el else "No rating"

                    if price != "Price not found" and price_limit:
                        price_num = int(price.replace("₹", "").replace(",", "").split(".")[0])
                        if price_num > price_limit:
                            continue

                    results.append({
                        "title": title,
                        "price": price,
                        "rating": rating,
                        "url": url
                    })
                    page_results += 1

                except Exception:
                    continue

            if page_results == 0:
                print(f"⚠️ Page {page_num} had no valid results.")
                with open(f"amazon_no_results_page_{page_num}.html", "w", encoding="utf-8") as f:
                    f.write(page.content())

        browser.close()

    return results
