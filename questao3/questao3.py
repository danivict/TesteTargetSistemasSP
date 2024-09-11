import json

# Função para calcular faturamento
def calcular_faturamento(filename):
    # Ler o arquivo JSON
    with open(filename, 'r') as file:
        dados = json.load(file)
    
    faturamento_diario = dados["faturamento"]

    # Calcula o menor e maior valor de faturamento (desconsiderando dias com faturamento 0)
    faturamento_valido = [x for x in faturamento_diario if x > 0]
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    # Calcula a média mensal de faturamento (desconsiderando dias com faturamento 0)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Conta quantos dias o faturamento foi superior à média mensal
    dias_acima_da_media = sum(1 for x in faturamento_valido if x > media_mensal)

    # Exibe os resultados
    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Chamar a função passando o nome do arquivo JSON
calcular_faturamento("questao3/faturamento_mensal.json")
