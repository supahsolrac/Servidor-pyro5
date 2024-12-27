import obj
import Pyro5
import Pyro5.core
import Pyro5.server


@Pyro5.server.expose
class Personagens(object):

    def __init__(self):
        self.pers=[]

    def inserir(self,nome,nivel,exp,vida,vidamax):
        persona=obj.chara(nome,nivel,exp,vida,vidamax)
        for i in range(len(self.pers)):
            if (self.pers[i].nome==nome):
                return 0
        self.pers.append(persona)
        return 1

    def buscar(self,nome):
        for i in range(len(self.pers)):
            if (self.pers[i].nome==nome):
                return self.pers[i]
        return None

    def atualizar(self,nome,nivel,exp,vida,vidamax):
        for i in range(len(self.pers)):
            if (self.pers[i].nome==nome):
                self.pers[i].nivel=nivel
                self.pers[i].exp=exp
                self.pers[i].vida=vida
                self.pers[i].vidamax=vidamax
                return 1
        return 0

    def deletar(self,nome):
        for i in range(len(self.pers)):
            if (self.pers[i].nome==nome):
                self.pers.pop(i)
                return 1
        return 0
        


