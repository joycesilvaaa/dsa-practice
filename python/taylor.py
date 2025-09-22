def rad(x):
    pi = 3.1415 
    return x * (pi/180) 
    
def taylor(x):
    r = rad(x)
    a = 1 
    b = 1
    soma = 0
    n= 0
    while n <= 5:
        soma += a / b
        a = a * (-r**2)
        b = b * (2*n + 1) * (2*n + 2)
        n += 1
    return print(arrendondamento(soma))

def arrendondamento(numero):
    numero_string = f'{numero:.4f}'
    inteiro = numero_string.split('.')[0]
    decimal = numero_string.split('.')[1]
    if len(decimal) > 2:
        verifica = int(decimal[3])
        if verifica > 6:
            arredonda = round(float(f'{inteiro}.{decimal[:3]}') + 0.001, 3)
            return f'{arredonda:.3f}'
        return f'{inteiro}.{decimal[:3]}'
    return f'{numero:.3f}'
    
x = float(input()) 
taylor(x)