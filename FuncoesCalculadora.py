def somar(numero, memoria):
    resultado = memoria + numero
    return resultado

def subtrair(numero, memoria):
    resultado = memoria - numero
    return resultado

def multiplicar(numero, memoria):
    resultado = memoria * numero
    return resultado

def dividir(numero, memoria):
    if numero == 0:
        print("Erro: Não é possível dividir por zero.")
        return memoria
    resultado = memoria / numero
    return resultado


def calculadora():
    memoria = 0  

    while True:
        
        print("\nEscolha uma opção:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        
        if escolha == "5":
            print("Calculadora encerrada.")
            break
        elif escolha in ["1", "2", "3", "4"]:
            
            numero = float(input("Digite um número: "))


            if escolha == "1":
                memoria = somar(numero, memoria)
                print(f"Resultado da soma: {memoria}")
            elif escolha == "2":
                memoria = subtrair(numero, memoria)
                print(f"Resultado da subtração: {memoria}")
            elif escolha == "3":
                memoria = multiplicar(numero, memoria)
                print(f"Resultado da multiplicação: {memoria}")
            elif escolha == "4":
                memoria = dividir(numero, memoria)
                print(f"Resultado da divisão: {memoria}")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


calculadora()
