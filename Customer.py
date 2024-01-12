#I made a list of names, cities and states, and the customers are created randomly from this list

import datetime, random
import pandas as pd

Customers=[]

first_name = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Bruno', 'Lucas', 'Aiden', 'Mia',
              'Ethan', 'Elijah', 'Harper', 'Abigail', 'Amelia', 'Mason', 'Ella', 'Alexander', 'Grace', 'Lily',
              'Benjamin', 'Sebastian', 'Catherine', 'Daniel', 'Mila', 'Chloe', 'Henry', 'Scarlett', 'James',
              "Natalie", "Gabriel", "Zoe", "Aria", "Sophie"]

last_name = ['Smith', 'Johnson', 'Silva', 'Santos', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodrigues', 'Martinez',
             'Jones', 'Pereira', 'Taylor', 'Anderson', 'Thomas', 'Ferreira', 'White', 'Jackson', 'Martins', 'Harris',
             'Lopez', 'Clark', 'Murray', 'Lewis', 'Mendes', 'Lee', 'Oliveira', 'Walker', 'Costa', 'Hall', "O'Brien",
             "Ryan", "Murphy", "Schmidt", 'Ferrari', "Suzuki", "Tanaka", "Yamamoto", "Watanabe", "Ito"]

Cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
          'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Indianapolis', 'Fort Worth',
          'Charlotte', 'Seattle', 'Denver', 'El Paso', 'Detroit', 'Washington', 'Boston', 'Memphis', 'Nashville',
          'Portland', 'Oklahoma City', 'Las Vegas', 'Baltimore', 'Louisville', 'Milwaukee', 'Albuquerque',
          'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Long Beach', 'Mesa', 'Atlanta', 'Colorado Springs',
          'Virginia Beach', 'Raleigh', 'Omaha', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Wichita']

States = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA', 'TX', 'FL', 'CA', 'OH', 'IN', 'TX', 'NC',
          'WA', 'CO', 'TX', 'MI', 'DC', 'MA', 'TN', 'TN', 'OR', 'OK', 'NV', 'MD', 'KY', 'WI', 'NM', 'AZ', 'CA',
          'CA', 'MO', 'CA', 'AZ', 'GA', 'CO', 'VA', 'NC', 'NE', 'FL', 'FL', 'CA', 'MN', 'OK', 'KS']

columns = ['Customer_ID', 'First_name', 'Last_name', 'Birth_date', 'email', 'Phone', 'City', 'State']

start_date = datetime.datetime(1973, 1, 1)
end_date = datetime.datetime(2023, 12, 31)


n=1
while n < 701:
    customer = []
    customer.append('C.' + str(n).zfill(3))
    cus_fn = random.choice(first_name)
    cus_ln = random.choice(last_name)
    customer.append(cus_fn)
    customer.append(cus_ln)
    customer.append(start_date + datetime.timedelta(random.randint(0, (end_date - start_date).days)))
    customer.append(cus_fn.lower() + random.choice(["_",'.']) + cus_ln.lower() + '@email.com')
    customer.append('555-' + str(random.randint(100,999)) + '-' + str(random.randint(100, 999)))
    place = random.randint(0,47)
    customer.append(Cities[place])
    customer.append(States[place])
    Customers.append(customer)
    customer = []
    n += 1


df = pd.DataFrame(Customers, columns = columns)

df.to_csv('Customer.csv', index=False)
