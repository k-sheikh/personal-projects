from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

results_list = []

product = input(
    "What product would you like to search for? (case sensitive): ")
stock_check = input(
    "Would you like to limit your search to items that are in stock? Yes/No: ")

while stock_check.lower() not in ["yes", "no"]:
    print("That was an invalid entry. Please try again")
    stock_check = input(
        "Would you like to limit your search to items that are in stock? Yes/No: ")

if stock_check.lower() == "no":
    stock_check = ""
else:
    stock_check = "N=4131"

url = f"https://www.newegg.com/global/uk-en/p/pl?d={product}{stock_check}"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# Find the number of pages of results
page_text = doc.find(class_="list-tool-pagination-text").strong
num_pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

for page in range(1, num_pages + 1):
    url = f"https://www.newegg.com/global/uk-en/p/pl?d={product}&page={page}"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    # Specify html element for items
    div = doc.find(
        class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    items = div.find_all(string=re.compile(product))
    for item in items:
        inner_list = []
        # Item description
        inner_list.append(item.split(":")[0])

        parent = item.parent
        if parent.name != "a":
            continue

        # Item weblink
        link = parent['href']
        inner_list.append(link)

        # Item price
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").find(
                "strong").string + next_parent.find(class_="price-current").find("sup").string
            inner_list.append(f"£{price}")

            # Excludes results with incomplete information
            if len(inner_list) == 3:
                results_list.append(inner_list)
            else:
                pass
        except:
            pass

# Get current date and time, and convert object to string
current_datetime = str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))

# Create filename
file_name = f"Search results {current_datetime}.txt"

with open(file_name, "w", encoding="UTF-8") as f:
    f.write(
        f"##### Search results for \"{product}\" as of {current_datetime} #####")
    for item in results_list:
        f.write(f"\n\n{item[0]}\n")     # Product name
        f.write(f"{item[1]}\n")         # Website link
        f.write(f"{item[2]}")           # Price

print("\nResults file created successfully in current directory")
