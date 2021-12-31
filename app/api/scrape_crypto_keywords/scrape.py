from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio
import pandas as pd
import time

async def get_crypto_buzzwords():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://coinmarketcap.com/alexandria/glossary")
    page_content = await page.content()
    soup = BeautifulSoup(page_content, 'html.parser')
    cryto_buzz_words = soup.find_all('h2', attrs={'class':'sc-bdfBwQ Text-msjfkz-0 Heading-juwhnu-0 cnOLEs ehzvDo'})
    buzz_words = []
    for cryto_buzz_word in cryto_buzz_words:
        buzz_words.append([cryto_buzz_word.text])
    df = pd.DataFrame(buzz_words, columns=["buzzwords"])
    #print(df)
    df.to_csv("crypto_keywords.csv")

#asyncio.get_event_loop().run_until_complete(get_crypto_buzzwords())


async def get_crypto_names():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://coinmarketcap.com/all/views/all/")
    page_content = await page.content()
    soup = BeautifulSoup(page_content, 'html.parser')
    crypto_names = soup.find_all('a', attrs={'class':'cmc-table__column-name--name cmc-link'})

    crypto_currencies = []
    crypto_dict = {}
    final_data = []
    for crypto_name in crypto_names:
        crypto_currencies.append(crypto_name.text)
    df = pd.read_csv("crypto_keywords.csv")
    existing_list = df['buzzwords'].tolist()
    
    existing_list.extend(crypto_currencies)
    final_data = [ [x] for x in existing_list]
    crypto_dict["buzzwords"] = final_data
    final_data.append(crypto_dict)
    df1 = pd.DataFrame(final_data)
    print(df1)
    df1.to_csv("crypto_keywords.csv")
    
    #print(df)

asyncio.get_event_loop().run_until_complete(get_crypto_names())