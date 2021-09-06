class Stats:
    def __init__(self, *args):
        self.nom = x
        self.type = "Statistiques"
        self.data = y

    def data_count(self):
        return len(self.data)

Var = Stats("data Mehdi", [1,2,3,4,5])
Var2 = Stats("data Pascal", [1,2,3,4,5,6])

print(Var2.nom)
print(Var2.type)
print(Var2.data)

print(Var2.data_count())

print(type(Var2))