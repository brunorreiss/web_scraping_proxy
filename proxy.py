import requests
from bs4 import BeautifulSoup
import json

proxyList = []
page = 1

while True:
    response = requests.get(f'https://free-proxy-list.net/?page={page}')
    bs = BeautifulSoup(response.text, 'lxml')

    table = bs.find('table')
    rows = table.find_all('tr')

    for row in rows[1:]:
        columns = row.find_all('td')
        ip = columns[0].text
        port = columns[1].text
        protocol = columns[6].text
        country = columns[4].text

        if protocol == 'yes' and (country == 'elite proxy' or country == 'anonymous'):
            proxy = {
                'ip': ip,
                'porta': port,
                'protocolo': protocol,
                'pais': country
            }

            proxyList.append(proxy)

    next_button = bs.find('a', class_='next')
    if not next_button:
        break

    page += 1

json_data = json.dumps(proxyList, indent=4)

with open('proxies.json', 'w') as f:
    f.write(json_data)

print(f"Total de proxies salvos: {len(proxyList)}")
