# ETL using Pandas and Cassandra

from cassandra.cluster import Cluster
import pandas as pd

# Extract Data

cluster = Cluster(['209.188.7.148'],port=9042)
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