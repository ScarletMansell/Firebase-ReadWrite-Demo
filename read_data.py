import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection("users").document("user_1")
doc = doc_ref.get()
# get to reading document
if doc.exists:
    print("Document data:")
    print(doc.to_dict())
else:
    print("No such document.")