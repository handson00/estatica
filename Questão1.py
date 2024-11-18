#Questão 1

import statistics
import math
import matplotlib.pyplot as plt

areas = [
    (300, 399),
    (400, 499),
    (500, 599),
    (600, 699),
    (700, 799),
    (800, 899),
    (900, 999),
    (1000, 1099),
    (1100, 1199)
]

frequencias = [14, 46, 58, 76, 68, 62, 48, 22, 6]

pontos_medios = []
for area in areas:
    inicio, fim = area
    ponto_medio = (inicio + fim) / 2
    pontos_medios.append(ponto_medio)

dados = []
for i in range(len(areas)):
    dados.extend([pontos_medios[i]] * frequencias[i])

media = sum(dados) / len(dados)

soma_dos_quadrados = 0
for dado in dados:
    soma_dos_quadrados += (dado - media) ** 2
desvio_padrao = math.sqrt(soma_dos_quadrados / len(dados))

mediana = statistics.median(dados)

contagem = {}
for dado in dados:
    if dado in contagem:
        contagem[dado] += 1
    else:
        contagem[dado] = 1

max_frequencia = max(contagem.values())
moda = [k for k, v in contagem.items() if v == max_frequencia]

if len(moda) > 1:
    moda = "Não tem moda"
else:
    moda = moda[0]

dados_ordenados = sorted(dados)

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

print(f" A Média é: {media:.2f}")
print(f" A Mediana é : {mediana:.2f}")
print(f" A Moda é : {moda}")
print(f"O Desvio Padrão é: {desvio_padrao:.2f}")
print(f"O Quartil 1 (Q1) é: {q1:.2f}")
print(f"O Decil 3 (D3) é: {d3:.2f}")
print(f"O Decil 7 (D7) é: {d7:.2f}")
print(f" O Percentil 15 (P15) é: {p15:.2f}")
print(f" o Percentil 90 (P90) é: {p90:.2f}")

plt.bar([f'{inicio}-{fim}' for inicio, fim in areas], frequencias, color='lightblue')
plt.title("Distribuição das Frequencias por area")
plt.xlabel("areas")
plt.ylabel("frequência")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
