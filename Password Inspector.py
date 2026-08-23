user_password = input("Enter your password: ")
password_length = len(user_password)

if password_length < 8:
    print("Password is too short. Please enter at least eight characters.")
else:
    print("Password length is acceptable.")
