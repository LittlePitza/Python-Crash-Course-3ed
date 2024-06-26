# Stripping Names. Use a variable to represent a person's name, and include some whitespace characters at the
# beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.


def main():
    name = " \t\n Jonh Doe \t\n"  # Original name with whitespace characters
    print(f"Original name: {name}")  # Print original name
    print(f"Striped name: {name.strip()}")  # Print striped name
    print(f"Left stripped name: {name.lstrip()}")  # Print left stripped name
    print(f"Right stripped name: {name.rstrip()}")  # Print right stripped name


if __name__ == '__main__':
    main()  # Run the main function
