def conversor_medidas():
    valor = None
    
    while True:
        try:
            valor = float(input('Digite o valor à ser convertido:'))
            break
        
        except ValueError:
            print('Você não digitou um numero para conversão!') 
    
    print('-----------------------------------------------')
    centimetros = valor*100
    milimetros = centimetros*10
    print(f'A conversão de {valor} em centímetros é: {centimetros}')
    print('-------------------------------------------------------')
    print(f'A conversão de {valor} para milímetros é: {milimetros}')


conversor_medidas()

