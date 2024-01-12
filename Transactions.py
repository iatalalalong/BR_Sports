#This are the Transactions info
import uuid
import csv
import pandas as pd
from random import choice, randint
from datetime import date, timedelta, datetime

#This defines the client for each transaction, depending on the store
def place(L):
    lojas = ["NY001", "CA002", "MD003", "CO004", "TX005", "TN006", "WA007"]
    for n in L:
        idx = lojas.index(n['Store_ID'])
        cliente = customers[randint((0+(100*idx)), (99+(100*idx)))]
        n['Customer_ID'] = cliente

def place2(item):
    lojas = ["NY001", "CA002", "MD003", "CO004", "TX005", "TN006", "WA007"]
    idx = lojas.index(item)
    cliente = customers[randint((0+(100*idx)), (99+(100*idx)))]
    return(cliente)

def dates(item):
    if len(item['Transaction_ID']) == 36:
        dt = datetime(2023, 1, 1) + timedelta(days=randint(1, 364))
    else:
        if item['Transaction_ID'][36] == 'b':
            dt = datetime(2023, 6, 1) + timedelta(days=randint(1, 30))
            print(f'Basket {dt}')
        if item['Transaction_ID'][36] == 'a':
            dt = datetime(2023, 10, 1) + timedelta(days=randint(1, 30))
        if item['Transaction_ID'][36] == 'f':
            dt = datetime(2023, 2, 1) + timedelta(days=randint(1, 30))
    return(dt)


columns = ['Transaction_ID', 'Transaction_value', 'Transaction_date', 'Store_ID', 'Payment_method', 'Customer_ID']

Methods = ['Cash', 'Credit', 'Debit']
transaction = {}
Transactions = []

arq_inv = 'Inventory.csv'
dados = pd.read_csv(arq_inv)
ids = dados['Transaction_ID'].tolist()


arq_cus = 'Customer.csv'
cus = pd.read_csv(arq_cus)
customers = cus['Customer_ID'].tolist()



#This assigns the total value of the transaction
val_tot = dados.groupby('Transaction_ID').agg({'Selling_price': 'sum'}).reset_index()
for a, b in val_tot.iterrows():
    transaction = {'Transaction_ID': b.iloc[0], 'Transaction_value': round(b.iloc[1],2)}
    Transactions.append(transaction.copy())
print(len(Transactions), type(Transactions))

#This creates a list with unique IDs and the store
stores = dados.drop_duplicates(subset='Transaction_ID').reset_index(drop=True)
loja = {}
Lojas = []
for a, b in stores.iterrows():
    loja = {'Transaction_ID': b.iloc[4], 'Store_ID': b.iloc[3]}
    Lojas.append(loja.copy())
print(len(Lojas), type(Lojas))

contador = 0
for n in Transactions:
    for m in Lojas:
        if n['Transaction_ID'] == m['Transaction_ID'] :
            n['Store_ID'] = m['Store_ID']
            n['Payment_method'] = choice(Methods)
            n['Transaction_date'] = dates(n)
            n['Customer_ID'] = place2(n['Store_ID'])
            Lojas.remove(m)
            contador += 1
            print(f'{contador} de {len(Transactions)}, e lojas é {len(Lojas)}')
            break



#XMAS
for x in range(0,800):
    gift = choice(Transactions)
    if len(gift['Transaction_ID']) == 36:
        gift['Transaction_date'] = datetime(2023, 12, 1) + timedelta(days=randint(1, 24))




df = pd.DataFrame(Transactions, columns = columns)

df.to_csv('Sales.csv', index=False)