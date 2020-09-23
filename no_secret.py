# codigo criado para quebrar a cifra de césar por meio da força bruta

def ask_file():# função para pedir o arquivo para o usuario.
    directy = open(input("Digite o nome do arquivo. (exemplo: arquivo.txt): ") , "r") # o arquivo tem que estar na mesma pasta do .py
    text = directy.read()
    directy.close()
    return text

def analyze(message): #função para analisar se o testo esta descriptografado.
    dictionary = open("dicionarioptcompleto.txt",
                      "r")  # abre o dicionario que sera usado para verificação das palavras.
    dictionary_util = dictionary.readlines()
    message_util = message.split(" " or "." or "?")  # separa o texto em palavras unicas

    cont = 0

    for i in range(len(message_util)):
        for word in dictionary_util:
            if word == message_util[i] + '\n':
                cont = cont + 1



    percentagem = cont*100/len(message_util)

    if percentagem >= 30.0:
        return True
    dictionary.close()


def decrypt(text, rotation ): #função que realiza a troca de letras.
    aplhabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text_decr = ""
    for letter in text: # laço para percorrer  as letras do texto
        if letter == " ":
            text_decr += " "
        elif letter == "\n":
            text_decr +="\n"
        elif letter == "?":
            text_decr += "?"
        elif letter == ".":
            text_decr += "."
        elif letter == ",":
            text_decr += ","
        elif letter == "-":
            text_decr +="-"
        else:
            index = aplhabet.index(letter)
            new_letter = aplhabet[index - rotation]
            text_decr += new_letter

    return text_decr
while True:
    esco = input("Escolha uma opção. D - Decrypt, E - Encripyt: ")
    if esco == D or esco == E:
         break
    else:
        print("escolha invalida, tente novamente.\n")

if esco == "E":
    from random import *
    rotation = randrange(1 , 25)
    message = ask_file()
    encrypt = cifra_cesar(message,rotation)
    print(encrypt,"\n")
    print(rotation)
elif esco =="D":
    message = ask_file()
    rotation = 1
    counter = 0
    while True:

        if counter == 25:
            print("Não foi possível quebrar")

        else:
            read = cifra_cesar(message, rotation)
            if analyze(read) == True:
                print("\n", read, "\n")
                break
            else:
                rotation = rotation + 1
