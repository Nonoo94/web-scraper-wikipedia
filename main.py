from bs4 import BeautifulSoup
import requests
import csv
import lxml
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
resp = requests.get(url)
src = resp.content
soup = BeautifulSoup(src , 'lxml')

table = soup.find('table' , class_ ='wikitable sortable mw-collapsible')
table_titles = table.find_all('th')
table_title = [data.text.strip() for data in table_titles]
#print(table_title)
df = pd.DataFrame(columns = table_title)
table_columns = table.find_all('tr')
for table_column in table_columns[1:]:
    rows = table_column.find_all('td')
    row_data = [data.text.strip() for data in rows]
    #print(row_data)
    length = len(df)
    df.loc[length] = row_data
    df.to_csv(r'E:\web_scrapping_wikipedia\banks.csv' , index=False)
print("File Saved!")