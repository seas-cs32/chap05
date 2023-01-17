### chap05/guess-server-noabstractions.py
import random
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    secret = random.randint(1, 100)
    # print(f'The secret number is {secret}')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("GUESS-THE-NUMBER server started. Listening on", (HOST, PORT))

        conn, addr = s.accept()
        print('Connected by', addr)
        with conn:
            while True:
                guess = conn.recv(1024).decode('utf-8')
                if not guess:
                    break
                guess = int(guess)

                # Check guess against secret and respond
                if guess < secret:
                    conn.sendall('Too small!'.encode('utf-8'))
                elif guess == secret:
                    conn.sendall('Exactly! You win!'.encode('utf-8'))
                else:
                    conn.sendall('Too big!'.encode('utf-8'))

            print('Disconnected')

if __name__ == '__main__':
    main()
