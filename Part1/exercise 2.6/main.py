# Exercise 2.6 Famous Quote 2 Repeat the previous exercise, but this time store the famous person’s name in a
# variable called famous_person. Then compose your message and store it in a new variable called message.
# Print your message.

import random # Import the random module to generate random numbers


def main():
    autor_quote = {
        "Arthur C. Clarke": ["Any sufficiently advanced technology is indistinguishable from magic.",
                             "The only way of discovering the limits of the possible is to venture a little way past "
                             "them into the impossible."],

        "Isaac Asimov": ["The saddest aspect of life right now is that science gathers knowledge faster than society ",
                         "The only constant is change, continuing change, inevitable change, that is the dominant "
                         "factor in society today."],

        "Linus Torvalds": ["Talk is cheap. Show me the code.", "Software is like sex; it's better when it's free."],

        "Ralph Johnson": ["Any fool can write code that a computer can understand. Good programmers write code that ",
                          "First, solve the problem. Then, write the code.", "Don't comment bad code—rewrite it."
                          ]
    }  # Dictionary with the quotes of the authors

    autor_select = random.choice(list(autor_quote.keys()))  # Select a random author
    quote_select = random.choice(autor_quote[autor_select])  # Select a random quote from the author

    message = f"{autor_select} once said: {quote_select}" # Compose the message
    print(message)  # Print the message


if __name__ == "__main__":
    main()  # Call the main function

