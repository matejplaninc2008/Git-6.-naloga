print("=== PASSWORD VALIDATOR ===")

while True:
    password = input("Vnesi geslo: ")

    upper = False
    lower = False
    number = False

for char in password:
    if char >= "A" and char <= "Z":
        upper = True

