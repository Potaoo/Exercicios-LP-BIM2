def calcular_soma(arquivo):
    with open(arquivo, 'r') as f:
        numeros = [int(line.strip()) for line in f]
    return sum(numeros)

def multiplicar_elementos(arquivo):
    with open(arquivo, 'r') as f:
        numeros = [int(line.strip()) for line in f]
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def encontrar_maior_elemento(arquivo):
    with open(arquivo, 'r') as f:
        numeros = [int(line.strip()) for line in f]
    return max(numeros)

if __name__ == "__main__":
    arquivo_entrada = "arquivos/entrada.txt"

    # Calcular e imprimir a soma
    soma = calcular_soma(arquivo_entrada)
    print(f"SOMA = {soma}")

    # Calcular e imprimir o produto
    produto = multiplicar_elementos(arquivo_entrada)
    print(f"PRODUTO = {produto}")

    # Encontrar e imprimir o maior elemento
    maior_elemento = encontrar_maior_elemento(arquivo_entrada)
    print(f"MAIOR ELEMENTO = {maior_elemento}")
