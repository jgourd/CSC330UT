from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from base64 import b64decode

DICTIONARY = "words.txt";

# enter the DB password below
db_password = "";

# grab the dictionary words
with open(DICTIONARY, "r") as file:
    words = file.read().splitlines()

for password in words:
    print(f"Trying: {password} on {db_password}: ", end="")

    # decrypt the password with the known symmetric key
    cipher = AES.new((bytes(password, "utf-8") + (b"\x00" * (32 - len(password))))[:32], AES.MODE_CBC, b"\x00" * 16)
    try:
        plain_password = unpad(cipher.decrypt(b64decode(db_password)), 16)
    except:
        plain_password = b""

    # display the results
    print(f"{plain_password.decode('utf-8')}")

