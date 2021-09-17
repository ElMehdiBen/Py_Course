from cassandra.cluster import Cluster

if __name__ == "__main__":
    cluster = Cluster(['209.188.7.148'],port=9042)
    session = cluster.connect('data', wait_for_all_pools=True)
    session.execute('USE data')
    rows = session.execute('SELECT * FROM users')
    for row in rows:
        print(row.age,row.name,row.username)