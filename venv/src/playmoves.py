from bdb import Bdb
from pynput.keyboard import Key, Controller
import time

global file
file = 'button.txt'

class Playmoves:
    keyboard = Controller()

    # controles
    Bup = 'up'
    Bdown = 'down'
    Bleft = 'left'
    Bright = 'right'
    Ba = 'A'
    Bb = 'B'
    Blt = 'a'
    Brt = 's'
    Bselect = 'start'
    Bstart = 'select'
    PositionMenu = 1
    temp=""
    PM=1
    def action(self, msg):
        print(msg)
        if msg in "=":
            msg=self.temp
        else:
            self.temp=msg

        try:
            if msg in ("up", "cima", "w"):
                self.pressUp()
            elif msg in ("down", "baixo", "s"):
                self.pressDown()
            elif msg in ("left", "esquerda", "a"):
                self.pressDown()
            elif msg in ("right", "direita", "d"):
                self.pressRight()
            elif msg in ("x", "Ba", "action", "ação"):
                self.pressA()
            elif msg in ("z", "Bb", "back", "voltar"):
                self.pressB()
            elif msg in ("rt", "righttrigger", "gatilhodireito", "gd"):
                self.pressRT()
            elif msg in ("lt", "lefttrigger", "gatilhoesquerdo", "ge"):
                self.pressLT()
            elif msg in ("start", "st"):
                self.pressStart()
            elif msg in ("select", "slt"):
                self.pressSelect()
            elif msg in ("save", "salvar"):
                self.save()
            elif msg in ("recover", "recuperar"):
                self.recover()

            else:
                if(msg.__contains__('-')):
                    msgMenu = msg.split("-", 1)[0]
                    msgNum = msg.split("-", 1)[1]
                    if int(msgNum) >= 25:
                        msgNum = 25
                    if msgMenu in ("atk", "ataque", "atacar","attack"):
                        self.battle(msgMenu,msgNum)
                    elif msgMenu in ("up", "cima", "w"):
                        self.walk(self.Bup, int(msgNum))
                    elif msgMenu in ("down", "baixo", "s"):
                        self.walk(self.Bdown, int(msgNum))
                    elif msgMenu in ("left", "esquerda", "a"):
                        self.walk(self.Bleft, int(msgNum))
                    elif msgMenu in ("right", "direita", "d"):
                        self.walk(self.Bright, int(msgNum))
                elif msg in ("correr","run","pokemon", "pkm", "switch", "trocar","item", "bag", "mochila"):
                    self.battle(msg)
        except:
            print("Estive aqui com a msg: " + msg)
    # presse and release a button button -> button to be pressed, wtp->time to w8 to press,wtr -> time w8 to release button
    def prelease(self, button, wtr=0.1, wtp=0.1):
        time.sleep(wtp)
        time.sleep(wtr)
        global file
        with open(file, 'w') as f:
            f.write(button)

    def walk(self, side, times=1, boots=True):
        print(times)
        times = times+1
        # if (boots == True):
        #     self.keyboard.press(self.Bb)
        #     self.keyboard.press(side)
        for x in range(times):
            self.prelease(side)
            time.sleep(0.05)

        # self.keyboard.release(side)
        # self.keyboard.release(self.Bb)

    def battle(self, atkAction,atkNum=0):

        print(atkAction)
        self.prelease(self.Bb, 0.1, 1)
        self.prelease(self.Bb, 0.1, 0.1)
        self.prelease(self.Bb, 0.1, 0.5)
        if atkAction in ("atk", "attack", "ataque"):
            # seleciona opção de batalha
            self.prelease(self.Bup)
            self.prelease(self.Bleft)
            self.prelease(self.Ba, 0.1, 0.1)

            # ataque 1
            if atkNum == "1":
                self.prelease(self.Bup, 0.1)
                self.prelease(self.Bleft)
                self.prelease(self.Ba)

            # ataque 2
            elif atkNum == "2":
                self.prelease(self.Bup)
                self.prelease(self.Bright)
                self.prelease(self.Ba)

            # ataque 3
            elif atkNum == "3":
                self.prelease(self.Bdown)
                self.prelease(self.Bleft)
                self.prelease(self.Ba)

            # ataque 4
            elif atkNum == "4":
                self.prelease(self.Bdown)
                self.prelease(self.Bright)
                self.prelease(self.Ba)


        elif atkAction in ("run", "fugir"):
            self.prelease(self.Bright)
            self.prelease(self.Bdown)
            self.prelease(self.Ba)
            self.prelease(self.Ba,0.1,0.5)

        elif atkAction in ("item", "bag", "mochila"):
            self.prelease(self.Bright)
            self.prelease(self.Bup)
            self.prelease(self.Ba)

        elif atkAction in ("pokemon", "pkm", "switch", "trocar"):
            self.prelease(self.Bleft)
            self.prelease(self.Bdown)
            self.prelease(self.Ba)

    def save(self):
        self.prelease(self.Bstart)
        while (self.PM != 4):
            if (self.PM < 4):
                self.PM += 1
                self.prelease(self.Bup)

            else:
                self.PM -= 1
                self.prelease(self.Bdown)
        self.prelease(self.Ba)
        time.sleep(0.2)
        self.prelease(self.Ba)

        self.prelease(self.Ba)

    def recover(self):
        def pres(t1=0.1,t2=0.1):
            self.keyboard.press(self.Bb)
            self.prelease(self.Ba,t1,t2)
        pres(1)
        time.sleep(0.3)
        pres(1)
        pres(1)
        pres(1)
        time.sleep(5)
        pres(0.5)
        pres(0.5)

        self.prelease(self.Bb)

    def pressA(self):
       self.prelease((self.Ba))
       # self.prelease(self.Ba)

    def pressB(self):
        self.prelease(self.Bb)

    def pressRT(self):
        self.prelease(self.Brt)

    def pressLT(self):
        self.prelease(self.Blt)

    def pressStart(self):
        self.prelease(self.Bstart)

    def pressSelect(self):
        self.prelease(self.Bselect)

    def pressUp(self):
        self.prelease(self.Bup)

    def pressDown(self):
        self.prelease(self.Bdown)

    def pressLeft(self):
        self.prelease(self.Bleft)

    def pressRight(self):
        self.prelease(self.Bright)