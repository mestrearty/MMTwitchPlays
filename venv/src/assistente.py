import datetime
class Assistente:
    timeEnterSave = datetime.datetime.now()
    timeExit = datetime.datetime.now()
    timeEnterRecover = datetime.datetime.now()
    timeEnterAgua = datetime.datetime.now()
    timeEnterChat = datetime.datetime.now()

    t = 0
    tagua = 0
    tchat = 0

    def __init__(self):
        self.timeEnterSave = datetime.datetime.now()
        self.timeExit = datetime.datetime.now()
        self.timeEnterRecover = datetime.datetime.now()

    def setTimeExit(self):
        self.timeExit = datetime.datetime.now()

    def setTimeSave(self):
        self.timeEnterSave = datetime.datetime.now()

    def setTimeRecover(self):
        self.timeEnterRecover = datetime.datetime.now()

    def setTimeAgua(self):
        self.timeEnterAgua = datetime.datetime.now()

    def setTimeChat(self):
        self.timeEnterChat = datetime.datetime.now()

    def timeSaveCompare(self):
        diferenca = self.timeExit.minute - self.timeEnterSave.minute
        if diferenca > self.t or diferenca < -55:
            self.setTimeSave()
            return "Ei, tem muito tempo que você não salva, que tal você salvar o jogo?"

    def timeRecovercomapre(self):
        diferenca = self.timeExit.minute - self.timeEnterRecover.minute
        if diferenca > self.t or diferenca < -55:
            self.setTimeRecover()
            return "Opa, tem muito tempo que você não vai ao Centro Pokemon! Não acha que deveria curar seus pokemons?"

    def timeBeberAguacomapre(self):
        diferenca = self.timeExit.minute - self.timeEnterAgua.minute
        if diferenca > self.tagua or diferenca < -55:
            self.setTimeAgua
            self.setTimeAgua()
            return "E ai jovem, que tal uma pausa pra beber uma água e ficar hidratado?"

    def timeRegrasChatcompare(self):
        diferenca = self.timeExit.minute - self.timeEnterChat.minute
        if diferenca > self.tchat or diferenca < -55:
            self.setTimeChat()
            return "Ficou com dúvidas de como jogar? Vai na nossa descrição. Lá tem todas as regras!"

    def verificar(self):
        self.setTimeExit()

        msg = self.timeSaveCompare()
        if isinstance(msg, str):
            return msg

        msg = self.timeRecovercomapre()
        if msg:
            return msg

        msg = self.timeBeberAguacomapre()
        if msg:
            return msg

        msg = self.timeRegrasChatcompare()
        if msg:
            return msg
