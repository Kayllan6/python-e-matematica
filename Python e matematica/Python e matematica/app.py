# ANALISE DE DADOS - AREAS DE FORMAÇÃO NA GRADUAÇÃO

import pandas as pd
import matplotlib.pyplot as plt

arquivo = "Tabela_3_Areas_gerais_de_formacao_na_graduacao.xlsx"


df = pd.read_excel(arquivo, header=None)

dados = df.iloc[3:36].copy()
dados.columns = [
    "Local",
    "Total", "Total_Homens", "Total_Mulheres",
    "CTEM", "CTEM_Homens", "CTEM_Mulheres",
    "Educacao_Saude", "Educacao_Saude_Homens",
    "Educacao_Saude_Mulheres"
]


for coluna in dados.columns[1:]:
    dados[coluna] = pd.to_numeric(dados[coluna], errors="coerce")


brasil = dados.iloc[0]
regioes = dados.iloc[1:6].copy()
estados = dados.iloc[6:].copy()

# ---------------------------------------------------------
# GRAFICO 1 - PESSOAS COM GRADUACAO POR REGIAO
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(regioes["Local"], regioes["Total"] / 1_000_000)
plt.title("Pessoas com nivel superior completo por regiao")
plt.xlabel("Regiao")
plt.ylabel("Pessoas (em milhoes)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

print("\\nGRAFICO 1 - EXPLICACAO")
print("Este grafico compara a quantidade de pessoas com ensino superior completo")
print("nas cinco grandes regioes do Brasil. A barra mais alta representa a regiao")
print("com maior quantidade de pessoas graduadas.")
print("CONCLUSAO: o Sudeste apresenta o maior total, enquanto o Norte apresenta")
print("o menor total. Isso mostra uma concentracao maior de pessoas graduadas no Sudeste.")
print("A quantidade total, sozinha, nao indica a proporcao de graduados na populacao.")

# ---------------------------------------------------------
# GRAFICO 2 - HOMENS E MULHERES NO BRASIL
# ---------------------------------------------------------
categorias = ["Total", "Ciencia, Tecnologia,\nEngenharias e Matematica",
              "Educacao, Servicos,\nSaude e Bem-estar"]
homens = [
    brasil["Total_Homens"],
    brasil["CTEM_Homens"],
    brasil["Educacao_Saude_Homens"]
]
mulheres = [
    brasil["Total_Mulheres"],
    brasil["CTEM_Mulheres"],
    brasil["Educacao_Saude_Mulheres"]
]

posicoes = range(len(categorias))
largura = 0.35

plt.figure(figsize=(11, 6))
plt.bar([p - largura/2 for p in posicoes], [v/1_000_000 for v in homens],
        width=largura, label="Homens")
plt.bar([p + largura/2 for p in posicoes], [v/1_000_000 for v in mulheres],
        width=largura, label="Mulheres")
plt.title("Pessoas com graduacao por sexo e area de formacao")
plt.xlabel("Grupo")
plt.ylabel("Pessoas (em milhoes)")
plt.xticks(list(posicoes), categorias)
plt.legend()
plt.tight_layout()
plt.show()

print("\\nGRAFICO 2 - EXPLICACAO")
print("O grafico compara homens e mulheres no total de graduados e nas duas")
print("areas de formacao destacadas na planilha.")
print("CONCLUSAO: as mulheres sao maioria no total de pessoas graduadas.")
print("Na area de Ciencia, Tecnologia, Engenharias e Matematica, os homens")
print("sao maioria. Ja em Educacao, Servicos pessoais, Saude e Bem-estar,")
print("as mulheres representam a maior parte.")


posicoes = range(len(regioes))
largura = 0.35

plt.figure(figsize=(11, 6))
plt.bar([p - largura/2 for p in posicoes],
        regioes["CTEM"] / 1_000_000, width=largura,
        label="Ciencia, Tecnologia, Engenharias e Matematica")
plt.bar([p + largura/2 for p in posicoes],
        regioes["Educacao_Saude"] / 1_000_000, width=largura,
        label="Educacao, Servicos, Saude e Bem-estar")
plt.title("Areas de formacao por regiao")
plt.xlabel("Regiao")
plt.ylabel("Pessoas (em milhoes)")
plt.xticks(list(posicoes), regioes["Local"])
plt.legend()
plt.tight_layout()
plt.show()

print("\\nGRAFICO 3 - EXPLICACAO")
print("Este grafico mostra, em cada regiao, a quantidade de pessoas nas duas")
print("grandes areas de formacao apresentadas na tabela.")
print("CONCLUSAO: em todas as regioes, Educacao, Servicos pessoais, Saude e")
print("Bem-estar apresenta um numero maior de pessoas do que CTEM.")
print("O Sudeste possui os maiores numeros absolutos nas duas areas.")


top_ctem = estados.nlargest(10, "CTEM").sort_values("CTEM")
plt.figure(figsize=(10, 7))
plt.barh(top_ctem["Local"], top_ctem["CTEM"] / 1_000_000)
plt.title("10 estados com mais pessoas formadas em CTEM")
plt.xlabel("Pessoas (em milhoes)")
plt.ylabel("Estado")
plt.tight_layout()
plt.show()

print("\\nGRAFICO 4A - EXPLICACAO")
print("O grafico apresenta os dez estados com maior quantidade de pessoas")
print("formadas em Ciencia, Tecnologia, Engenharias e Matematica.")
print("CONCLUSAO: Sao Paulo aparece na primeira posicao, seguido por Minas Gerais")
print("e Rio de Janeiro. Os maiores numeros estao concentrados no Sudeste.")

top_educacao = estados.nlargest(10, "Educacao_Saude").sort_values("Educacao_Saude")
plt.figure(figsize=(10, 7))
plt.barh(top_educacao["Local"], top_educacao["Educacao_Saude"] / 1_000_000)
plt.title("10 estados com mais pessoas formadas em Educacao, Servicos, Saude e Bem-estar")
plt.xlabel("Pessoas (em milhoes)")
plt.ylabel("Estado")
plt.tight_layout()
plt.show()

print("\\nGRAFICO 4B - EXPLICACAO")
print("O grafico apresenta os dez estados com maior quantidade de pessoas")
print("na area de Educacao, Servicos pessoais, Saude e Bem-estar.")
print("CONCLUSAO: Sao Paulo lidera novamente, seguido por Minas Gerais")
print("e Rio de Janeiro. Isso reforca a concentracao dos maiores totais")
print("de graduados nos estados mais populosos do Sudeste.")


percentual_mulheres = brasil["Total_Mulheres"] / brasil["Total"] * 100
percentual_homens_ctem = brasil["CTEM_Homens"] / brasil["CTEM"] * 100
percentual_mulheres_educacao = (
    brasil["Educacao_Saude_Mulheres"] / brasil["Educacao_Saude"] * 100
)

print("\\nCONCLUSAO GERAL")
print(f"O Brasil possui {brasil['Total']:,.0f} pessoas com nivel superior completo.")
print(f"As mulheres representam {percentual_mulheres:.1f}% do total de graduados.")
print(f"Na area CTEM, os homens representam {percentual_homens_ctem:.1f}%.")
print(f"Na area de Educacao, Servicos, Saude e Bem-estar,")
print(f"as mulheres representam {percentual_mulheres_educacao:.1f}%.")
print("Os dados mostram diferencas na distribuicao por sexo entre as areas")
print("e uma concentracao de numeros absolutos de graduados na regiao Sudeste.")

print("\\nOBSERVACAO IMPORTANTE:")
print("A planilha apresenta contagens absolutas. Portanto, os estados e regioes")
print("mais populosos tendem a ter numeros maiores. Para comparar a proporcao")
print("de graduados entre populacoes, seria necessario ter tambem o total de")
print("habitantes de cada regiao ou estado.")
print("As duas areas destacadas sao apenas as categorias apresentadas nesta tabela;")
print("nao devem ser interpretadas como a totalidade de todas as areas de formacao.")
