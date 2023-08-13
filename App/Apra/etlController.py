import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import re


def fromURLtoDB():
    url = "https://www.apra.gov.au/monthly-authorised-deposit-taking-institution-statistics"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    excel_links = []

    for link in soup.find_all("a"):
        href = link.get("href")

        if href and href.endswith(".xlsx"):
            excel_links.append(href)
        else:
            pass
    # Creamos las carpetas si no existen
    if not os.path.exists("./data/historical"):
        os.makedirs("./data/historical")
    if not os.path.exists("./data/monthly"):
        os.makedirs("./data/monthly")

    # Descargamos los archivos y los guardamos en las carpetas correspondientes
    for i, link in enumerate(excel_links):
        response = requests.get(link)
        filename = link.split("/")[-1].replace("%20","_")
        if i == 1:
            path = os.path.join("./data/monthly", filename)
        elif i == 2:
            path = os.path.join("./data/historical", filename)
        else:
            continue
        with open(path, "wb") as f:
            f.write(response.content)

def loadInfo(engine, data):
    files = [f for f in os.listdir(data['folder'])]
    filename = files[0]
    df = pd.read_excel(os.path.join(data['folder'],filename), sheet_name='Table 1', skiprows=1 if data['table'] == 'datos_mensuales' else '')
    columns = []
    for col in df.columns:
        col = re.sub(r'[ .,-]+', '_', col)
        columns.append(col.lower()[:64])
    df.rename( columns = {df.columns[i] : columns[i] for i in range(len(columns)) }, inplace= True )
    try:
        df.to_sql(data['table'], con=engine, if_exists='replace', chunksize=1000)
        return "Success"
    except Exception as e:
        return e

def loadDatabase(engine):
    fromURLtoDB()
    data = [
        {
            'folder': "./data/historical/",
            'table':'datos_historicos'
        },
        {
            'folder': "./data/monthly/",
            'table':'datos_mensuales'
        }
    ]
    for i in range(len(data)):
        req = loadInfo(engine, data[i])
    return req
