# Exercise 4.13 Buffet

def main():
    menu = ('pizza', 'hamburger', 'hotdog', 'pasta', 'salad')
    print('Welcome to the buffet!\nPick your favorite food from the menu below and enjoy your evening!\n')
    for food in menu:
        print(f'Plate {menu.index(food)+1}: {food}')

    # menu[0] = 'sushi' # This line will raise an error because tuples are immutable
    menu = ('sushi', 'hamburger', 'hotdog', 'pasta', 'salad')
    print('\nOur menu has been updated!\n')
    for food in menu:
        print(f'Plate {menu.index(food)+1}: {food}')  # This is a better way to print the menu


if __name__ == "__main__":
    main()
