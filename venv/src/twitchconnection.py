from playmoves import Playmoves
import socket
import sys
import re

class TwichConnection:
    SERVER = "irc.twitch.tv"
    PORT = 6667
    PASS = "oauth:w6ftvibub59cggtrie3jaou6pd7up9"
    BOT = "artficer"
    CHANNEL = "artficer"
    OWNER = "artficer"
    irc = socket.socket()
    irc.connect((SERVER, PORT))
    irc.send(("PASS " + PASS + "\n" +
              "NICK " + BOT + "\n" +
              "JOIN #" + CHANNEL + "\n").encode())

    playmoves = Playmoves()

    def __init__(self):
        self.joinchat()
        self.sendMessage("Bot Connectado - Twitch Play ativo")

        # obter dados do chat
        while True:
           #    eduardo rocha soares self.sendMessage("recover")
            try:
                readbuffer = self.irc.recv(1024).decode()
            except:
                readbuffer = ""

            for line in readbuffer.split("\r\n"):
                ping=line
                if line == "":
                    continue
                elif ping.split(":")[1] in "tmi.twitch.tv": #verifica se a twitch quer fechar conexção PING :tmi.twitch.tv "PONG " in ping.split(":")[0] and
                    msgg = "PONG :tmi.twitch.tv".encode()
                    self.irc.send(msgg)
                    print("Mantendo conexção")
                    continue
                else:
                    user = self.getUser(line)
                    message = self.getMessage(line)
                    print(user + " - " + message)

                    if (message.__contains__("palmito")):
                        self.sendMessage("Um salve pra galera do pokemon TCGJF!! Bjks Zé " + user)
                    elif (message.__contains__("nikolasrenanpedro")):
                        self.sendMessage(
                            "As maiores lendas que já passaram pelo if!! Nikolas o Sábio, Renan o esforçado, Pedro o... deixa pra la que deu preguiça")
                    self.playmoves.action(message)

    def joinchat(self):
        Loading = True
        while Loading:
            readbuffer_join = self.irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                Loading = self.loadingComplete(line)

    def loadingComplete(self, line):
        if ("End of /NAMES list" in line):
            print("Bot has joined " + self.CHANNEL + "'s Channel")
            print("Conectado")
            return False
        else:
            return True

    def sendMessage(self, message):
        messageTemp = "PRIVMSG #" + self.CHANNEL + " :" + message
        self.irc.send((messageTemp + "\n").encode())
        print(message)

    def getUser(self, line):
        separete = line.split(":", 2)
        user = separete[1].split("!", 1)[0]
        return user

    def getMessage(self, line):
        try:
            message = (line.split(":", 2)[2])
        except:
            message = ""
        return message
