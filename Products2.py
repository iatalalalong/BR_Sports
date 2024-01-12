#This list creates a catalog of all the products.
from random import choice, randint, uniform
import pandas as pd

#This function creates a SKU (Stock Keeping Unit) for every different product (considering, color, size, etc)
def SKU(lista):
    for item in lista:
        brands = ['PrecisionPlay', 'Legendz', 'Jupiter Sports', 'X Trophy','PowerPinnacle','VelocityGear','Legendz',
                 'EnduranceGear', 'SprintTech Co', 'TrekTrailblazers', 'SummitStriders', 'RidgeRangers', '2Spin Bikes',
                 'BR Bikes', 'EpicDunk Co', 'Elevate Sports']
        sports = ['Basketball', 'Soccer', 'Football', 'Baseball', 'Running', 'Hiking', 'Cycling']
        sku_id = str(lista.index(item)).zfill(4)
        sku_cat = str(category.index(item['Category'])).zfill(2)
        sku_sc = str(sub_category.index(item['Sub_Category'])).zfill(2)
        sku_bd = str(brands.index(item['Brand'])).zfill(2)
        sku_sp = str(sports.index(item['Sport'])).zfill(2)
        if isinstance(item['Size'],str):
            sku_sz = item['Size'][0:1].capitalize()
        else:
            sku_sz = str(int((float(item['Size'])*2))-13).zfill(2)
        sku_co = item['Color'][0:2].upper()
        sku = sku_id +'-'+sku_cat +'-'+sku_sc +'-'+sku_bd +'-'+sku_sp +'-'+sku_sz +'-'+sku_co
        item['SKU'] = sku



basketball_teams = ['Thunder Strikers', 'Sky Raptors', 'Blaze Dunkers', 'Quantum Hoopers', 'Velocity Vipers',
                    'Nova Breakers', 'Eclipse Titans', 'Lunar Legends']
soccer_teams = ['Palm Trees', 'Phoenix Prowess', 'Cerulean Cyclones', 'Aurora Aces', 'Eclipse Envoys',
                'Blaze Blazers']
football_teams = ['Crimson Cavaliers', 'Crimson Chargers', 'Rapid Ravens', 'Savage Stallions', 'Blaze Buccaneers',
                  'Thunder Tornadoes', 'Apex Avengers', 'Spire Spiders']
baseball_teams = ['Cosmos Crushers', 'Stellar Stingers', 'Fusion Falcons', 'Gotham Bats', 'Silver Arrows']
teams = [basketball_teams, soccer_teams, football_teams, baseball_teams]

brand = ['PrecisionPlay', 'Legendz', 'Jupiter Sports', 'X Trophy']
category = ['Equipment', 'Clothing', 'Shoes']
sub_category = ['Jersey', 'Shorts', 'Shoes', 'Cleats', 'Boots', 'NA', 'Shirt','Urban', 'MTB', 'Urban', 'Speed', 'MTB']
color = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Black', 'White', 'Purple']
sport = ['Basketball', 'Soccer', 'Football', 'Baseball', 'Running', 'Hiking', 'Cycling']
size = ['S', 'M', 'L', 'XL']

Products = []
product = {'SKU':'', 'Product_name':'', 'Brand':'', 'Actual_price':'', 'Category':'', 'Sub_Category':'', 'Sport':'',
           'Size':'', 'Color':'', 'Team':''}
columns = ['SKU', 'Product_name', 'Brand', 'Actual_price', 'Category', 'Sub_Category', 'Sport', 'Size', 'Color', 'Team']



###--JERSEY AND SHORTS--###

# Both of color choices are random, but it checks if the 2nd color is the same as the first, and tries again
# in case it's the same

#'product' is for Jerseys and 'product_2' is for shorts
sp = 0
for g in teams:
    for t in g:
        product['Product_name'] = t + "'s " + 'Jersey'
        product['Brand'] = choice(brand)
        product['Actual_price'] = round(uniform(35.00, 100.00), 2)
        shorts_price = round(uniform(10.00, 30.00), 2)
        product['Category'] = category[1]
        product['Sub_Category'] = sub_category[0]
        product['Sport'] = sport[sp]
        product['Team'] = t
        for c in range(0,2):
            cor = choice(color)
            if c == 1:
                while cor == product['Color']:
                    cor = choice(color)
                product['Color'] = cor
            else:
                product['Color'] = cor
            for s in size:
                product['Size'] = s
                product_2 = product.copy()
                product_2['Product_name'] = t + "'s " + 'Shorts'
                product_2['Actual_price'] = shorts_price
                product_2['Sub Category'] = sub_category[1]
                Products.append(product.copy())
                Products.append(product_2.copy())
    sp += 1


