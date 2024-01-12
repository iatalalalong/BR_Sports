#This is the Inventory. It tracks every single product, from the supplier, to the store, and finally the sale.

import csv
from random import uniform, randint, choice, choices
import pandas as pd
import uuid
from datetime import date,datetime,timedelta
from collections import Counter


#This Function creates an unique ID for every item.
def prod_id(L, i):
    pid = str(len(L)+1).zfill(6) +'.'+i['SKU'][0:4]
    return(pid)

#This function creates a transaction ID.
def tra_id(L):
    lojas = ["NY001", "CA002", "MD003", "CO004", "TX005", "TN006", "WA007"]
    indices_organizados = [[],[],[],[],[],[],[]]
    indices_organizados_bask = [[], [], [], [], [], [], []]
    indices_organizados_base = [[], [], [], [], [], [], []]
    indices_organizados_foot = [[], [], [], [], [], [], []]
    tot = 0
    #First it separates products (by the index) among the stores they are in
    for n in L:
        print(n)
        if n['Status'] == 'Sold':
            if len(n['Product_ID']) == 11:
                val = n['Store']
                ind = lojas.index(val)
                indices_organizados[ind].append(L.index(n))
            else:
                if n['Product_ID'][11] == 'b':
                    val = n['Store']
                    ind = lojas.index(val)
                    indices_organizados_bask[ind].append(L.index(n))
                if n['Product_ID'][11] == 'a':
                    val = n['Store']
                    ind = lojas.index(val)
                    indices_organizados_base[ind].append(L.index(n))
                if n['Product_ID'][11] == 'f':
                    val = n['Store']
                    ind = lojas.index(val)
                    indices_organizados_foot[ind].append(L.index(n))
    print('etapa 1')


    #Then, for each store it groups randomly (from 1 to 5) products to assign a single transaction ID.
    #All these steps had to be taken to assure that every transaction has only products from the same store.
    for n in indices_organizados:
        while len(n) > 5:
            tam_tr = randint(1, 5)
            tran_id = uuid.uuid4()
            for m in range(0, tam_tr):
                idx = choice(n)
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)
        tran_id = uuid.uuid4()
        while len(n)!= 0:
            for idx in n:
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)
    print('etapa 2')


    for n in indices_organizados_bask:
        while len(n) > 5:
            tam_tr = randint(1, 5)
            tran_id = uuid.uuid4()
            for m in range(0, tam_tr):
                idx = choice(n)
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)+'b'
        tran_id = uuid.uuid4()
        while len(n)!= 0:
            for idx in n:
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)+'b'
    print('etapa 3')

    for n in indices_organizados_base:
        while len(n) > 5:
            tam_tr = randint(1, 5)
            tran_id = uuid.uuid4()
            for m in range(0, tam_tr):
                idx = choice(n)
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)+'a'
        tran_id = uuid.uuid4()
        while len(n)!= 0:
            for idx in n:
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)+'a'
    print('etapa 4')

    for n in indices_organizados_foot:
        while len(n) > 5:
            tam_tr = randint(1, 5)
            tran_id = uuid.uuid4()
            for m in range(0, tam_tr):
                idx = choice(n)
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)+'f'
        tran_id = uuid.uuid4()
        while len(n)!= 0:
            for idx in n:
                n.remove(idx)
                L[idx]['Transaction_ID'] = str(tran_id)+'f'
    print('etapa 5')

def transacts(L, i, f):

    indices = []
    for n in range(i, f):
        if L[n]['Status'] == 'Sold':
            indices.append(n)


    while len(indices) > 7:
        tam_tr = randint(1, 7)
        tran_id = uuid.uuid4()
        for m in range(0, tam_tr):
            idx = choice(indices)
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id)

    tran_id = uuid.uuid4()
    while len(indices)!= 0:
        for idx in indices:
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id)

def transacts_NBA(L, i, f):

    indices = []
    for n in range(i, f):
        if L[n]['Status'] == 'Sold':
            indices.append(n)


    while len(indices) > 7:
        tam_tr = randint(1, 7)
        tran_id = uuid.uuid4()
        for m in range(0, tam_tr):
            idx = choice(indices)
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id)+'b'

    tran_id = uuid.uuid4()
    while len(indices)!= 0:
        for idx in indices:
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id)+'b'

def transacts_MLB(L, i, f):

    indices = []
    for n in range(i, f):
        if L[n]['Status'] == 'Sold':
            indices.append(n)


    while len(indices) > 7:
        tam_tr = randint(1, 7)
        tran_id = uuid.uuid4()
        for m in range(0, tam_tr):
            idx = choice(indices)
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id)+'a'

    tran_id = uuid.uuid4()
    while len(indices)!= 0:
        for idx in indices:
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id)+'a'

def transacts_NFL(L, i, f):

    indices = []
    for n in range(i, f):
        if L[n]['Status'] == 'Sold':
            indices.append(n)


    while len(indices) > 7:
        tam_tr = randint(1, 7)
        tran_id = uuid.uuid4()
        for m in range(0, tam_tr):
            idx = choice(indices)
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id) +'f'

    tran_id = uuid.uuid4()
    while len(indices)!= 0:
        for idx in indices:
            indices.remove(idx)
            L[idx]['Transaction_ID'] = str(tran_id) +'f'

