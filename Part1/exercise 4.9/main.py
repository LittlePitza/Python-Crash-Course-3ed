#  Exercise 4.9 Cube Comprehension
# Use a list comprehension to generate a list of the first 10 cubes.

def main():
    cubes = [x**3 for x in range(1, 11)]
    # Explanation: x is the variable, x**3 is the cube of x, and range(1, 11) is the range of x from 1 to 10.
    for cube in cubes:
        print(f'The cube of {cubes.index(cube) + 1} is {cube}.')
    # Explanation: cubes.index(cube) + 1 is the index of the cube in the list plus 1 to get the number of the cube.


if __name__ == "__main__":
    main()