###--SHOES--###
basketball_shoes = ['Air Thrive', 'Flying Pro', 'Stealth Stride', 'Sky Surge']
soccer_shoes = ['Precision Predators', 'Power Kicks', 'TurboStrike', 'Cleat Catalyst']
running_shoes = ['SwiftStride', 'Light SPD', 'VelocityVenture','MarathonMomentum', 'Velox Vortex']
bike_shoes = ['Elite Bike', 'Le Clip', 'Pedal9']
hiking_boots = ['TrekTrailblazers', 'SummitStriders', 'RidgeRangers']
shoes = [basketball_shoes, soccer_shoes, running_shoes, hiking_boots, bike_shoes]
shoe_color = ['White', "Black", 'Red', 'Blue']
boot_color = ['Black', 'Brown']
shoes_brands = ['PrecisionPlay', 'PowerPinnacle','VelocityGear']
sport = ['Basketball', 'Soccer', 'Running', 'Hiking','Cycling']

sp=0
for g in shoes:
    for t in g:
        product['Actual_price'] = round(uniform(40.00, 120.00), 2)
        product['Category'] = category[2]
        product['Sport'] = sport[sp]
        product['Team'] = 'NA'
        if g != hiking_boots:
            if g == soccer_shoes:
                product['Product_name'] = t + " Cleats"
                product['Sub_Category'] = sub_category[3]
            else:
                product['Product_name'] = t + " Shoes"
                product['Sub_Category'] = sub_category[2]
            if g == bike_shoes:
                product['Brand'] = shoes_brands[2]
            else:
                product['Brand'] = choice(shoes_brands)
            product['Color'] = choice(color)
            for s in range(14, 20):
                if g == basketball_shoes:
                    s += 2
                product['Size'] = round((s / 2), 1)
                Products.append(product.copy())
        else:
            product['Product_name'] = t + " Boots"
            product['Sub_Category'] = sub_category[4]
            product['Brand'] = shoes_brands[1]
            for c in boot_color:
                product['Color'] = c
                for s in range(14, 20):
                    product['Size'] = round((s / 2), 1)
                    Products.append(product.copy())
    sp +=1


###--EQUIPMENT--###

#To make the equipment prices feasible I made a list of prices along with the equiments.

#Basketball
b_brands = ['EpicDunk Co', 'Elevate Sports']
basket_eq = ["Professional Basketball", "Basketball Hoop", "Basketball Net"]
basket_eq_p = [30.00, 250.00, 25.00]

for e in basket_eq:
    for c in b_brands:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = basket_eq_p[basket_eq.index(e)] + randint(-5,20)
        product['Category'] = category[0]
        product['Sub_Category'] = sub_category[5]
        product['Sport'] = 'Basketball'
        product['Color'] = 'Unique'
        product['Size'] = 'Unique'
        product['Team'] = 'NA'
        Products.append(product.copy())



#Soccer
soccer_eq = ["Professional Soccer Ball", "Training and Practice Net", "Professional Goalkeeper Gloves"]
soccer_eq_p = [30.00, 50.00, 50.00]
s_brand = ['Legendz', 'X Trophy']

for e in soccer_eq:
    for c in s_brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = soccer_eq_p[soccer_eq.index(e)] + randint(-5,20)
        product['Category'] = category[0]
        product['Sub_Category'] = sub_category[5]
        product['Sport'] = 'Soccer'
        product['Team'] = 'NA'
        if e != "Professional Goalkeeper Gloves":
            product['Color'] = 'Unique'
            product['Size'] = 'Unique'
            Products.append(product.copy())
        else:
            for cor in ('Black', 'White'):
                product['Color'] = cor
                for tam in size:
                    product['Size'] = tam
                    Products.append(product.copy())


#Football
football_eq = ["Professional Football", 'Shoulder Pads', 'Professional Helmet']
football_eq_p = [40.00, 80.00, 60.00]
F_brand = ['Legendz', 'X Trophy']

for e in football_eq:
    for c in F_brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = football_eq_p[football_eq.index(e)] + randint(-5,20)
        product['Category'] = category[0]
        product['Sub_Category'] = sub_category[5]
        product['Sport'] = 'Football'
        product['Color'] = "Unique"
        product['Team'] = 'NA'
        if e != 'Shoulder Pads':
            product['Size'] = 'Unique'
            Products.append(product.copy())
        else:
            for tam in size:
                product['Size'] = tam
                Products.append(product.copy())


#Baseball
baseball_eq = ["Professional Baseball", 'Baseball Bat', 'Baseball Gloves']
baseball_eq_p = [20.00, 60.00, 50.00]
ba_brand = ['Legendz', 'PrecisionPlay']

for e in baseball_eq:
    for c in ba_brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = baseball_eq_p[baseball_eq.index(e)] + randint(-5,10)
        product['Category'] = category[0]
        product['Sub_Category'] = sub_category[5]
        product['Sport'] = 'Baseball'
        product['Color'] = "Unique"
        product['Size'] = 'Unique'
        product['Team'] = 'NA'
        Products.append(product.copy())



