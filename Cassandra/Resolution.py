from cassandra.cluster import Cluster
import pandas as pd

# Extract Data

cluster = Cluster(['209.188.7.148'],port=9042)
session = cluster.connect('noura', wait_for_all_pools=True)
session.execute('USE noura')

data = pd.read_csv("nyc_flights.csv")

data.columns
data.info()

data.isnull().sum()

# Pas de problemes de nulls au niveau de la donnee
# Est ce que j'ai besoin de feature engineering - creation de nouvelles colonnes a partir des anciennes
# Dep / Arr delays peuvent etre positifs ou negatifs - Dep > 0 & Arr < 0 (on a pu rattraper des minutes)
# data["calc_delay"] = data["dep_delay"] + data["arr_delay"]
# calc_delay > 0 un retard / calc_delay = 0 retard rattrape ou pas de retard / calc_delay < 0 une avance


session.execute("CREATE TABLE nyc_flights(\
     year int, \
 month int, \
 day int, \
 dep_time int, \
 dep_delay int, \
 arr_time int, \
 arr_delay int, \
 carrier text, \
 tailnum text, \
 flight int, \
 origin text, \
 dest text, \
 air_time int, \
 distance int, \
 hour int, \
 minute int, \
    PRIMARY KEY ((carrier), year, tailnum));")



query = "INSERT INTO nyc_flights (year, month, day, dep_time, dep_delay, arr_time, arr_delay, carrier, tailnum, flight, origin, dest, air_time, distance, hour, minute) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
prepared = session.prepare(query)

data[0:100].apply(lambda row: session.execute(prepared, (row["year"], row["month"], row["day"], row["dep_time"], row["dep_delay"], row["arr_time"], row["arr_delay"], row["carrier"], row["tailnum"], row["flight"], row["origin"], row["dest"], row["air_time"], row["distance"], row["hour"], row["minute"])), axis=1)


# TablePlus - CQL Questions
"""
select carrier, year, sum(dep_delay), sum(arr_delay) from nyc_flights group by carrier, year

select carrier, year, sum(dep_delay), sum(arr_delay) from nyc_flights where dep_delay > 0 and arr_delay > 0 group by carrier, year ALLOW FILTERING
"""