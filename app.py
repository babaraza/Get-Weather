import requests
from bs4 import BeautifulSoup

# TODO:
#   Get historical temperature reading from api or website
#   Open Existing Excel file for appending data
#   Append Temperature readings in correct columns


url = 'https://www.wunderground.com/history/monthly/KSGR/' \
      'date/2017-8?req_city=Richmond&req_state=TX&req_statename=Texas&reqdb' \
      '.zip=77469&reqdb.magic=1&reqdb.wmo=99999'

s = requests.Session()
resp = s.get(url)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")

test = soup.findAll('td')

print(soup)
# for header in test:
#     if header.text == "Avg Temperature":
#         print("found it")
#     else:
#         print("not working")