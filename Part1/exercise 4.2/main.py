# Exercise 4.2 Animals
# Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

def main():
    animals = ['dog', 'cat', 'bird']
    for animal in animals:
        print(f'A {animal.title()} is a great pet!')
        print(f'You can teach a {animal.title()} tricks!')
        if animal == 'dog':
            print('Dogs are loyal and friendly.\n')
        elif animal == 'cat':
            print('Cats are independent and playful.\n')

    print('\nAll of these animals make great pets!')


if __name__ == '__main__':
    main()

