### chap05/guess-server.py
import random
from socket32 import create_new_socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    with create_new_socket() as s:
        # Bind socket to address and publish contact info
        s.bind(HOST, PORT)
        s.listen()
        print("GUESS-THE-NUMBER server started. Listening on", (HOST, PORT))

        # Answer incoming connection
        conn2client, addr = s.accept()
        print('Connected by', addr)

        with conn2client:
            # Create a secret for this connection    
            secret = random.randint(1, 100)

            while True:   # message processing loop
                msg = conn2client.recv()
                if msg == '':
                    break
                guess = int(msg)

                # Check guess against secret and respond
                if guess < secret:
                    conn2client.sendall('Too small!')
                elif guess == secret:
                    conn2client.sendall('Exactly! You win!')
                else:
                    conn2client.sendall('Too big!')

            print('Disconnected')

if __name__ == '__main__':
    main()
