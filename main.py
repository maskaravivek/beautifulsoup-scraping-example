import requests
from bs4 import BeautifulSoup

def get_page_contents(url):
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    
    page = requests.get(url, headers=headers)
    
    if page.status_code == 200:
        return page.text
    return None

def get_quotes_and_authors(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    try:
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
    except Exception as e:
        print(e)
        return None, None
    return quotes, authors

if __name__ == '__main__':
    url = 'http://quotes.toscrape.com'
    page_contents = get_page_contents(url)
    
    if page_contents:
        quotes, authors = get_quotes_and_authors(page_contents)
        for i in range(len(quotes)):
            print(quotes[i].text)
            print(authors[i].text)
            print()
    else:
        print('Failed to get page contents.')