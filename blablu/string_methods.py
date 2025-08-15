user_name = input("Enter your username: ")

if len(user_name) > 12:
    print("Your username is too long (12 character max)")
elif not user_name.find(" ") == -1:
    print("Your username must not contain space")
elif not user_name.isalpha():
    print("Your username must not include a number")
else:
    print(f"Welcome {user_name}")
    