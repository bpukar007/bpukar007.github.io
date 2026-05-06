import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("/Users/mac/desktop/books.txt", "w") as file:
    for book in books:
        title_element = book.find("h3")
        title = title_element.a["title"] if title_element and title_element.a else "No title"
        
        price_element = book.find("p", class_="price_color")
        price = price_element.text.strip() if price_element else "No price"

        rating_element = book.find("p", class_="star-rating")
        rating = "No rating"
        if rating_element:
            rating_class = rating_element.get("class")
            if len(rating_class) > 1:
                rating = rating_class[1].title() 
        
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Rating: {rating}")
        print("-" * 50)
        
        file.write(f"Title: {title}\n")
        file.write(f"Price: {price}\n")
        file.write(f"Rating: {rating}\n")
        file.write("=" * 50 + "\n")

print("Scraping complete! Check books.txt")