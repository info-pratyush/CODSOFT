
import random
import string

print("\n===== Password generator =====\n")

length = int(input("Enter the length of the password: "))

char = ""

if input("\nInclude lowercase letters? (y/n): ").lower() == "y":
    char += string.ascii_lowercase

if input("\nInclude uppercase letters? (y/n): ").lower() == "y":
    char += string.ascii_uppercase

if input("\nInclude digits? (y/n): ").lower() == "y":
    char += string.digits

if input("\nInclude special characters? (y/n): ").lower() == "y":
    char += string.punctuation

if not char:
    print("No character types selected. Please try again.")

else:
    password = ''
                       
    for i in range(length):
        password += random.choice(char)

    print("\nGenerated password: " + password)