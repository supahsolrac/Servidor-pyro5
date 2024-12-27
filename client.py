import obj
import Pyro5.client
import Pyro5.errors
import Pyro5.api
import sys

crud = Pyro5.client.Proxy("PYRONAME:carlosdreyer")
input("parada 2")
#crud = CRUD()
try:
    crud._pyroBind()
    input("parada 3")
except Pyro5.errors.CommunicationError:
    print("Objeto remoto não encontrado. Encerrando execução")
    sys.exit(1)

Pyro5.api.register_dict_to_class("obj.chara", obj.chara_dict_to_class)

opcao = 0

while True:

    print('Digite 1 para inserir, 2 para buscar, 3 para atualizar, 4 para excluir, 5 para sair')
    opcao = int(input("Opção desejada: "))
    match(opcao):
        case 1:
            nome = input("Digite nome do personagem: ")
            nivel = int(input("Digite nivel do personagem: "))
            exp = int(input("Digite exp do personagem: "))
            vida = int(input("Digite vida do personagem: "))
            vidamax = int(input("Digite vida maxima do personagem: "))
            resp = crud.inserir(nome,nivel,exp,vida,vidamax)
            if resp==1:
                print("inserido")
            else: 
                print("personagem ja existe")
        case 2:
            nome=input("Digite nome do personagem: ")
            char=crud.buscar(nome)
            try:
                char.print()
            except AttributeError:
                print("personagem não foi encontrado")
        case 3:
            nome=input("Digite nome do personagem: ")
            nivel = int(input("Digite o novo nivel do personagem: "))
            exp = int(input("Digite o novo exp do personagem: "))
            vida = int(input("Digite o novo vida do personagem: "))
            vidamax = int(input("Digite o novo vida maxima do personagem: "))
            resp=crud.atualizar(nome,nivel,exp,vida,vidamax)
            if resp==1:
                print("atualizado com sucesso")
            else:
                print("personagem não foi encontrado")
        case 4:
            nome=input("Digite nome do personagem: ")
            resp=crud.deletar(nome)
            if resp==1:
                print("deletado com sucesso")
            else:
                print("personagem não foi encontrado")
        case 5:
            break
        case _:
            print('Opção inválida')
    input("parada pos metodo")
