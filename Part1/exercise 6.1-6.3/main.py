# Exercise 6.1 - 6.3

def print_person_details():
    people = [
        {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'},
        {'first_name': 'Jane', 'last_name': 'White', 'age': 25, 'city': 'Los Angeles'},
        {'first_name': 'Alice', 'last_name': 'Smith', 'age': 35, 'city': 'Chicago'}
    ]

    for person in people:
        print(f'Complete name: {person["first_name"]} {person["last_name"]} - Age: {person["age"]} '
              f'- City: {person["city"]} \n')


def favorite_numbers():
    numbers = [
        {'name': 'John', 'favorite_number': 10},
        {'name': 'Jane', 'favorite_number': 20},
        {'name': 'Alice', 'favorite_number': 30}
    ]
    for number in numbers:
        print(f'{number["name"]} favorite number is {number["favorite_number"]}\n')


def glossary_python():
    glossary = {
        'list': 'A collection of items in a particular order',
        'dictionary': 'A collection of key-value pairs',
        'tuple': 'An immutable list',
        'set': 'A collection in which each item must be unique',
        'if': 'A conditional statement that allows you to test a condition',
        'for': 'A loop that allows you to iterate over a collection of items',
        'while': 'A loop that continues to run as long as a certain condition is true',
        'function': 'A named block of code that can be called whenever you need it',
        'class': 'A blueprint for creating objects',
        'module': 'A file that contains code you can use in your program'
    }
    for key, value in glossary.items():
        print(f'{key.title()}: {value}\n')


def main():

    # Exercise 6.1
    print_person_details()
    # Exercise 6.2
    favorite_numbers()
    # Exercise 6.3
    glossary_python()


if __name__ == "__main__":
    main()
