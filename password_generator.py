import random
import string
import time

def get_num_chars():
    n = input("Type number of letters (4-60) ")
    try:
        n = int(n)
    except:
        input("Invalid input, press enter to finish")
        quit
    n = min(max(4, n), 60)
    return n

def get_password_n(n):
    all_chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    out=""
    if (len(out) < n):
        out += random.choice(string.ascii_lowercase)
    if (len(out) < n):
        out += random.choice(string.ascii_uppercase)
    if (len(out) < n):
        out += random.choice(string.digits)
    if (len(out) < n):
        out += random.choice(string.punctuation)
    if (len(out) < n):
        out += random.choice(string.ascii_letters)

    while (len(out) < n):
        out += random.choice(all_chars)

    out = list(out)
    random.shuffle(out)
    return "".join(out)
        
print("Password Generator")
n = get_num_chars()
print("Generating password", n, "characters")
print(get_password_n(n))
input("Press enter to finish")


