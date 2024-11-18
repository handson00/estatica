#Questão 2

import statistics
import math
import matplotlib.pyplot as plt


valores = [
    61, 65, 43, 53, 55, 51, 58, 55, 59, 56,
    52, 53, 62, 49, 68, 51, 50, 67, 62, 64,
    53, 56, 48, 50, 61, 44, 64, 53, 54, 55,
    48, 54, 57, 41, 54, 71, 55, 46, 57, 54,
    48, 63, 49, 55, 57, 53, 46, 48, 52, 51
]


H = 5  
min_val = min(valores)
max_val = max(valores)


classes = []
inicio = min_val
while inicio < max_val:
    fim = inicio + H - 1
    classes.append((inicio, fim))
    inicio = fim + 1


frequencias = [0] * len(classes)
for valor in valores:
    for i, (inicio, fim) in enumerate(classes):
        if inicio <= valor <= fim:
            frequencias[i] += 1
            break


pontos_medios = [(inicio + fim) / 2 for inicio, fim in classes]


dados_expandido = []
for i in range(len(classes)):
    dados_expandido.extend([pontos_medios[i]] * frequencias[i])


media = sum(dados_expandido) / len(dados_expandido)
soma_dos_quadrados = sum((x - media) ** 2 for x in dados_expandido)
desvio_padrao = math.sqrt(soma_dos_quadrados / len(dados_expandido))
mediana = statistics.median(dados_expandido)


contagem = {}
for dado in dados_expandido:
    contagem[dado] = contagem.get(dado, 0) + 1
max_frequencia = max(contagem.values())
moda = [k for k, v in contagem.items() if v == max_frequencia]
if len(moda) > 1:
    moda = "Não tem moda"
else:
    moda = moda[0]


dados_ordenados = sorted(dados_expandido)

def calcular_percentil(dados, percentil):
    posicao = (percentil / 100) * (len(dados) - 1)
    abaixo = int(posicao)
    acima = abaixo + 1
    if acima < len(dados):
        return dados[abaixo] + (dados[acima] - dados[abaixo]) * (posicao - abaixo)
    else:
        return dados[abaixo]

q1 = calcular_percentil(dados_ordenados, 25)
d3 = calcular_percentil(dados_ordenados, 30)
d7 = calcular_percentil(dados_ordenados, 70)
p15 = calcular_percentil(dados_ordenados, 15)
p90 = calcular_percentil(dados_ordenados, 90)


print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Quartil 1 (Q1): {q1:.2f}")
print(f"Decil 3 (D3): {d3:.2f}")
print(f"Decil 7 (D7): {d7:.2f}")
print(f"Percentil 15 (P15): {p15:.2f}")
print(f"Percentil 90 (P90): {p90:.2f}")


plt.bar([f'{inicio}-{fim}' for inicio, fim in classes], frequencias, color='lightblue')
plt.title("Distribuição de Frequências - Tempo de Preenchimento")
plt.xlabel("Intervalos de Tempo (s)")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
