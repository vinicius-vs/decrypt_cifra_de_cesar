# codigo criado para quebrar a cifra de césar por meio da força bruta

def ask_file():# função para pedir o arquivo para o usuario.
    directy = open(input("Digite o nome do arquivo. (exemplo: arquivo.txt): ") , "r") # o arquivo tem que estar na mesma pasta do .py
    text = directy.read()
    directy.close()
    return text

def analyze(message): #função para analisar se o testo esta descriptografado.
    dictionary = open("dicionariopt.txt", "r") # abre o dicionario que sera usado para verificação das palavras.
    dictionary_util = dictionary.readlines()
    message_util = message.split(" " or "." or "?") # separa o texto em palavras unicas
    for word in dictionary_util:
        if word == message_util[0]+'\n':
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

message = ask_file()
rotation = 1
while True:
    read = decrypt(message, rotation)
    if analyze(read) == True:
        break
    else:
        rotation = rotation + 1
print("\n",read,"\n")