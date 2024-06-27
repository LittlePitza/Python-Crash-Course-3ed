# Exercise 3.4 - 3.7 Guest List, Changing Guest List, More Guests, Shrinking Guest List
"""Summary 3.4 to 3.7: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list
that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each
person, inviting them to dinner."""

# 3.4 Guest List


def main():
    # List of guests
    guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
    # Print invitation message to each guest
    for guest in guests:
        print(f"Hello {guest}, I would like to invite you to dinner.")
    print(f'Error: {guests[-1]} is not available to attend the dinner.')
    print(f'Searching for a new guest to invite...')
    # New guest
    new_guest = 'Nikola Tesla'
    print(f'Found a new guest to invite, is {new_guest}.')
    # Replace guest
    guests[-1] = new_guest
    # Print a new invitation message to last guest
    print(f"Hello {guests[-1]}, I would like to invite you to dinner.")
    # Add more guests
    print('We found a bigger table, so we can invite more guests.')
    guests_forgotten = ['Galileo Galilei', 'Charles Darwin']
    # Insert new guests to the beginning of the list
    guests.insert(0, guests_forgotten[0])
    guests.insert(2, guests_forgotten[1])
    guests.append('Stephen Hawking')
    # Print invitation message to each guest
    for guest in guests:
        print(f"Hello {guest}, I would like to invite you to dinner.")

    # Shrinking guest list
    print('We can only invite two guests for dinner.')
    # Remove guests from the list
    print(f"Sorry {guests.pop()}, we can't invite you to dinner.")
    print(f"Sorry {guests.pop()}, we can't invite you to dinner.")
    print(f"Sorry {guests.pop()}, we can't invite you to dinner.")
    print(f"Sorry {guests.pop()}, we can't invite you to dinner.")
    # Print invitation message to each guest
    for guest in guests:
        print(f"Hello {guest}, I would like to invite you to dinner.")

    # Remove guests from the list using del
    del guests[0]
    print(f"Sorry {guests[0]}, we can't invite you to dinner.")
    # Empty list
    guests.clear()
    print(guests)


if __name__ == '__main__':
    main()