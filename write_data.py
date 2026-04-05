import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# write into a collection 'users'
doc_ref = db.collection("users").document("user_1")
doc_ref.set({
    "name": "Scarlet",
    "email": "scarletmansell@gmail.com",
    "role": "student"
})

print("Data written successfully.")