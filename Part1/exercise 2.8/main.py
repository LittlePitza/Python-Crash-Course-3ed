# Exercise 2.8 File Extensions.

def main(filename):
    new_file = filename.removesuffix(".txt")
    print(f"Filename: {filename} \nNew filename: {new_file}")


if __name__ == "__main__":
    main("hello.txt")
