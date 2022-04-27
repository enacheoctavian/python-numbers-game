from client_server import Client

client = Client()
clientInput = input(
    "    Welcome to  the GREATERlesser game! Today you will try to guess a number from 1 to 100\n"
    "Please only attempt to send numbers otherwise the game will end\n"
    "Your first guess:")
n = 1
client.client_socket.send(clientInput.encode())
while True:
    serverOutput = client.client_socket.recv(512).decode()

    if serverOutput == 'won':
        print('Bingo, you got the right number, it took you ' + str(n) + ' guesses.')
        break
    elif serverOutput == 'lost':
        print('Please only use integers ranging from 1 to 100')
        break
    elif serverOutput == 'greater':
        print('Greater!')
    elif serverOutput == 'lesser':
        print('Lesser!')

    clientInput = input('Enter another guess: ')
    client.client_socket.send(clientInput.encode())
    n = n + 1
