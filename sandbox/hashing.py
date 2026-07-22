import hashlib


password = "QWERTY123"

def hash_password(password):

    user_input = input("Please enter the password: ")
    return user_input

hashed_pass = hashlib.md5(password.encode()).hexdigest()



while True:
    user_input = hash_password(password)
    if user_input == password:
        print("Access granted!")
    else:
        print("Access denied!")