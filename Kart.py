def melhor_volta(matriz_tempos):
    melhor_volta_tempo = float('inf')
    melhor_volta_corredor = 0
    for corredor in range(len(matriz_tempos)):
        for volta in range(len(matriz_tempos[corredor])):
            if matriz_tempos[corredor][volta] < melhor_volta_tempo:
                melhor_volta_tempo = matriz_tempos[corredor][volta]
                melhor_volta_corredor = corredor + 1  # Adiciona 1 porque a corrida começa do corredor 1, não 0
                melhor_volta_numero = volta + 1  # Adiciona 1 porque as voltas começam do número 1, não 0

    return melhor_volta_corredor, melhor_volta_numero

def classificacao_final(matriz_tempos):
    tempos_finais = [sum(corredor) for corredor in matriz_tempos]
    classificacao = sorted(enumerate(tempos_finais, start=1), key=lambda x: x[1])
    return classificacao

def volta_com_media_mais_rapida(matriz_tempos):
    medias_por_volta = [sum(matriz_tempos[corredor][volta] for corredor in range(len(matriz_tempos))) / len(matriz_tempos) for volta in range(len(matriz_tempos[0]))]
    volta_mais_rapida = medias_por_volta.index(min(medias_por_volta)) + 1  # Adiciona 1 porque as voltas começam do número 1, não 0
    return volta_mais_rapida

if __name__ == "__main__":
    # Leitura dos tempos e nomes dos corredores
    matriz_tempos = []
    nomes_corredores = []
    for corredor in range(6):
        nome = input(f"Digite o nome do corredor {corredor + 1}: ")
        nomes_corredores.append(nome)
        tempos = [float(input(f"Digite o tempo da volta {volta + 1} em segundos: ")) for volta in range(10)]
        matriz_tempos.append(tempos)

    # a) Melhor volta
    melhor_corredor, melhor_volta = melhor_volta(matriz_tempos)
    print(f"A melhor volta da prova foi do corredor {nomes_corredores[melhor_corredor - 1]} na volta {melhor_volta}.")

    # b) Classificação final
    classificacao = classificacao_final(matriz_tempos)
    print("\nClassificação Final:")
    for posicao, (corredor, tempo) in enumerate(classificacao, start=1):
        print(f"{posicao}º lugar: {nomes_corredores[corredor - 1]} - Tempo total: {tempo} segundos")

    # c) Volta com média mais rápida
    volta_mais_rapida = volta_com_media_mais_rapida(matriz_tempos)
    print(f"\nA volta com a média mais rápida foi a volta {volta_mais_rapida}.")
