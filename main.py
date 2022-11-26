'''
Gostaria de comentar que, nessa atividade, chegar no objetivo principal de ter um código de uma suposta loja online funcional não tardou muito de se alcançar. Entretanto, o mais difícil e trabalhoso foi o processo de aprendizagem, tentativa e erro para eu conseguir aperfeiçoar meu código para ser o mais blindado a bugs e errors que eu consigo.
Portanto, incentivo o senhor ou a senhora a tentar quebrar meu código para o testar. Por favor, me dê um feedback a respeito :)
'''

import unicodedata
import re
from classes import *

a = Armazem()
c = Carrinho()
loop = True

while loop:
    print('=============================================\nBem vindo ao chatbox de atendimento.\nOs seguintes comandos estão disponíveis:\n1 - Adicionar item\n2 - Remover item\n3 - Mostrar carrinho de compras\n4 - Fechar carrinho de compras\n5 - Olhar as ofertas\n=============================================')
    sair = False
    while True:
        try:
            resposta = int(input())
            if int(resposta) not in (1,2,3,4,5):
                print('Resposta inválida, digite um número correspondente a uma das opções(1,2,3,4,5).')
            else:
                resposta = int(resposta)
                break
        except:
            print('Ops, resposta inválida, digite um número correspondente a uma das opções(1,2,3,4,5).')


    if resposta == 1:
        while sair == False:
            print('==============================================\nDiga a quantidade e o item que deseja por favor:')
            while True:
                x = (unicodedata.normalize('NFD', input())).encode('ascii', 'ignore').decode('utf8').casefold()
                
                numero = [float(s) for s in re.findall(r'-?\d+\.?\d*', x)]#A variável 'num' recebe uma lista com os dígitos numéricos da quantidade que ele definiu
                try:
                    num = numero[0]

                    nome = str(re.sub(r'[0-9]+', '', x)).replace(" ", "") #A variável 'nome' recebe o nome do produto que ele definiu em sua resposta, o replace evita um bug específico.

                    if (nome in c.carrinho and num + c.carrinho[nome][1] > a. produtos[nome][0]) or num > a.produtos[nome][0] or nome not in a.produtos:
                        print('Com essa quantidade, ficará com mais no carrinho do que temos do produto disponível, ou o produto selecionado não está disponível na nossa loja, por favor, digite um produto e uma quantidade válida que deseja.')
                    else:
                        break
                except:
                    print('Ops, resposta inválida.')  

            preco = a.checar_preco(nome)

            c.adicionar_produto(nome, num, preco)
            print('O produto foi adicionado, deseja pôr mais algum ?(S/N)')

            while True:
                try:
                    x = input()
                    if str(x.upper()).replace(" ", "") == 'S' and len(x) < 4:
                        break
                    if str(x.upper()).replace(" ", "") == 'N' and len(x) < 4:
                        sair = True
                        break
                    print('Resposta inválida, digite S/N:')
                except:
                    print('Erro, reposta inválida. Por favor, responda S/N.')
    
    if resposta == 2:

        while sair == False:
            print('==============================================\nDiga a quantidade e o item que deseja remover por favor:')
            while True:
                x = (unicodedata.normalize('NFD', input())).encode('ascii', 'ignore').decode('utf8').casefold()

                numero = [float(s) for s in re.findall(r'-?\d+\.?\d*', x)]

                try:
                    num = numero[0]

                    nome = str(re.sub(r'[0-9]+', '', x)).replace(" ", "") #O objeto 'nome' recebe o nome do produto que ele definiu em sua resposta, o replace evita um bug específico.

                    preco = a.checar_preco(nome)
                    
                    if c.carrinho[nome][1] < num or nome not in c.carrinho:
                        print('Erro, você tentou remover mais do item do que há no carrinho, ou digitou um item que não está presente no carrinho.')
                    else:
                        break
                except:
                    print('Opa, resposta inválida, tente novamente')

            c.remover_produto(nome, num, preco)
            print('O produto foi removido, deseja remover mais algum ?(S/N)')
            
            while True:
                try:
                    x = str(input().upper()).replace(" ", "")
                    if x[0] == 'S' and len(x) < 4:
                        break
                    if x[0] == 'N' and len(x) < 4:
                        sair = True
                        break
                    print('Resposta inválida, digite S/N:')
                except:
                    print('Ops, resposta inválida, por favor, decida por S/N.')

    if resposta == 3:
        print('==============================================')
        for i in c.carrinho:
            print(f'{i}         Preço:R${c.carrinho[i][0]} Quantidade:{c.carrinho[i][1]} Saldo:R${c.carrinho[i][2]}')
        print('Insira qualquer coisa para retornar ao menu:')
        input()

    if resposta == 4:
        print('==============================================')
        c.fechar_carrinho(a.produtos)
        print('Digite qualquer coisa para retornar ao menu.')
        input()

    if resposta == 5:
        a.ver_ofertas()
        input()
