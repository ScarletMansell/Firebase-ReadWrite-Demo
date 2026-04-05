import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

print("=== Write Data to Firestore ===")

collection_name = input("Enter collection name: ").strip()
num_fields = int(input("How many fields do you want to add? "))

data = {}

for i in range(num_fields):
    field_name = input(f"Enter name for field #{i + 1}: ").strip()
    field_value = input(f"Enter value for '{field_name}': ").strip()
    data[field_name] = field_value

docs = db.collection(collection_name).stream()
max_id = 0

for doc in docs:
    try:
        doc_id_num = int(doc.id)
        if doc_id_num > max_id:
            max_id = doc_id_num
    except ValueError:
        pass

next_id = str(max_id + 1)

db.collection(collection_name).document(next_id).set(data)

print("\nData written successfully.")
print(f"Collection: {collection_name}")
print(f"Document ID: {next_id}")
print("Data:", data)
