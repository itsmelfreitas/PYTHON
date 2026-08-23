user_password = input("Enter your password: ")
password_length = len(user_password)

while password_length < 8:
    print("Password is too short. Please enter at least eight characters.")
    user_password = input("Enter your password: ")
    password_length = len(user_password)

print("Password entered successfully.")
