# Exercise 2.4 Name Cases: Use a variable to represent a person’s name, and then print that person’s name in
# lowercase, uppercase, and title case.

import random


def generate_name():  # Generate a random name
    first_names = ['john', 'jane', 'jim', 'jill', 'jack']
    last_names = ['smith', 'jones', 'williams', 'taylor', 'brown']
    generate_full_name = random.choice(first_names) + ' ' + random.choice(last_names)
    return generate_full_name


def main():
    print("Hello " + generate_name().title() + "!")
    print("Hello " + generate_name().upper() + "!")
    print("Hello " + generate_name().lower() + "!")


if __name__ == "__main__":
    main()
