import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

print("=== All Data in Firestore ===\n")

collections = db.collections()

found_data = False

for collection in collections:
    print(f"Collection: {collection.id}")
    docs = collection.stream()

    has_docs = False
    for doc in docs:
        has_docs = True
        found_data = True
        print(f"  Document ID: {doc.id}")
        print(f"  Data: {doc.to_dict()}")
        print()

    if not has_docs:
        print("  (No documents)\n")

if not found_data:
    print("No data found in the database.")
