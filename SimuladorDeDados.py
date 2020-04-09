## Criaçao de um simulador de dado de 0 a 6 numeros ##
import random

## Variaveis ##
resposta = str(input("Deseja realizar uma rolagem? Responda Sim ou Não: "))
(resposta)

while resposta == 'sim':
    numeroSorteado = random.randint(0, 6)
    print("O numero sorteado é {}" + numeroSorteado)