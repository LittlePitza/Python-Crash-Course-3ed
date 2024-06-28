# Exercise 4.11 My Pizzas, Your Pizzas

def main():
    favorite_pizzas = ['pepperoni', 'extra cheese', 'mexican', 'hawaiian', 'honululu']
    friend_pizzas = favorite_pizzas[:]
    print("My favorite pizzas are:", ', '.join([pizza.title() for pizza in favorite_pizzas]))

    new_pizzas = ['margherita', 'vegetarian', 'seafood', 'meat lovers']
    friend_pizzas.extend(new_pizzas)
    friend_pizzas = [pizza for pizza in friend_pizzas if pizza not in ['mexican', 'honululu']]
    print(f'\nMy friend just tell me that his favorite pizzas are:', ', '.join([pizza.title() for pizza in friend_pizzas]))
    print(f'\nBut I know that his favorite pizzas are:', ', '.join([pizza.title() for pizza in favorite_pizzas]))


if __name__ == '__main__':
    main()
