# Exercise 3.1-3.2 Names and Greetings
# Write a program that prints your name and a greeting to the screen.

def main():
    friends = ['John', 'Paul', 'George', 'Ringo']
    message = f'Hello {friends[0]}! How are you today?'
    message2 = f'Hello {friends[1]}! How are you today?'
    message3 = f'Hello {friends[2]}! How are you today?'
    message4 = f'Hello {friends[3]}! How are you today?'
    print(f'My friends are {friends[0]}, {friends[1]}, {friends[2]}, and {friends[3]}.')
    print(f'{message}\n{message2}\n{message3}\n{message4}')


if __name__ == '__main__':
    main()
