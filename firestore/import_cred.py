# Alternative to storing creds/tokens in .env files. Useful when passing the code around various different devices.


from tkinter import filedialog
import firebase_admin
from firebase_admin import credentials, firestore


def import_cred():
    file_path = filedialog.askopenfilename(title="Select Credential File", filetypes=[("JSON Files", "*.json")])
    return file_path




cred = credentials.Certificate(import_cred())
firebase_admin.initialize_app(cred)

db = firestore.client()
db.collection("collection").document("document").set({"User3":17, "User5":155}, merge=True)
