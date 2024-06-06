### chap05/guess-client.py
from socket32 import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def main():
    print('## Welcome to GUESS THE NUMBER! ##')

    with create_new_socket() as s:
        s.connect(HOST, PORT)

        while True:   # our game loop
            # Grab a guess from the player
            while True:
                try:
                    guess = int(input('Please input your guess: '))
                    break
                except ValueError:
                    print('Guesses must be an integer. Try again...')

            s.sendall(str(guess))
            response = s.recv()
            print(response)

            if response == 'Exactly! You win!':
                break

if __name__ == '__main__':
    main()
