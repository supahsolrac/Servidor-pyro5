class chara:

    def __init__(self,nome,nivel,exp,vida,vidamax):
        self.nome=nome
        self.nivel=nivel
        self.exp=exp
        self.vida=vida
        self.vidamax=vidamax

    def print(self):
        print("nivel: ", self.nivel, " exp:", self.exp)
        print("vida: ", self.vida,"/",self.vidamax)

def chara_class_to_dict(obj):
    charadict = {
        "__class__":"obj.chara",
        "nome":obj.nome,
        "nivel":obj.nivel,
        "exp":obj.exp,
        "vida":obj.vida,
        "vidamax":obj.vidamax,
    }
    return charadict

def chara_dict_to_class(classname, dic):
    c = chara(dic["nome"],dic["nivel"],dic["exp"],dic["vida"],dic["vidamax"])
    return c

