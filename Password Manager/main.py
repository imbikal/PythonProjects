from cryptography.fernet import Fernet

# Function to generate and save the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Uncomment this line and run the script once to generate the key
write_key()

# Ask for the master password
master_pwd = input("What is the master password? ")

# Load the key and derive the encryption key using the master password
key = Fernet(load_key())
fer = key  # Fernet instance for encryption and decryption

# View stored passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_pass = data.split("|")
                decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                print(f"User: {user} | Password: {decrypted_pass}")
    except FileNotFoundError:
        print("No passwords stored yet.")

# Add a new password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{encrypted_pwd}\n")

# Main loop
while True:
    mode = input("Would you like to add a new password or view existing (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
