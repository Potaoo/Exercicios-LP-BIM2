#1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova
pessoas=[]
for i in range(10):
    nome=input(f'Digite o nome da {i+1}° pessoa: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    pessoas.append([nome,idade])
print(pessoas)

mais_nova = pessoas[0]

for pessoa in pessoas:
    if pessoa < mais_nova:
        mais_nova = pessoa
print(mais_nova)