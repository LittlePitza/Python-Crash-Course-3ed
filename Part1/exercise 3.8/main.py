# Exersice 3.8 Seeing the World.

def main():
    locations = ['japan', 'swiss', 'norway', 'italy', 'england']
    print(f'Temporarily sorted in alphabetical order: {sorted(locations)}')
    print(f'Original list: {locations}')
    # Sorting the list in reverse alphabetical order
    print(f'Temporarily sorted in reverse alphabetical order: {sorted(locations, reverse=True)}')
    print(f'Original list: {locations}')  # Original list is not changed
    locations.reverse()  # Reversing the list
    print(f'Reversed list: {locations}')  # Reversed list
    locations.reverse()  # Reversing the list again to get the original list
    print(f'Original list: {locations}')  # Original list again
    locations.sort()
    print(f'Sorted list: {locations}')
    locations.sort(reverse=True)  # Sorting the list in reverse alphabetical order
    print(f'Reverse sorted list: {locations}')


if __name__ == "__main__":
    main()
