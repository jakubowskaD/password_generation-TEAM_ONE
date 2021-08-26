import random
import string

def get_num_chars():
    n = input("Type number of letters (4-60) ")
    try:
        n = int(n)
    except:
        print("Invalid input, press enter to finish")
        quit
    n = min(max(4, n), 60)
    return n

def create_password_n(n):
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    out=""
    if (len(out) < n):
        out += random.choice(string.ascii_lowercase)
    if (len(out) < n):
        out += random.choice(string.ascii_uppercase)
    if (len(out) < n):
        out += random.choice(string.digits)
    if (len(out) < n):
        out += random.choice(string.punctuation)
    
    while (len(out) < n):
        out += random.choice(all_chars)

    out = list(out)
    random.shuffle(out)
    return "".join(out)

if __name__ == "__main__":
    next_game = True
    while next_game:
        print("Password Generator")
        n = get_num_chars()
        print("Generating password", n, "characters")
        print(create_password_n(n))
        input("Press enter to finish")
        next_time_input = input("Do you want to play next time? Yes or No ?")
        if next_time_input == "No":
            next_game = False





