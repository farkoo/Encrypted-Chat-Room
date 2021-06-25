from socket import *
from _enc import *
import sys
from colorama import Fore, Back, Style

host = "127.0.0.1"
port = 2580

try:
    s = socket(AF_INET, SOCK_STREAM)
except error as e:
    print(Fore.RED + Back.LIGHTWHITE_EX + "Error creating socket: %s" % e + Style.RESET_ALL)
    sys.exit(1)

try:
    s.connect((host, port))
except gaierror as e:
    print(Fore.RED + Back.LIGHTWHITE_EX + "Address-related error connecting to server: %s" % e + Style.RESET_ALL)
    sys.exit(1)
except socket.error as e:
    print(Fore.RED + Back.LIGHTWHITE_EX + "Connection error: %s" % e + Style.RESET_ALL)
    sys.exit(1)

msg = input(Fore.LIGHTMAGENTA_EX + "You: " + Style.RESET_ALL)
while msg != "Good Bye":
    msg = encrypt(msg)
    print(Fore.LIGHTMAGENTA_EX + "You(Encoded): " + str(msg) + Style.RESET_ALL)
    try:
        s.send(msg.encode('ascii'))
    except error as e:
        print(Fore.RED + Back.LIGHTWHITE_EX + "Error sending data: %s" % e + Style.RESET_ALL)
        sys.exit(1)
    try:
        data = s.recv(2048)
    except error as e:
        print(Fore.RED + Back.LIGHTWHITE_EX + "Error receiving data: %s" % e + Style.RESET_ALL)
        sys.exit(1)
    data = data.decode('ascii')
    data = decrypt(data)
    print(Fore.LIGHTYELLOW_EX + "server: " + str(data) + Style.RESET_ALL)

    if not len(data) or data == "Good Bye":
        print(Fore.LIGHTCYAN_EX + "Connection Closed Successfully. ^ ^" + Style.RESET_ALL)
        s.close()
        exit(0)

    msg = input(Fore.LIGHTMAGENTA_EX + "You: " + Style.RESET_ALL)

print(Fore.LIGHTCYAN_EX + "Connection Closed Successfully. ^ ^" + Style.RESET_ALL)
s.close()
exit(0)
