from collections import Counter
import math, random, csv, json
import json
import requests, json

def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]
with open('email.txt', 'r') as f:
        domain_counts = Counter(get_domain(line.strip())
                                for line in f
                                if "@" in line)
print(domain_counts)


if __name__ == "__main__":

    def process(date, symbol, price):
        print date, symbol, price

    print "tab delimited stock prices:"

    with open('tab_delimited_stock_prices.txt', 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            date = row[0]
            symbol = row[1]
            closing_price = float(row[2])
            process(date, symbol, closing_price)

    print

    with open('colon_delimited_stock_prices.txt', 'rb') as f:
        reader = csv.DictReader(f, delimiter=':')
        for row in reader:
            date = row["date"]
            symbol = row["symbol"]
            closing_price = float(row["closing_price"])
            process(date, symbol, closing_price)

    print

    print "writing out comma_delimited_stock_prices.txt"

    today_prices = { 'CHINESE' : 90.91, 'ENGLISH' : 41.68, 'MATH' : 64.5 }

    with open('comma_delimited_stock_SCORE.txt','wb') as f:
        writer = csv.writer(f, delimiter=',')
        for stock, price in today_prices.items():
            writer.writerow([stock, price])

    print "BeautifulSoup"




serialized = """{ "title" : "Data Science Book",
"author" : "Joel Grus",
"publicationYear" : 2014,
"topics" : [ "data", "science", "data science"] }"""
# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print deserialized

endpoint = "https://api.github.com/users/mesonhu/repos"
repos = json.loads(requests.get(endpoint).text)
for rows in repos:
    data1=rows["name"]
    print(data1)
