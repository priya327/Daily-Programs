from pymongo import MongoClient   # TOP OF FILE

client = MongoClient("mongodb://localhost:27017/")

db = client["company"]

employe = db["employee"]

employe.insert_one({
    "name": "jai",
    "salary": 50000,
    "department": "IT",
    "experience": 2
})

for emp in employe.find():
    print(emp)

employe.update_one(
    {
        "name": "jai"
    },
    {
        "$set": {
            "salary": 41000
        }
    }
)

print("updated")

