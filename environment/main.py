import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import html

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

dados = []
for item in soup.find_all('div', class_='quote'):
    autor = item.find('small', class_='author').get_text(strip=True)
    frase = item.find('span', class_='text').get_text(strip=True)
    
    frase = html.unescape(frase)

    dados.append({
        'Autor': autor,
        'Frase': frase
    })

# Cria um dataframe
dataframe = pd.DataFrame(dados)

#exporta para um arquivo csv
dataframe.to_csv('citações.csv', index=False, encoding='utf-8')

print('Arquivo gerado com sucesso!')