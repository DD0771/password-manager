from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    return open("key.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def save_password(service, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.txt", "a") as f:
        f.write(f"{service} | {encrypted_password.decode()}\n")

def load_passwords():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            service, encrypted_password = line.split("|")
            print(f"Service: {service.strip()}, Password: {decrypt_password(encrypted_password.strip())}")

while True:
    mode = input("Hi Denil, would you like to add a new password or view existing ones? (view/add), press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        load_passwords()
    elif mode == "add":
        service = input("Enter the service name: ")
        password = input("Enter the password: ")
        save_password(service, password)
    else:
        print("Invalid mode.")
        
