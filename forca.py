import random

def inicializar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def abrir_aquivo(nome_arquivo):

    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    possibilidade_secreta = [linha.strip() for linha in arquivo.readlines()]
    arquivo.close()
    return possibilidade_secreta


def item_aleatorio(lista):
    quant = len(lista) - 1
    index_rad = random.randint(0, quant)

    return lista[index_rad]


def jogar():


    inicializar()

    possibilidade_secreta = abrir_aquivo("palavras.txt")

    palavra_secreta = item_aleatorio(possibilidade_secreta)



    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros= 0

    while(not enforcou and not acertou):
        chute = input("Qual letra:")
        chute = chute.strip()


        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        if(acertou):
            print("Parabens Voce ganhou o jogo.")
            print("quer jogar novamente?")
        if(enforcou):
            print("voce perdeu ")


    jogar_dnv = input("jogar dnv?(S ou N)")


    if(jogar_dnv == "s"):
        jogar()
    elif(jogar_dnv == "n"):
        print("saindo...")
    else:
        print("volta pra escola...")



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