columns = ['Product_ID', 'SKU', 'Status', 'Store', 'Transaction_ID', 'Purchase_price', 'Selling_price']
item = {'Product_ID': '', 'SKU': '', 'Status': '', 'Store': '', 'Transaction_ID': '', 'Purchase_price': '', 'Selling_price': ''}
Items = []
status = ['Sold', 'In Stock']
chances=[0.9,0.1]

#This imports stores
stores = ["NY001", "CA002", "MD003", "CO004", "TX005", "TN006", "WA007"]

#This imports the SKUs and the prices
path_prods = pd.read_csv('Products.csv')
SKUs = path_prods['SKU'].tolist()
prices = path_prods['Actual_price'].tolist()
teams = path_prods['Team'].tolist()
sports = path_prods['Sport'].tolist()



#This creates a random (between 60% and 70% of selling price) purchase price for every product
pur_prices = []
for p in prices:
    pur_price = round(p * uniform(0.6,0.7),2)
    pur_prices.append(pur_price)


#Here I've created 50 - 60 items for each product.
for k in stores:
    li= len(Items)
    print(k)
    for n in SKUs:
        tam = randint(30, 150)
        for m in range(0, tam):
            item['SKU'] = n
            item['Selling_price'] = prices[SKUs.index(n)]
            item['Purchase_price'] = pur_prices[SKUs.index(n)]
            item['Status'] = choices(status, weights=chances, k=1)[0]
            item['Store'] = k
            item['Product_ID'] = prod_id(Items, item)
            Items.append(item.copy())
    lf=len(Items)
    transacts(Items, li, lf)
    li = len(Items)
    for t in teams:
        # NBA
        if str(t) in 'Thunder StrikersLunar Legends':
            print('achou basketball')
            tam = randint(10, 20)
            for m in range(0, tam):
                item['SKU'] = SKUs[teams.index(t)]
                item['Selling_price'] = prices[teams.index(t)]
                item['Purchase_price'] = pur_prices[teams.index(t)]
                item['Status'] = 'Sold'
                item['Store'] = k
                item['Product_ID'] = str(prod_id(Items, item))
                Items.append(item.copy())
    lf = len(Items)
    transacts_NBA(Items, li, lf)
    li = len(Items)
    for t in teams:
        if str(t) in 'Cosmos CrushersStellar Stingers':
            print('achou baseball')
            tam = randint(10, 20)
            for m in range(0, tam):
                item['SKU'] = SKUs[teams.index(t)]
                item['Selling_price'] = prices[teams.index(t)]
                item['Purchase_price'] = pur_prices[teams.index(t)]
                item['Status'] = 'Sold'
                item['Store'] = k
                item['Product_ID'] = str(prod_id(Items, item)) + 'a'
                Items.append(item.copy())
        lf = len(Items)
        transacts_MLB(Items, li, lf)
        li = len(Items)
    for t in teams:
        if str(t) in 'Rapid RavensApex Avengers':
            print('achou futebol')
            tam = randint(10, 20)
            for m in range(0, tam):
                item['SKU'] = SKUs[teams.index(t)]
                item['Selling_price'] = prices[teams.index(t)]
                item['Purchase_price'] = pur_prices[teams.index(t)]
                item['Status'] = 'Sold'
                item['Store'] = k
                item['Product_ID'] = str(prod_id(Items, item)) + 'f'
                Items.append(item.copy())
        lf = len(Items)
        transacts_NFL(Items, li, lf)
        li = len(Items)






#print('NBAAA')
#for n in teams:
#    # NBA
#        tam = randint(50,100)
#        for m in range(0, tam):
#            item['SKU'] = SKUs[teams.index(n)]
#            item['Selling_price'] = prices[teams.index(n)]
#            item['Purchase_price'] = pur_prices[teams.index(n)]
#            item['Status'] = 'Sold'
#            item['Store'] = choice(stores)
#            item['Product_ID'] = str(prod_id(Items, item))+'b'
#            Items.append(item.copy())
#
#    # MLB
#    if str(n) in 'Cosmos CrushersStellar Stingers':
#        tam = randint(50,100)
#        for m in range(0, tam):
#            item['SKU'] = SKUs[teams.index(n)]
#            item['Selling_price'] = prices[teams.index(n)]
#            item['Purchase_price'] = pur_prices[teams.index(n)]
#            item['Status'] = 'Sold'
####            item['Store'] = choice(stores)
   #         item['Product_ID'] = str(prod_id(Items, item))+'a'
   #         Items.append(item.copy())
#
#    # NFL
#    if str(n) in 'Rapid RavensApex Avengers':
#        tam = randint(50,100)
#        for m in range(0, tam):
#            item['SKU'] = SKUs[teams.index(n)]
#            item['Selling_price'] = prices[teams.index(n)]
#            item['Purchase_price'] = pur_prices[teams.index(n)]
#            item['Status'] = 'Sold'
#            item['Store'] = choice(stores)
#            item['Product_ID'] = str(prod_id(Items, item))+'f'
#            Items.append(item.copy())

#for t in sports:
 #   if t == 'Hiking':
 #       for m in range(10, 25):
 #           item['SKU'] = SKUs[sports.index(t)]
 #           item['Selling_price'] = prices[sports.index(t)]
 #           item['Purchase_price'] = pur_prices[sports.index(t)]
 #           item['Store'] = 'CO004'
 #           item['Product_ID'] = prod_id(Items,item)
 #           Items.append(item.copy())




df = pd.DataFrame(Items, columns = columns)

df.to_csv('Inventory.csv', index=False)
