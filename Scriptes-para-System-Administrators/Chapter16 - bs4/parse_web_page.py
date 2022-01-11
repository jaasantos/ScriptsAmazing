import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://www.instagram.com')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

print([parse_obj.text])

