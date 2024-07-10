# Exercise 5.3 - 5.5 Alien Colors

import random
import time


def main():

    # Exercise 5.3
    # alien_color = "red"
    # if alien_color.lower() == "green":
    # print(f'You have earned 5 Points! {alien_color.capitalize()} Alien')
    # else:
    # print(f'You have earned 10 Points! {alien_color.capitalize()} Alien')

    # Exercise 5.4
    alien_colors = ["green", "yellow", "red"]
    alien_color = random.choice(alien_colors)
    if alien_color.lower() == "green":
        print(f'You have earned 5 Points for shooting the {alien_color.capitalize()} Alien!')
    elif alien_color.lower() == "yellow":
        print(f'You have earned 10 Points for shooting the {alien_color.capitalize()} Alien!')
    else:
        print(f'You have earned 15 Points for shooting the {alien_color.capitalize()} Alien!')
    # Sleep for 2 seconds
    time.sleep(2)


if __name__ == "__main__":
    main()
