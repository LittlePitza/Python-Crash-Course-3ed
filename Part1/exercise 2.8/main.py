# Exercise 2.8 File Extensions.

def main(filename):
    new_file = filename.removesuffix(".txt")  # Removes the suffix ".txt" from the filename
    print(f"Filename: {filename} \nNew filename: {new_file}")  # Output: Filename: hello.txt New filename: hello


if __name__ == "__main__":
    main("hello.txt")  # Function call with the filename "hello.txt" as an argument
