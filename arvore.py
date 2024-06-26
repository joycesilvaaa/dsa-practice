def arvore(numero):
    letras = 'abcdefghijklmnopqrstuvxwyz' 
    letras_esquerda = letras[::-1] 
    i = 1 
    for n in range (0, numero):
        espaco = ' ' * (numero - n - 1) 
        if n > 0:
            linha =  espaco + letras_esquerda[-i:-1] + '*'+ letras[1:i] 
        else:
            linha = espaco + letras[n]
        print(linha)
        i = i + 1
        
numero= int(input())

arvore(numero)

        

