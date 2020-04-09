## Criaçao de um simulador de dado de 0 a 6 numeros ##
import random

## Variaveis ##
def sorteiaNumero():
    numeroSorteado = random.randint(0, 6)
    print("O numero sorteado é ", numeroSorteado)
    pergunta()

def pergunta():
    respostaUsuario = str(input("Deseja realizar uma rolagem? Responda Sim ou Não: "))
    while respostaUsuario == 'sim':
        sorteiaNumero()
    else:
        pergunta()

pergunta()