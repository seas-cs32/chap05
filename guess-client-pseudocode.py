### chap05/guess-client-pseudocode.py
import socket

# Addressing information for the server

print('## Welcome to GUESS THE NUMBER! ##')

# Create a socket and call it s
    # Connect s to the server

    while True:
        # Grab a guess from the player
        while True:
            try:
                guess = int(input('Please input your guess: '))
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')

        # Use s to send guess to server
        # Wait for server to respond on s with answer to comparison
        # Print response

        # Is game over?