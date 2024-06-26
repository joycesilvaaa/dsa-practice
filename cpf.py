#Valida Cpf

cpfs =[] #cpf digitados pelo usuario

def soma_produto(cpf, fim_contagem):
    soma = 0 
    for n in range (0,fim_contagem):
        digito = int(cpf[n])
        soma += digito * (n+2)
    return soma

def calcula_resto(soma):
    soma = soma % 11
    if soma == 0 or soma == 1:
        return '0'
    return str(11 - soma)

n= int(input())
c= 1
while c <= n:
    cpf = str(input())
    cpfs.append(cpf)
    c += 1

for cpf in cpfs:
    cpf_nove_digito = cpf[:-2][::-1]
    decimo_numero = calcula_resto(soma_produto(cpf_nove_digito, 9))

    cpf_dez_digito = cpf_nove_digito[::-1] + decimo_numero
    ultimo_numero = calcula_resto(soma_produto(cpf_dez_digito, 10))

    cpf_verificado = cpf_dez_digito + ultimo_numero

    if cpf == cpf_verificado:
        print('VALIDO')
    else:
        print('INVALIDO')