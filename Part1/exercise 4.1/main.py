# Exercise 4.1 Pizzas.
# Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
# and then use a for loop to print the name of each pizza.

def main():
    pizzas = ['mexican', 'pepperoni', 'extra cheese']
    for pizza in pizzas:
        print(f'I love {pizza.title()} pizza!')
    print('I really love pizza!')


if __name__ == '__main__':
    main()
