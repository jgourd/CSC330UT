from bcrypt import checkpw

DICTIONARY = "words.txt"

# enter the DB hash below
db_hash = "";

# grab the dictionary words
with open(DICTIONARY, "r") as f:
    words = f.read().splitlines()

# hash each dictionary word and compare
for password in words:
    print(f"Trying: {password}")
    if (checkpw(password.encode("utf-8"), db_hash.encode("utf-8"))):
        # we found it!
        print("**SUCCESS!")
        break
