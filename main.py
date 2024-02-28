import sys
import time

produtos = [('Chevette', '1998', 'Azul'), ('Fusca', '1980', 'Vermelho'), ('Ferrari', '1988', 'Preto')]

def cadastrar(): #Cadastrar 
  print("-"*50)
  q = int(input('Quantos carros deseja cadastrar? '))
  for i in range(q):
    modelo = input('Modelo do carro: ')
    ano = input('Ano do carro: ')
    cor = input('Cor do carro: ')
    carro = (modelo, ano, cor)
    produtos.append(carro)
    print(f'Carro: {carro} cadastrado')
    print("-"*50)
def menu():
  print('Bem vindo ao seu programa de gerenciamento')
  print("-"*50)
  print('MENU')
  print("""
  1 - Cadastrar produto
  2 - Mostrar produtos
  3 - Pesquisar produtos
  4 - Alterar produtos
  5 - Remover produtos
  6 - Sair""")
  print("-"*50)
def mostrar():
  print('-' *50)
  for produto in produtos:
    print(produto)
  print('-' *50)
def pesquisar():
  carro_pesq = input('Digite o nome, ano ou cor do carro que você gostaria de pesquisar: ')
  for produto in produtos:
    if carro_pesq in produto:
      print(produto)
def alterar():
  n= 0
  for produto in produtos:
    print(n,"-",produto)
    n += 1 
  p_escolhido = int(input('Qual produto você gostaria de alterar? '))
  modelo = input('Modelo do carro: ')
  ano = input('Ano do carro: ')
  cor = input('Cor do carro: ')
  carro = (modelo, ano, cor)
  produtos[p_escolhido] = carro
  print(f'Carro: {carro} alterado')
  print("-"*50)
def remover():
  n= 0
  for produto in produtos:
    print(n,"-",produto)
    n +=1
  p_escolhido = int(input('Qual produto você gostaria de remover? '))
  del produtos[p_escolhido]
  print(f'Produto: {produtos[p_escolhido]} removido')
  print("-"*50)
def main():
  while True: 
    menu()
    opcao = int(input('Escolha uma opção: '))
    print('-' * 50)

    if opcao == 1:
      cadastrar()
    elif opcao == 2:
      mostrar()
    elif opcao == 3:
      pesquisar()
    elif opcao == 4:
      alterar()
    elif opcao == 5:
      remover()
    elif opcao == 6: 
      print('Encerrando Processo...')
      print('Processo finalizado')
      print('_'*50)
      sys.exit()
    else:
      print('Opção Inválida!')
      time.sleep(3)

if __name__ == "__main__":
  main()
      
#Mostrar, Pesquisar, Alterar, e Remover, além de opções de Relatórios