from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd

CoinData = []

driverlink = "./DRIVER/chromedriver"
url = "https://coinmarketcap.com/coins/"
def get_coins():
    print("Starrting the script...")
    browser = webdriver.Chrome(driverlink)
    time.sleep(1)
    browser.get(url)
    time.sleep(5)
    browser.execute_script("window.scrollBy(0,925)", "")
    time.sleep(1)
    browser.execute_script("window.scrollBy(0,925)", "")
    time.sleep(1)
    browser.execute_script("window.scrollBy(0,925)", "")
    time.sleep(1)
    browser.execute_script("window.scrollBy(0,925)", "")
    time.sleep(2)
    html = browser.page_source
    Soup = BeautifulSoup(html, 'lxml')
    table = Soup.find('table')
    tbody = table.find('tbody')
    tableData = tbody.findAll('tr')
    sno = 1
    for Coin in tableData[:50]:
        Link = "https://coinmarketcap.com" + (Coin.find('a', href=True))["href"]
        Name = (Coin.find('p', class_="sc-1eb5slv-0 iJjGCS")).get_text()
        Symbol = (Coin.find('p',class_="sc-1eb5slv-0 gGIpIK coin-item-symbol")).get_text()
        # print(sno)
        # print((Coin.find('a',href=True))["href"])
        # print((Coin.find('p',class_="sc-1eb5slv-0 gGIpIK coin-item-symbol")).get_text())
        # print((Coin.find('p', class_="sc-1eb5slv-0 iJjGCS")).get_text())
        CoinData.append([sno,Name,Symbol,Link])
        print([sno,Name,Symbol,Link])
        print("-----------------------------------------------------------------------")
        sno += 1
    df = pd.DataFrame(CoinData)    #creating pandas dataframe
    df.to_csv('Dataset.csv',mode="a", header=False, index=False,)  #saving the dataframe in form of csv file

get_coins()
