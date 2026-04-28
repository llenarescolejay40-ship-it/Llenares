def save_user():
    try:
        username = input("Enter username: ").strip()
        
        if not username:
            raise ValueError("Username cannot be empty.")
        
        age = int(input("Enter age: "))
        
        if age <= 0:
            raise ValueError("Age must be positive.")

        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

        print("User saved!")

    except ValueError as e:
        print("Error:", e)

    finally:
        print("System complete.")


def display_users():
    try:
        with open("users.txt", "r") as file:
            print("\nSaved Users:")
            print(file.read())

    except FileNotFoundError:
        print("No users yet.")

    finally:
        print("System complete.")


save_user()
display_users()