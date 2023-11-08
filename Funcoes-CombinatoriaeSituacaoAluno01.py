def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def calcular_combinacoes(N, M):
    if N < M:
        return 0
    else:
        return calcular_fatorial(N) // (calcular_fatorial(M) * calcular_fatorial(N - M))

def main():
    N = int(input("Digite o número total de alunos (N): "))
    M = int(input("Digite o número de alunos em um dos grupos (M): "))

    if N >= M >= 0:
        numero_combinacoes = calcular_combinacoes(N, M)
        print(f"O número de combinações possíveis é: {numero_combinacoes}")
    else:
        print("Entrada inválida. Certifique-se de que 0 <= M <= N.")

if __name__ == "__main__":
    main()
