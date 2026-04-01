from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

def main():
    url = "https://pages.daraz.lk/wow/gcp/route/daraz/lk/upr/router?spm=a2a0e.tm80449416.1949364570.2.24ea61402ffb8M&hybrid=1&data_prefetch=true&prefetch_replace=1&at_iframe=1&wh_pid=%2Flazada%2Fmegascenario%2Flk%2F4_4_26_lk%2FMensFashion&trafficSource=TT"
    scrape_infinite_scroll(url)

def scrape_infinite_scroll(url):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        last_height = page.evaluate("document.body.scrollHeight")
        count = 0

        while True:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            # give time to load data because slow internet
            time.sleep(5)

            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

            count += 1
            if count > 30:
                break

        page_content = page.content()
        browser.close()

        soup = BeautifulSoup(page_content, 'html.parser')

        product_cards = extract_product_cards(soup)

        write_to_csv(product_cards)

def extract_product_cards(soup):

    product_cards = soup.find_all('a', class_='jfy-product-card-component-pc')
    products = []

    for product in product_cards:

        link = product.get('href')
        if link.startswith('//'):
            link = 'https:' + link

        title = product.find('span', class_='product-card-title').text.strip()

        price = product.find('div', class_='lzd-base-component-price-react-pc')
        if price:
            price_discount = price.find('span', class_='lzdPriceDiscountPCV2').text.strip()
            price_origin = price.find('span', class_='lzdPriceOriginPCV2').text.strip() if price.find('span', class_='lzdPriceOriginPCV2') else 'No original price'

        img_tag = product.find('img')
        img_url = img_tag['src'] if img_tag else 'No image URL'

        product_data = {
            'title': title,
            'link': link,
            'discounted_price': price_discount,
            'original_price': price_origin,
            'image_url': img_url
        }

        products.append(product_data)

    return products

def write_to_csv(products):

    with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link', 'discounted_price', 'original_price', 'image_url'])

        writer.writeheader()

        for product in products:
            writer.writerow(product)

    print(f"{len(products)} items written to products.csv")

if __name__ == "__main__":
    main()
