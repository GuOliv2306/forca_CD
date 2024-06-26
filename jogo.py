"""modulo com funcionamento do jogo"""

from boneco import enforcado
import arte_GameOver

def table(tamanho_palavra_escolhida, acertos):
    print("========================================")
    for i in range(tamanho_palavra_escolhida):
        if acertos[i] == 0:
            print("_", end=" ")
        else:
            print(acertos[i], end=' ')
    print()
    """FUNÇÃO BONECO"""


def teste_letra_escolhida(letra, letras_escolhidas):
    if letra not in letras_escolhidas:
        letras_escolhidas.add(letra)
    else:
        print(letra)
        while letra in letras_escolhidas:
            letra = input("Entre com uma outra letra que você ainda não escolheu: ")
        teste_letra_escolhida(letra, letras_escolhidas)
    return letra


def acerto(letra, palavra_escolhida, acertos):
    if 0 not in acertos:
        print("Você venceu!!!")
        return "cabo"
    if letra in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if letra == palavra_escolhida[i]:
                acertos[i] = letra
        return True
    else:
        return False


def game(palavra_escolhida):
    acertos = [0] * len(palavra_escolhida)
    tentativas = 6
    letras_escolhidas = set()
    while tentativas >= 1:
        enforcado(tentativas)
        tamanho_palavra_escolhida = len(palavra_escolhida)
        table(tamanho_palavra_escolhida, acertos)

        letra_nao_oficial = input("Entre com uma letra: ")
        letra = teste_letra_escolhida(letra_nao_oficial, letras_escolhidas)
        print(letras_escolhidas)

        if acerto(letra, palavra_escolhida, acertos) == False:
            tentativas-=1
            print("ERROU!!!")
            if (tentativas == 0):
                print("VOCÊ PERDEU")
                print(f'a palavra era {palavra_escolhida}')
                arte_GameOver.gameover()
                break
            acerto(letra, palavra_escolhida, acertos)

        elif (acerto(letra, palavra_escolhida, acertos) == True):
            acerto(letra, palavra_escolhida, acertos)
        elif (tentativas == 0):
            print("VOCÊ PERDEU")
            print(f'a palavra era {palavra_escolhida}')
            arte_GameOver.gameover()
        else:
            tentativas = 0