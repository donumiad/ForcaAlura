import random
import os


def mostra_dica(erros, palavra_secreta):
    if erros == 7:
        print("\nDica numero 1:", palavra_secreta[1])
    elif erros == 4:
        print("\nDica numero 2:", palavra_secreta[2])
    elif erros == 1:
        print("\nUltima dica:", palavra_secreta[3])


def jogar():
    print('********************************')
    print('***Bem vindo ao jogo da forca***')
    print('********************************')

    palavra_secreta = inicializa_palavra_secreta()

    letras_acertadas = ["_" for letras in palavra_secreta[0]]

    enforcou = False
    acertou = False
    erros = 7

    while not enforcou and not acertou:
        index = 0
        esta_contido = 0

        mostra_dica(erros, palavra_secreta)

        print(letras_acertadas)
        print(f"Ainda tem {erros} tentativas")
        chute = input("Chute uma letra: ")
        chute = chute.strip().upper()


        # *************************************************
        # TESTA SE A LETRA ESTÁ CONTIDA NA PALAVRA SECRETA

        if chute in letras_acertadas:
            print("LETRA JÁ SELECIONADA. TENTE OUTRA")
        else:
            for letra in palavra_secreta[0]:
                if chute == letra:
                    letras_acertadas[index] = chute  # ADICIONA A LETRA NA LISTA
                    esta_contido = 1
                index += 1

        if esta_contido == 0:
            desenha_forca(erros)
            erros -= 1
        else:
            esta_contido == 0
        # **************************************************

        # ENCERRA O JOGO SE ACABAR AS TENTATIVAS OU SE ACERTART A PALAVRA
        if erros < 1:
            enforcou = True
            enforcou1(palavra_secreta)
        elif "_" not in letras_acertadas:
            acertou = True
            ganhou()
        # **************************************************

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def enforcou1(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def inicializa_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # ABRI O ARQUIVO
    palavras = []         # ARMAZENA TODAS AS PALAVRAS E DICAS
    palavra_secreta = []  # ARMAZENA A PALAVRA A SER ACERTADA E AS 3 DICAS

    for linha in arquivo:  # ADICIONA O ARQUIVO EM UMA LISTA
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras), 4)  # ESCOLHE UM NUMERO ALEATÓRIO EM RELAÇÃO AO TAMANHODA PALAVRA

    for cont_dicas in range(numero, numero+4):
        palavra_secreta.append(palavras[cont_dicas].upper())

    return palavra_secreta





if __name__ == "__main__":
    jogar()
