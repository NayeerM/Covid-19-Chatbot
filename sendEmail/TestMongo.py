from pymongo import MongoClient
client = MongoClient("mongodb+srv://covid:covid12@cluster0.2lsij.mongodb.net/Covid_19_DB?retryWrites=true&w=majority")
db = client.get_database('Covid_19_DB')
records = db.chat_records
print(records.count_documents({}))
new_chat = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}


records.remove()


