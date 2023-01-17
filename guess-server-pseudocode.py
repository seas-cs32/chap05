### chap05/guess-server-pseudocode.py
import random
from socket32 import create_new_socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

secret = random.randint(1, 100)
# print(f'The secret number is {secret}')

with create_new_socket() as s:
    # Bind socket to address and publish contact info

    # Answer incoming connection
    print('Connected by <client>')
    
    # Send and receive messages through the connection

        while True:
            guess = # recv guess from client
            guess = int(guess)

            # Check guess against secret and respond
            if guess < secret:
                # sendall('Too small!')
            elif guess == secret:
                # sendall('Exactly! You win!')
            else:
                # sendall('Too big!')

    # If we get here, client broke connection
