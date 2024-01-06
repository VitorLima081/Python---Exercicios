class Funcoes:
    @staticmethod
    def aumentar(n):
        conta_aumentar_dez = (n * 10) / 100
        soma_aumentar = conta_aumentar_dez + n
        
        return soma_aumentar

    @staticmethod
    def diminuir(n):
        conta_diminuir_dez = (n * 10) / 100
        subtrair = n - conta_diminuir_dez
        
        return subtrair
    
    @staticmethod
    def dobrar(n):
        conta_dobrar = n * 2
        return conta_dobrar
    
    @staticmethod
    def metade(n):
        conta_metade = n / 2
        return conta_metade

    @staticmethod
    def formatando_valor(n):
        valor_formatado = "R${:,.2f}".format(n)
        return valor_formatado    
