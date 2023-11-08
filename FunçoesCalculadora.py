def somar(memoria, numero):
    return memoria + numero

def subtrair(memoria, numero):
    return memoria - numero

def multiplicar(memoria, numero):
    return memoria * numero

def dividir(memoria, numero):
    if numero != 0:
        return memoria / numero
    else:
        print("Erro: Divisão por zero")
        return memoria

def limpar_memoria():
    return 0

def calculadora():
    memoria = 0

    while True:
        print("Estado da memória:", memoria)
        print("Opções:")
        print("(1) Somar")
        print("(2) Subtrair")
        print("(3) Multiplicar")
        print("(4) Dividir")
        print("(5) Limpar memória")
        print("(6) Sair do programa")

        opcao = input("Qual opção você deseja? ")

        if opcao == '1':
            numero = float(input("Digite o número a ser somado: "))
            memoria = somar(memoria, numero)
        elif opcao == '2':
            numero = float(input("Digite o número a ser subtraído: "))
            memoria = subtrair(memoria, numero)
        elif opcao == '3':
            numero = float(input("Digite o número a ser multiplicado: "))
            memoria = multiplicar(memoria, numero)
        elif opcao == '4':
            numero = float(input("Digite o número pelo qual dividir: "))
            memoria = dividir(memoria, numero)
        elif opcao == '5':
            memoria = limpar_memoria()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
