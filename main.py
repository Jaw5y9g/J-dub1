def main():
    while True:
        # Display the main menu with options
        print("File Processing Menu:")
        print("1. Create a new account")
        print("2. Update an existing account")
        print("3. Read user information file")
        print("4. Quit")

        # Get the user's choice
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            create_user_account()
        elif choice == "2":
            update_user_account()
        elif choice == "3":
            read_user_info_from_file()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def create_user_account():
    # Prompt the user for the file name
    file_name = input("Enter the name of the file to create or update: ")

    # Prompt the user for their information
    user_name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")

    try:
        # Open the specified file in write mode ('w')
        with open(file_name, 'w') as file:
            # Write user information as a comma-separated line
            file.write(f"{user_name},{street_address},{phone_number}\n")
            print(f"User information written to '{file_name}' successfully.")
    except IOError as e:
        # Handle file-related errors
        print(f"Error: {e}")


def update_user_account():
    # Prompt the user for the file name
    file_name = input("Enter the name of the file to update: ")

    # Prompt the user for their information
    user_name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")

    try:
        # Open the specified file in append mode ('a')
        with open(file_name, 'a') as file:
            # Write user information as a comma-separated line
            file.write(f"{user_name},{street_address},{phone_number}\n")
            print(f"User information updated in '{file_name}' successfully.")
    except IOError as e:
        # Handle file-related errors
        print(f"Error: {e}")


def read_user_info_from_file():
    # Prompt the user for the file name to read
    file_name = input("Enter the name of the file to read: ")

    try:
        # Open the specified file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            print(f"File contents:\n{content}")
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"File '{file_name}' not found.")
    except IOError as e:
        # Handle file-related errors
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
