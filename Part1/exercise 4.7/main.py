# Exercise 4.7 Threes. Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

def main():
    numbers = []
    for value in range(3, 31, 3):
        numbers.append(value)
        print(f'{value} ', end='')
    print()
    for number in numbers:
        print(f'{number}', end=' ')


if __name__ == '__main__':
    main()
