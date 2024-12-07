from hashlib import sha256

DICTIONARY = "words.txt"

# enter the DB hash below
db_password = "";
# enter the DB salt below
db_salt = "";

# grab the dictionary words
with open(DICTIONARY, "r") as file:
    words = file.read().splitlines()

# hash each dictionary word and compare
for password in words:
    print(f"Trying: {password}")
    if (sha256(bytes.fromhex(db_salt) + password.encode("utf-8")).hexdigest() == db_password):
        # we found it!
        print("**SUCCESS!")
        break

