import json

# Supondo que o JSON seja passado assim
dados_faturamento = '''
{
    "faturamento_diario": [1000, 2000, 0, 3000, 1500, 0, 4000, 2500, 500, 0]
}
'''

faturamento = json.loads(dados_faturamento)['faturamento_diario']

def calcular_faturamento(faturamento):
    faturamento_valido = [dia for dia in faturamento if dia > 0]  # Ignorar dias sem faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias = calcular_faturamento(faturamento)
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias}")
