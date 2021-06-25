from socket import *
from _enc import *
import sys
from colorama import Fore, Back, Style

host = "127.0.0.1"
port = 2580

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(Fore.LIGHTCYAN_EX + "Server Started Successfully..." + Style.RESET_ALL)
except error as e:
    print(Fore.RED + Back.LIGHTWHITE_EX + "Error creating socket: %s" % e + Style.RESET_ALL)
    sys.exit(1)

c, add = s.accept()
print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "Client: " + str(add) + Style.RESET_ALL)

try:
    while True:
        data = c.recv(1024)
        data = data.decode('ascii')
        data = decrypt(data)
        print(Fore.LIGHTMAGENTA_EX + "Client:", data)
        if not data:
            print(Fore.LIGHTCYAN_EX + "Disconnect TCP Packet Recieved")
            data = 'Good Bye'
        if data == 'Good Bye':
            c.close()
            print(Fore.LIGHTCYAN_EX + "Connection Closed Successfully.  ^ ^")
            exit(0)
        data = input(Fore.LIGHTYELLOW_EX + "You: " + Style.RESET_ALL)
        data = encrypt(data)
        c.send(data.encode('ascii'))
        print(Fore.LIGHTYELLOW_EX + "You(Encoded): " + str(data) + Style.RESET_ALL)
except KeyboardInterrupt:
    print(Fore.RED + Back.LIGHTWHITE_EX + "Keyboard Interrupt Pressed")
    s.close()
    print(Fore.Blue + "Connection Closed")
