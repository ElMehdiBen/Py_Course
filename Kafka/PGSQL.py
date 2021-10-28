import psycopg2


connection = psycopg2.connect(user="postgres",
                              password="123456789",
                              host="209.188.7.148",
                              port="5432",
                              database="data")
cursor = connection.cursor()
cursor.execute("select * from public.customers")

# fetchone is used to get line by line from PGSQL
row = cursor.fetchone()

# fetchall is used to get all the lines at once
DF = pd.DataFrame(cursor.fetchall())
