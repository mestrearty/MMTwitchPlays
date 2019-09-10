from assistente import Assistente
import time

global file
file = 'button.txt'

class Playmoves:
    assistente = Assistente() #chamando assistente

    #Biblioteca de comandos
    libup = ["up","cima","w"]
    libdown = ["down", "baixo", "s"]
    libleft = ["left", "esquerda", "a"]
    libright = ["right", "direita", "d"]
    liba = ["x", "ba", "action", "ação", "acao"]
    libb = ["z", "bb", "back", "voltar"]
    librt = ["rt", "righttrigger", "gatilhodireito", "gd"]
    liblt = ["lt", "lefttrigger", "gatilhoesquerdo", "ge"]
    libstart = ["start", "st"]
    libselect = ["select", "slt"]
    libsave = ["save", "salvar","sv"]
    librecover = ["recover", "recuperar"]
    libatk = ["atk", "ataque", "atacar","attack"]
    libbattle = ["correr","run","pokemon", "pkm", "switch", "trocar","item", "bag", "mochila"]
    libnotlearn = ["notl","naoaprender"]
    #Declaração dos controles controles
    Bup = 'up'
    Bdown = 'down'
    Bleft = 'left'
    Bright = 'right'
    Ba = 'A'
    Bb = 'B'
    Blt = ''
    Brt = ''
    Bselect = 'select'
    Bstart = 'start'
    PositionMenu = 1
    temp=""
    PM = 1

    #seleção do comando de entrada
    def action(self, msg):
        msg = msg.lower()
        print(msg)
        if msg in "=":
            msg=self.temp
        else:
            self.temp=msg

        try:
            if msg in self.libup:
                self.pressUp()
            elif msg in self.libdown:
                self.pressDown()
            elif msg in self.libleft:
                self.pressLeft()
            elif msg in self.libright:
                self.pressRight()
            elif msg in self.liba:
                self.pressA()
            elif msg in self.libb:
                self.pressB()
            elif msg in self.librt:
                self.pressRT()
            elif msg in self.liblt:
                self.pressLT()
            elif msg in self.libstart:
                self.pressStart()
            elif msg in self.libselect:
                self.pressSelect()
            elif msg in self.libsave:
                self.save()
            elif msg in self.librecover:
                self.recover()
            elif msg in self.libnotlearn:
                self.donotlearnatk()
            else:
                if(msg.__contains__('-')):
                    msgMenu = msg.split("-", 1)[0]
                    msgNum = msg.split("-", 1)[1]
                    print(msgMenu)
                    print(msgNum)
                    if int(msgNum) >= 25:
                        msgNum = 25
                    if msgMenu in self.libatk:
                        self.battle(msgMenu,msgNum)
                    elif msgMenu in self.libup:
                        self.walk(self.Bup, int(msgNum))
                    elif msgMenu in self.libdown:
                        self.walk(self.Bdown, int(msgNum))
                    elif msgMenu in self.libleft:
                        self.walk(self.Bleft, int(msgNum))
                    elif msgMenu in self.libright:
                        self.walk(self.Bright, int(msgNum))
                elif msg in self.libbattle:
                    self.battle(msg)



        except:
            print("Estive aqui com a msg: " + msg)
        # verifica se há alguma msg a enviar
        msgAssistente = self.assistente.verificar()
        if isinstance(msgAssistente, str):
            return msgAssistente
    def console(self, msg):
        global file
        with open(file, 'a+') as f:
            f.write(msg+"\n")
            f.close()

   # presse and release a button button -> button to be pressed, wtp->time to w8 to press,wtr -> time w8 to release button
    def prelease(self, button, wtp=0.1,wtr=0.1):
        time.sleep(wtp)
        self.console(button)
        time.sleep(wtr)

    def walk(self, side, times=1, boots=True):
        print(times)
        times = times+1
        for x in range(times):
            self.prelease(side, 0.07)

    def battle(self, atkAction,atkNum=0):

        print(atkAction)
        self.prelease(self.Bb, 1, 0.1)
        self.prelease(self.Bb, 0.1, 0.1)
        self.prelease(self.Bb, 0.1, 0.1)
        if atkAction in ("atk", "attack", "ataque"):
            # seleciona opção de batalha
            self.prelease(self.Bup)
            self.prelease(self.Bleft)
            self.prelease(self.Ba, 0.1, 0.1)

            # ataque 1
            if atkNum == "1":
                self.prelease(self.Bup, 1)
                self.prelease(self.Bleft, 0.5)
                self.prelease(self.Ba,0.5)

            # ataque 2
            elif atkNum == "2":
                self.prelease(self.Bup, 1)
                self.prelease(self.Bright, 0.5)
                self.prelease(self.Ba, 0.5)

            # ataque 3
            elif atkNum == "3":
                self.prelease(self.Bdown, 1)
                self.prelease(self.Bleft, 0.5)
                self.prelease(self.Ba, 0.5)

            # ataque 4
            elif atkNum == "4":
                self.prelease(self.Bdown, 1)
                self.prelease(self.Bright), 0.5
                self.prelease(self.Ba, 0.5)


        elif atkAction in ("run", "fugir"):
            self.prelease(self.Bright)
            self.prelease(self.Bdown)
            self.prelease(self.Ba)
            self.prelease(self.Ba,0.5)

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
        while (self.PM != 6):
            if (self.PM < 6):
                time.sleep(0.5)
                self.PM += 1
                self.prelease(self.Bdown)
            else:
                self.PM -= 1
                self.prelease(self.Bup)
        time.sleep(1)
        self.prelease(self.Ba)
        time.sleep(5)
        self.prelease(self.Ba)
        time.sleep(5)
        self.prelease(self.Ba)

        self.prelease(self.Ba)
        self.assistente.setTimeSave()

    def recover(self):
        self.prelease(self.Ba)
        time.sleep(4)
        self.prelease(self.Ba)
        time.sleep(4)
        self.prelease(self.Ba)
        time.sleep(4)
        self.prelease(self.Ba)
        time.sleep(12)
        self.prelease(self.Ba)
        time.sleep(7)
        self.prelease(self.Ba)

    def donotlearnatk(self):
        time.sleep(1)
        self.prelease(self.Bb)
        time.sleep(4)
        self.prelease(self.Bb)
        time.sleep(4)
        self.prelease(self.Bb)
        time.sleep(4)
        self.prelease(self.Ba)
        time.sleep(4)
        self.prelease(self.Bb)
        time.sleep(4)
        self.prelease(self.Bb)
        time.sleep(4)


    def pressA(self):
       self.prelease(self.Ba)

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


