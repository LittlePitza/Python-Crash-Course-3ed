# Exercise 4.7 Odd Numbers
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to
# print each number.


def main():
    add_numbers = []
    for i in range(1, 21, 2):
        add_numbers.append(i)
        print(add_numbers)

    for number in add_numbers:
        print(number)


if __name__ == "__main__":
    main()
