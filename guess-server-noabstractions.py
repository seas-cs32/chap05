### chap05/guess-server-noabstractions.py
import random
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind socket to address and publish contact info
        s.bind((HOST, PORT))
        s.listen()
        print("GUESS-THE-NUMBER server started. Listening on", (HOST, PORT))

        # Answer incoming connection
        conn2client, addr = s.accept()
        print('Connected by', addr)
        
        with conn2client:
            # Create a secret for this connection    
            secret = random.randint(1, 100)

            while True:   # message processing loop
                guess = conn2client.recv(1024).decode('utf-8')
                if guess == '':
                    break
                guess = int(guess)

                # Check guess against secret and respond
                if guess < secret:
                    conn2client.sendall('Too small!'.encode('utf-8'))
                elif guess == secret:
                    conn2client.sendall('Exactly! You win!'.encode('utf-8'))
                else:
                    conn2client.sendall('Too big!'.encode('utf-8'))

            print('Disconnected')

if __name__ == '__main__':
    main()
