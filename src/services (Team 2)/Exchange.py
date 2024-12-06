import requests
from bs4 import BeautifulSoup

def exchangeRate(currencyUnit):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36"
    }
    url = f"https://www.google.com/search?q=курсы+рубля+к+{currencyUnit}"
    response = requests.get(url, headers=headers)

    getHtmlPage = BeautifulSoup(response.text, "lxml")
    span = getHtmlPage.find('span', class_="DFlfde SwHCTb")
    value = span.text.strip()
    print(f"Один Российский рубль равен {value}" + " " + currencyUnit)

if __name__ == "__main__":
    exchange = exchangeRate()