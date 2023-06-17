#Jhonata Goncalves Antunes
#202102212812

# =============== QUESTÃO 1 LETRA A ===============
import pandas as pd

df = pd.read_csv('world_alcohol.csv', sep=',')


# Agrupa os tipos de bebidas em variaveis
Wine = df.loc[df['Beverage Types'] == 'Wine']
Others = df.loc[df['Beverage Types'] == 'Others']
Spirits = df.loc[df['Beverage Types'] == 'Spirits']
Beer = df.loc[df['Beverage Types'] == 'Beer']

print("Bebida: Wine")
print(Wine)
print("\n")

print("Bebida: Others")
print(Others)
print("\n")

print("Bebida: Beer")
print(Beer)
print("\n")

print("Bebida: Spirits")
print(Spirits)
print("\n")







# =============== QUESTÃO 1 LETRA B ===============
import pandas as pd
df = pd.read_csv('world_alcohol.csv', sep=',')

# ============= Agrupamento das Regiões =============
africa = df.loc[df['WHO region'] == 'Africa']
americas = df.loc[df['WHO region'] == 'Americas']
westernPacific = df.loc[df['WHO region'] == 'Western Pacific']
southEastAsia = df.loc[df['WHO region'] == 'South-East Asia']
europe = df.loc[df['WHO region'] == 'Europe']
easternMediterranean = df.loc[df['WHO region'] == 'Eastern Mediterranean']

# ============= Agrupamento das Anos =============
ano1984 = df.loc[df['Year'] == 1984]
ano1985 = df.loc[df['Year'] == 1985]
ano1986 = df.loc[df['Year'] == 1986]
ano1987 = df.loc[df['Year'] == 1987]
ano1989 = df.loc[df['Year'] == 1989]

# ============= Exibição das Regiões =============

print("Região: Africa\n",africa)
print("Região: AMerica\n",americas)
print("Região: Pacífico Ocidental\n",westernPacific)
print("Região: Sudeste da Ásia\n",southEastAsia)
print("Região: Europa\n",europe)
print("Região: Leste do Mediterrâneo\n",easternMediterranean)

# ============= Exibição dos anos =============
print("Ano:"+"1984",ano1984,"\n")
print("Ano:"+"1985",ano1985,"\n")
print("Ano"+"1986",ano1986,"\n")
print("Ano:"+"1987",ano1987,"\n")
print("Ano:"+"1989",ano1989,"\n")









# =============== QUESTÃO 1 LETRA C ===============
import pandas as pd
df = pd.read_csv('world_alcohol.csv', sep=',')

# faz a contagem das ocorrencias: regioes e paises e soma os valores das bebidas
regioes = df['WHO region'].value_counts()
paises = df['Country'].value_counts()
soma = df['Display Value'].sum()


print(regioes)
print(paises)

print(f'A soma das bebidas é {soma:.2f}')
print()
#print()






# =============== QUESTÃO 1 LETRA D ===============
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world_alcohol.csv', sep=',')

# faz a analise descritiva
m = df['Display Value'].mean()
print(f"A média das bebidas é {m:.2f}")

mo = df['Display Value'].mode()[0]
print(f"A moda das bebidas é {mo}")

med = df['Display Value'].median()
print(f"A mediana das bebidas é {med}")

estat_descritiva = df['Display Value'].describe()
print("Estatística Descritiva:")
print(estat_descritiva)

# faz o grafico comparativo e depois exibe
bebidasTipos = df.groupby('Beverage Types')
bebidasTipos['Display Value'].mean().plot.barh()

plt.xlabel('Tipo de Bebida')
plt.ylabel('Média dos Valores')
plt.title('Comparação das Médias por Tipo de Bebida')
plt.show()





# =============== QUESTÃO 1 LETRA E ===============
import pandas as pd
# armazena em variaveis bebidas de 1985 e regioes com bebidas maior que 4
df = pd.read_csv('world_alcohol.csv')
ano = df.loc[df['Year'] == 1985]['Beverage Types']
up4 = df.loc[df['Display Value'] > 4]['WHO region']
print("Bebidas do ano 1985")
print(ano)

print("Regiões com a Bebida maior que 4")
print(up4)





# =============== QUESTÃO 2 LETRA A ===============
import pandas as pd


#faz a requisição pegando o arquivo do github
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')
# procura os valores faltando e substitui pelo valor indicado
df = df.fillna(0.0)
print(df)




# =============== QUESTÃO 2 LETRA B ===============
import pandas as pd
#faz a requisição do arquivo csv no link github
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')

# armazena os valores usando o método loc para encontrar a coluna e linha
bacharel = df.loc[df['grau'] == 'Bacharelado']
licence = df.loc[df['grau'] == 'Licenciatura']
Tecno = df.loc[df['grau'] == 'tecnológico']

#exibe os os dados na tela
print(bacharel)
print(licence)
print(Tecno)





# =============== QUESTÃO 2 LETRA C ===============

import pandas as pd
# Agrupa os cursos em variaveis
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')
medicina = df.loc[df['curso_busca'] == "Medicina"]
enfermagem = df.loc[df['curso_busca'] == "Enfermagem"]
pedagogia = df.loc[df['curso_busca'] == "Pedagogia"]

print(medicina)
print(enfermagem)
print(pedagogia)





# =============== QUESTÃO 2 LETRA D ===============
import pandas as pd
# faz a requisição
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')

# agrupa os estados e calcula a media de cada
media_notas_estado = df.groupby('uf_busca')['nota_integral_ampla'].mean()
print(media_notas_estado)





# =============== QUESTÃO 2 LETRA E ===============
import pandas as pd
#faz a requisição
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')

# busca a coluna grau e verifica armazena os cursos do tipo Tecnológico
tecnologico = df.loc[df['grau'] == 'Tecnológico']

print(tecnologico)




# =============== QUESTÃO 2 LETRA F ===============
import pandas as pd
# faz a requisição e deleta a coluna "cidade_filtro" usando o método drop
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')
df = df.drop("cidade_filtro", axis='columns')
print(df.info)





# =============== QUESTÃO 2 LETRA G ===============
import pandas as pd
# agrupa os curso de medicina e calcula a média
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')
group = df.loc[df['curso_busca'] == 'Medicina']['mensalidade'].mean()
print(f'A média da mensalidade {group:.2f}')



# =============== QUESTÃO 2 LETRA H ===============
import pandas as pd
# agrupa a média da nota integral dos cursos de horário integral
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')
print(df.info)
group = df.loc[df['turno'] == 'Integral']['nota_integral_ampla'].mean()
print(f'A média é {group:.2f}')





# =============== QUESTÃO 2 LETRA I ===============
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')

media = df.loc[df['grau'] == 'Bacharelado']['nota_integral_ampla'].mean()
mediana  = df.loc[df['grau'] == 'Bacharelado']['nota_integral_ampla'].median()
moda = df.loc[df['grau'] == 'Bacharelado']['nota_integral_ampla'].mode()

# usa o método describe para descrever os dados
estat_desc = df.loc[df['grau'] == 'Bacharelado']['nota_integral_ampla'].describe()
print(estat_desc)




# =============== QUESTÃO 2 LETRA J ===============
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/jhon5103/datasets/main/cursos-prouni.csv', sep=',')

# cria o grafico  comparativo
grau = df.groupby('grau')['nota_integral_ampla'].mean()
plt.bar(grau.index, grau)
plt.xlabel('Curso')
plt.ylabel('Média das Notas Integral')
plt.title('Comparação das Médias das Notas de Integral de Cotas por Curso')
plt.show()




