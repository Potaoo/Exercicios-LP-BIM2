#2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
#número k. Imprima a matriz na tela antes e depois da multiplicação.
Matriz = []
N=3
M=3
for i in range(N):
    linha=[]
    for j in range(M):
        valor = int(input(f'Digite o valor para[linha {i+1}][coluna {j+1}]: '))
        linha.append(valor)
    Matriz.append(linha)
print(Matriz)    

print("Matriz original:")
for linha in Matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

k = int(input("\nDigite o valor de k para multiplicar a diagonal: "))

# Multiplicando a diagonal principal por k
for i in range(len(Matriz)):
    for j in range(len(Matriz[i])):
        if i == j:
            Matriz[i][j] *= k

print("\nMatriz após multiplicar a diagonal por k:")
for linha in Matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()