def status_aluno(media):
    if media > 6:
        return "Aprovado"
    elif 4 <= media <= 6:
        return "Verificação suplementar"
    else:
        return "Reprovado"

# Exemplo de uso da função
media_aluno = float(input("Digite a média do aluno: "))
status = status_aluno(media_aluno)
print("Status do aluno:", status)
