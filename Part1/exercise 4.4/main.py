# Exercise 4.4 to 4.5 Summing a million and counting to a million


def main():
    for i in range(1, 1000001):
        print(f'Number: {i}')

    numbers = list(range(1, 1000001))
    print(f'Minimum Number: {min(numbers)}')
    print(f'Maximum Number: {max(numbers)}')
    print(f'Sum of Numbers: {sum(numbers)}')
    print(numbers)


if __name__ == '__main__':
    main()
