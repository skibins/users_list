def delete_user(people_dict):
    # Ask the user if they want to delete a user from the dictionary.
    deleteUser = input("Are you sure that you want to delete a user? (Y/N) ")
    while deleteUser.lower() == "y":
        # Prompt the user to provide the ID of the user they want to delete.
        userId = input("Provide the user's ID: ")
        # Delete the user from the dictionary based on the provided ID.
        del people_dict[userId]

        # Print the updated list of users after the deletion.
        print("Users list after the update:")
        for userId, userData in people_dict.items():
            print(userId, ":", userData)

        # Ask the user if they want to delete another user.
        deleteUser = input("Do you want to delete another user? (Y/N) ")


def find_user(people_dict):
    # Prompt the user to enter the ID of the user they want to find.
    wantedUserId = input("Enter the wanted user's ID: ")
    userFound = False

    # Iterate through the dictionary to find the user with the provided ID.
    for userId, userData in people_dict.items():
        if userId == wantedUserId:
            # If the user is found, print their data.
            print("User data:")
            for key in userData:
                print(key, ":", userData[key])
            userFound = True

    # If the user is not found, print a message indicating so.
    if not userFound:
        print("User not found.")


def add_new_user(people_dict):
    wantNewUser = "Y"
    while wantNewUser.lower() == "y":
        # Generate a new user ID based on the current number of users in the dictionary.
        userId = str(len(people_dict))
        # Prompt the user to enter the details of the new user.
        userName = input("New user's name: ")
        userAge = int(input("New user's age: "))
        userSex = input("New user's sex: ")

        # Create a dictionary representing the new user's data.
        newRecord = {'name': userName, 'age': userAge, 'sex': userSex}
        # Add the new user to the dictionary with the generated ID.
        people_dict[userId] = newRecord

        # Ask the user if they want to add another user.
        wantNewUser = input("Do you want to add another user? (Y/N) ")


people = {
    "0": {'name': 'John', 'age': 27, 'sex': 'Male'},
    "1": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    "2": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "3": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
    "4": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
    "5": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
    "6": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
    "7": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
    "8": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "9": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
}

# Prompt the user to choose an action (find user, delete user, or add user).
choseAction = input("Choose an action: find user(1), delete user(2), add user(3) (To exit type 'esc'): ")

# Continue executing the chosen action until the user decides to exit.
while choseAction in ['1', '2', '3']:
    if choseAction == '1':
        # Execute the function to find a user in the dictionary.
        find_user(people)
    elif choseAction == '2':
        # Execute the function to delete a user from the dictionary.
        delete_user(people)
    elif choseAction == '3':
        # Execute the function to add a new user to the dictionary.
        add_new_user(people)
        # Print the updated list of users after adding a new user.
        print("Users list after an update:")
        for uId, uData in people.items():
            print(uId, ":", uData)
    else:
        # If no valid option is selected, print a message indicating so.
        print("No option selected.")

    # Prompt the user to choose another action.
    choseAction = input("Choose an action: find user(1), delete user(2), add user(3) (To exit type 'esc'): ")

# Print a message indicating the termination of the program.
print("Program terminated.")
