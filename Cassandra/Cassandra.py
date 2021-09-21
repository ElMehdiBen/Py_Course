# ETL using Pandas and Cassandra

from cassandra.cluster import Cluster
import pandas as pd

# Extract Data

cluster = Cluster(['209.188.7.148', '209.188.7.149', '209.188.7.150'],port=9042)
session = cluster.connect('mehdi', wait_for_all_pools=True)
session.execute('USE mehdi')
rows = session.execute('SELECT * FROM data')
############################################
# Transform Data
data = pd.DataFrame(rows)

data

############################################
# Load Data
# Write data to Cassandra - Creating new table

session.execute('CREATE TABLE emp_2(\
   emp_id int PRIMARY KEY,\
   emp_name text,\
   emp_city text,\
   emp_sal varint,\
   emp_phone varint\
   );')


session.execute("INSERT INTO emp_2 (emp_id, emp_name, emp_city,\
   emp_phone, emp_sal) VALUES(1,'ram', 'Hyderabad', 9848022338, 50000);")

session.execute("INSERT INTO fortype(id, card) VALUES (1,\
{'number':12, 'birth_day':'12/08/1990', 'pin':3421}\
);")

session.execute("INSERT INTO fortype(id, details) VALUES (2, {name : 'product', price : 1350});")

query = "INSERT INTO data (id, continent, location) VALUES (?, ?, ?)"
prepared = session.prepare(query)

data[0:10].apply(lambda row: session.execute(prepared, (row['id'], row['continent'], row['location'])), axis=1)

