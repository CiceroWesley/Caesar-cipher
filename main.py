

alfabet ='abcdefghijklmnopqrstuvwxyz'

def criptografar(text, k):
    ciferText = ''
    #para texto com mais de uma palavra
    if  " " in text:
        text = text.split(" ")
        for i in range(len(text)):
            ciferTextAux = ''
            for letter in text[i]:
                p = alfabet.index(letter)
                newIndex = (p + k) % 26
                ciferTextAux += alfabet[newIndex]
            ciferTextAux += " "
            ciferText +=ciferTextAux
    #para texto com uma palavra
    else:
        for letter in text:
            p = alfabet.index(letter)
            newIndex = (p + k) % 26
            ciferText += alfabet[newIndex]    
        
    return ciferText    

def descriptografar(text, k):
    ciferText = ''
    #para texto com mais de uma palavra
    if  " " in text:
        text = text.split(" ")
        for i in range(len(text)):
            ciferTextAux = ''
            for letter in text[i]:
                p = alfabet.index(letter)
                newIndex = (p - k) % 26
                ciferTextAux += alfabet[newIndex]
            ciferTextAux += " "
            ciferText +=ciferTextAux
    #para texto com uma palavra
    else:
        for letter in text:
            p = alfabet.index(letter)
            newIndex = (p - k) % 26
            ciferText += alfabet[newIndex]    
        
    return ciferText  

def main():
    option = int(input("1 - Criptografar texto com chave k\n2 - Descriptografar texto com chave k\n3 - Descriptografar texto com força bruta\n"))

    if option == 1:
        text = input("Insira o texto:")
        k = int(input("Insira o k:"))
        print(criptografar(text,k))
    elif option == 2:
        text1 = input("Insira o texto:")
        k = int(input("Insira o k:"))
        print(descriptografar(text1,k))
    elif option == 3:
        a = 1
    else:
        print("Opção inválida")


main()