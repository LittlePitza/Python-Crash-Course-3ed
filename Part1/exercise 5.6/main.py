# Exercise 5.6 Stages of life
import time
import random


def main():
    while True:
        age = random.randint(0, 100)
        if age < 2:
            print(f'Age: {age}\nStage of life: baby')
        if 2 <= age < 13:
            print(f'Age: {age}\nStage of life: child')
        if 13 <= age < 20:
            print(f'Age: {age}\nStage of life: teenager')
        if 20 <= age < 65:
            print(f'Age: {age}\nStage of life: adult')
        if age >= 65:
            print(f'Age: {age}\nStage of life: elder')
        time.sleep(2)


if __name__ == "__main__":
    main()
