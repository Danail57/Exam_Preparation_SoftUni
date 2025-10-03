import re
pattern = r"^[a-zA-Z0-9._%+-]{2,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

while True:
    email = input("Write your email or 'End': ")
    if email == "End":
        break

    if re.match(pattern, email):
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")
