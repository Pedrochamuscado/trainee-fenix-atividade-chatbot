class Armazem:
    
    def __init__(self):
        self.produtos = {'chinelo':[30, 20.5], 'short':[20, 35.75], 'bone':[12, 15], 'camisa':[60, 8]}
    
    def checar_preco(self, produto):
        return self.produtos[produto][1]
    #verificado
    
    def ver_ofertas(self):
        for i in self.produtos:
            preco = f'{round(self.produtos[i][1]):.2f}'
            print(f'-- {i.title()} por R${preco.replace(".",",")}   Estoque  {int(self.produtos[i][0])}')
        print('\nPressione qualquer botão para retornar ao menu.')
    #verificado

class Carrinho(Armazem):
    def __init__(self):
        self.carrinho = {}
    
    def adicionar_produto(self, nome, quantidade, preco):
        saldo = quantidade*preco
        if nome in self.carrinho:
            self.carrinho[nome][1] += quantidade
            self.carrinho[nome][2] += saldo
        else:
            self.carrinho[nome] = [preco, quantidade, saldo]
    
    def remover_produto(self, nome, quantidade, preco):
        saldo = quantidade*preco
        if nome in self.carrinho and self.carrinho[nome][1] > quantidade:
            self.carrinho[nome][1] -= quantidade
            self.carrinho[nome][2] -= saldo

        if nome in self.carrinho and self.carrinho[nome][1] == quantidade:
            del self.carrinho[nome]
    
    def fechar_carrinho(self, produtos):
        for i in self.carrinho:
            produtos[i][0] -= self.carrinho[i][1]

        saldo_total = 0
        for i in self.carrinho:
            saldo_total += self.carrinho[i][2]
        total_gasto = f'{round(saldo_total):.2f}'
        print(f'A sua compra deu um total de R${total_gasto.replace(".",",")}.\nObrigado pela preferência :)')
        self.carrinho = {}