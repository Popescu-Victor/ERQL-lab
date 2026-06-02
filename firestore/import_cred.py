<<<<<<< HEAD
=======
# Alternative to storing creds/tokens in .env files. Useful when passing the code around various different devices.


from tkinter import filedialog
import firebase_admin
from firebase_admin import credentials, firestore


>>>>>>> 2191ca5ccb030d8368b6f1d632100d701974a4a7
def import_cred():

    from tkinter import filedialog
    import firebase_admin
    from firebase_admin import credentials, firestore


    file_path = filedialog.askopenfilename(title="Select Credential File", filetypes=[("JSON Files", "*.json")])
    return file_path

    cred = credentials.Certificate(import_cred())
    firebase_admin.initialize_app(cred)


def input_data(user_input):

    commands = user_input.lower().split(" ")

<<<<<<< HEAD
    collection_ID = commands[0]
    document_ID = commands[1]
    field_name = commands[2]
    field_value = " ".join(commands[3:])

    db = firestore.client()
    db.collection(collection_ID).document(document_ID).set({field_name: field_value}, merge=True)
=======
db = firestore.client()
db.collection("collection").document("document").set({"User3":17, "User5":155}, merge=True)
>>>>>>> 2191ca5ccb030d8368b6f1d632100d701974a4a7
