#bot.py
from cfg import *
import socket
import time
import re
CHAT_MSG = re.compile(r"^:\w+!\w@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ ")

"""bot functions"""


def chat(sock, msg):
    """
    Send a chat message to the server.
    """
    sock.send("PRIVMSG #{} :{}".format(CHAN, msg))


def main_loop():
    while connected:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            print(str("Pong"))
        else:
            username = re.search(r"\w+", response).group(0)  # returns entire match
            message = response.split(':')
            # print(response)
            print(username + ": " + message[2])
            for pattern in PATT:
                if re.match(pattern, message[2]):
                    print(str("match"))
                    break
        time.sleep(1/RATE)  # limits how many messages per second we can send

try:
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
    connected = True
except Exception as e:
    print(str(e))
    connected = False

main_loop()