#Running
running_eq = ["Hydration Belt",  "Fitness Tracker", 'Energy Gel Flask']
running_eq_p = [25.00, 35.00, 15.00]
brand = ['EnduranceGear', 'SprintTech Co']

for e in running_eq:
    for c in brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = running_eq_p[running_eq.index(e)] + randint(-1,5)
        product['Category'] = category[0]
        product['Sub Category'] = sub_category[5]
        product['Sport'] = 'Running'
        product['Color'] = "Unique"
        product['Size'] = 'Unique'
        product['Team'] = 'NA'
        Products.append(product.copy())


#Running Shirts and Shorts
running_cl = ['Dry Fit Shirt', "Dry Fit Shorts"]
r_brand = ['EnduranceGear', 'SprintTech Co']
color_ru_cl= ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Black', 'White', 'Purple']

for e in running_cl:
    for c in r_brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = round(uniform(10.00, 25.00), 2)
        product['Category'] = category[1]
        product['Team'] = 'NA'
        if e =='Dry Fit Shirt':
            product['Sub_Category'] = sub_category[6]
        else:
            product['Sub_Category'] = sub_category[1]
        product['Sport'] = 'Running'
        for c in range(0, 2):
            product['Color'] = color_ru_cl.pop()
            for s in size:
                product['Size'] = s
                Products.append(product.copy())
        color_ru_cl = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Black', 'White', 'Purple']


#Hiking and camping
hiking_eq = ['Trekking Poles', 'Headlamp', 'GPS Compass', 'Backpack', 'Tent']
hiking_eq_p = [50.00, 30.00, 100.00, 75.00, 250.00]
h_brand = ['TrekTrailblazers', 'SummitStriders', 'RidgeRangers']

for e in hiking_eq:
    for c in h_brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = hiking_eq_p[hiking_eq.index(e)] + randint(-2,25)
        product['Category'] = category[0]
        product['Sub_Category'] = sub_category[5]
        product['Sport'] = 'Hiking'
        product['Team'] = 'NA'
        if e == 'Backpack' or 'Tent':
            for cor in ('Green', 'Gray', 'Blue'):
                product['Color'] = cor
                for tam in ('S','L'):
                    product['Size'] = tam
                    if tam == 'L':
                        product['Actual_price'] += 10.00
                        Products.append(product.copy())
        else:
            product['Size'] = 'Unique'
            product['Color'] = 'Unique'
            Products.append(product.copy())


#Cycling Equipment
bike_eq = ['Handlebar Grips', 'Gear Set', 'Cycling Helmet', 'GPS Bike Computer', 'Suspension Fork', 'Disc Brakes',
              'LED Bike Lights', 'Saddle', ' Water Bottle Cage', 'Repair Kit']
bike_eq_p = [12.00, 100.00, 50.00, 150.00, 200.00, 50.00, 30.00, 50.00, 5.00, 20.00]
bi_brand = ['2Spin Bikes', 'BR Bikes']

for e in bike_eq:
    for c in bi_brand:
        product['Brand'] = c
        product['Product_name'] = product['Brand'] + "'s " + e
        product['Actual_price'] = bike_eq_p[bike_eq.index(e)] + randint(-1,20)
        product['Category'] = category[0]
        product['Sub_Category'] = sub_category[5]
        product['Sport'] = 'Cycling'
        product['Size'] = 'Unique'
        product['Team'] = 'NA'
        if e == 'Cycling Helmet':
            for cor in ('Black', 'White', 'Red'):
                product['Color'] = cor
                Products.append(product.copy())
        else:
            product['Color'] = 'Unique'
            Products.append(product.copy())


#Bikes
bikes = ['VelocityViper', 'TrailBlaze Raptor', 'CruiserComet', 'SpeedStrider', 'AeroAvalanche']
bikes_p = [250.00, 600.00, 800.00, 1000.00, 1250.00]
bikes_color = ['White', "Black", 'Red', 'Silver']
bikes_sc = ['Urban', 'MTB', 'Urban', 'Speed', 'MTB']
for e in bikes:
    product['Brand'] = choice(brand)
    product['Product_name'] = e
    product['Actual_price'] = bikes_p[bikes.index(e)]
    product['Category'] = category[0]
    product['Sub Category'] = bikes_sc[bikes.index(e)]
    product['Sport'] = 'Cycling'
    product['Size'] = 'Unique'
    product['Team'] = 'NA'
    for c in range(0,2):
        cor = choice(bikes_color)
        if c == 1:
            while cor == product['Color']:
                cor = choice(bikes_color)
            product['Color'] = cor
            Products.append(product.copy())
        else:
            product['Color'] = cor
            Products.append(product.copy())


SKU(Products)

itens = [[valor for valor in item.values()] for item in Products]

for n in itens:
    print(f'{n}\n')

df = pd.DataFrame(Products, columns = columns)

df.to_csv('Products.csv', index=False)