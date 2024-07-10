def greet_users(users):
    if not users:
        print("We need to find some users!")
        return

    for user in users:
        if user.lower() == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        elif user.lower() == 'pizza':
            print(f"Hello {user}, would you like to control the world?")
        else:
            print(f"Hello {user}, thank you for logging in again.")


def exercise_5_10():
    current_users = {'admin', 'pizza', 'cremo', 'pinguin', 'random_guy78'}
    new_users = ['Pizza', 'Cremo', 'Pinguin', 'Random_guy78', 'MangoMaker', 'Car_guy23', 'Applesucks_99']
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Sorry {new_user}, that name is already taken.")
        else:
            print(f"Great! {new_user} is available.")


def main():
    print('Chapter 5 - If Statements')
    print('Exercise 5.8 & 5.9 Combined')
    users = ['admin', 'Pizza', 'Cremo', 'Pinguin', 'Random_guy78']
    greet_users(users)
    print('Exercise 5.10 Optimized')
    exercise_5_10()


if __name__ == '__main__':
    main()
