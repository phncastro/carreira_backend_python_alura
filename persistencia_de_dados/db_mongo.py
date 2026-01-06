from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['escola']
estudantes = db['estudantes']

estudantes.insert_one({'nome': 'Pablo', 'idade': 22})

for estudante in estudantes.find():
    print(estudante)