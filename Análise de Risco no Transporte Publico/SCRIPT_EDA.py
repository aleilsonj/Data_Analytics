# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:00:46 2024

@author: ALEILSON
"""
# %% 
import os
# Defina o caminho do novo diretório no formato Windows
novo_diretorio = r'C:\Users\ALEILSON\Documents\github\Data_Analytics\Análise de Risco no Transporte Publico'  # Use r'' para evitar problemas de escape
# Altera o diretório de trabalho
os.chdir(novo_diretorio)
# Verifique se o diretório de trabalho foi alterad
print(os.getcwd())

# %% Introdução

'''
Este projeto tem como objetivo analisar os dados de acidentes que ocorrem no 
transporte público. Alguns dos objetivos são compreender qual o acidente mais 
frequente, qual a faixa etária mais afetada e quais são as características das 
vítimas que sofrem acidentes.

Para alcançar esses objetivos, serão utilizadas ferramentas de análise de dados.
O objetivo é responder a essas perguntas e outras que possam auxiliar na 
tomada de decisão para futuras medidas com o objetivo de prevenir acidentes no
transporte público.

Com essas informações, espera-se gerar insights valiosos para o desenvolvimento
de estratégias mais eficazes de prevenção de acidentes no transporte público,
visando melhorar a segurança dos usuários.

'''

# %% Carregando pacotes
import pandas as pd
import numpy as np
from pandasql import sqldf
import matplotlib.pyplot as plt
import seaborn as sns

# %% Carregando dataframe
df = pd.read_excel('TFL Bus Safety.xlsx')
# Criando uma conexão com o DataFrame
pysqldf = lambda q: sqldf(q, globals())

# %% Análise dos dados
'''Serão utilizadas ferramentas de análise de dados para responder as perguntas 
propostas no objetivo do projeto, como identificar o tipo de acidente mais 
frequente, a faixa etária mais afetada e as características das vítimas que 
sofrem acidentes. Além disso, outras análises serão realizadas para gerar 
insights valiosos para o desenvolvimento de estratégias de prevenção de 
acidentes no transporte público.
'''
# %% Qual a quantidade de incidentes por gênero?
#  Executando consulta SQL
query = '''
        SELECT 
            "Victims Sex" AS Sex, 
            COUNT(*) AS Victims 
        FROM 
            df 
        GROUP BY 
            "Victims Sex"
        ORDER BY 
            Victims 
                DESC
        '''

resultado = pysqldf(query)

# Exibindo os resultados
print(resultado.head())

# %% Executnado com Pandas
df['Victims Sex'].value_counts()

'''
Observando os resultados da query, vemos que a maioria dos incidentes 
aconteceram com pessoas do gênero feminino:

Cerca de 11.847 vítimas são do gênero feminino;
As vítimas do gênero masculino são 7.709;
E cerca de 3.602 vítimas não possuem informação de gênero.
'''

# %% Plot 1 Qual a quantidade de incidentes por gênero?
# Criar o gráfico de barras horizontal
plt.figure(figsize=(10, 6))
plt.bar(resultado['Sex'], resultado['Victims'], color=['pink', 'blue', 'gray'])

# Remover as linhas de grade
plt.grid(False)
plt.title('Accidents by gender')
plt.gca().axes.yaxis.set_visible(False)
plt.gca().axes.xaxis.set_visible(True)
# Remove as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# Adiciona os valores de contagem no topo de cada barra
for index, value in enumerate(resultado['Victims']):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

# Salvar o gráfico como imagem
plt.savefig('Accidents by gender.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
'''
Analisando o gráfico de pizza acima, fica claro que a maior parte das vítimas 
são do gênero feminino, representando 51,16% dos gêneros das vítimas que 
sofreram algum tipo de incidente. Já o gênero masculino representa 33,29% das 
vítimas que sofreram algum incidente nesse período, e 15,55% não possuem 
informações sobre o gênero.
'''

# %% Qual faixa etária esteve mais envolvida nos incidentes?
# Executando consulta SQL
query2 = '''
        SELECT 
            "Victims Age" AS "Age Group", 
            COUNT (*) AS Victims 
        FROM 
            df 
        GROUP BY 
            "Victims Age"
        ORDER BY 
            Victims 
                DESC
        '''

resultado2 = pysqldf(query2)

# Exibindo o resultado
print(resultado2)

# %%
# Com Pandas
df['Victims Age'].value_counts()

#%%
# gráfico de barras horizontal
plt.figure(figsize=(10, 6))
plt.bar(resultado2['Age Group'],
        resultado2['Victims'],
        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Definir a cor de fundo como branco
plt.gca().set_facecolor('white')

# Remover as linhas de grade
plt.grid(False)

# Adicionar o título
plt.title('Victims by Age')

# Remover o eixo y, ticks e labels
plt.gca().axes.yaxis.set_visible(False)

# Remover eixo x, ticks e labels
plt.gca().axes.xaxis.set_visible(True)

# Remover as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Adicionar os valores de contagem no topo de cada barra
for index, value in enumerate(resultado2['Victims']):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

# Salvar o gráfico como imagem
plt.savefig('Victims by Age.png', format='png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()

# %%
'''
É possível ver no resultado da query acima o número de vítimas por faixa etária:

Os adultos são as vítimas que mais sofreram algum tipo de incidente. 
Eles representam cerca de 10.754 vítimas;
A segunda maior contabilização de vítimas não tem sua faixa etária informada, 
totalizando 7.135 vítimas;
O grupo que menos sofreu algum tipo de incidente foram os jovens. 
Estes representam um total de 319 vítimas.
Vejamos o gráfico a seguir para melhor visualização dessas informações.
Ao analisar o gráfico de barras acima, é possível ver que as vítimas 
consideradas adultas foram o grupo que mais contabilizou incidentes, 
totalizando um número superior a 10.000 vítimas. Já os grupos dos idosos 
e crianças apresentaram um número de vítimas inferior a 3.000. E os jovens 
foram os que menos contabilizaram algum tipo de incidente nesse período de 
estudo.
'''

# %% Qual o percentual de incidentes por tipo de evento (Incident Event Type)?
# Executando consulta SQL
query3 = '''
        SELECT 
            "Incident Event Type", 
            COUNT(*) AS Count, 
            ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM df), 2) AS Percentual
        FROM 
            df
        GROUP BY 
            "Incident Event Type"
        ORDER BY 
            Count 
                DESC
        '''

resultado3 = pysqldf(query3)

# Exibindo os resultados
print(resultado3)

# %%

# Ordenando o DataFrame do maior para o menor em relação à coluna 'Percentual'
resultado3 = resultado3.sort_values(by='Percentual', ascending=True)

# %% Plot 3

# Criando uma coloração baseada nos percentuais
colors = plt.cm.Reds(np.linspace(0.3, 1, len(resultado3)))

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.barh(resultado3['Incident Event Type'], resultado3['Percentual'], color=colors)
plt.xlabel('Porcentagem (%)')
plt.title('Incident Event Type')
plt.xlim(0, 35)  # Ajuste o limite do eixo x se necessário

# Remover o eixo y, ticks e labels
plt.gca().axes.yaxis.set_visible(True)

# Remover eixo x, ticks e labels
plt.gca().axes.xaxis.set_visible(True)

# Remover as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Adicionando os rótulos das porcentagens
for index, value in enumerate(resultado3['Percentual']):
    plt.text(value, index, f'{value:.2f}%', va='center')

plt.tight_layout()

# Salvar o gráfico como imagem
plt.savefig('Incident Event Type.png', format='png', dpi=300, bbox_inches='tight')
plt.show()


'''
Observando os resultados sobre o percentual por tipo de incidente na query 
acima, vemos:

Slip Trip Falls - que representam os incidentes como escorregões, tropeços ou 
quedas. Esses são aproximadamente 30% do total de incidentes.
Onboard Injuries - São as lesões que ocorreram a bordo do veículo, que nesse 
caso são os transportes públicos. Esse tipo de incidente representa 
aproximadamente 28% do total.
Robbery e Fire - são os incidentes com menor ocorrência. O primeiro se refere 
aos roubos com ameaças ou uso de força e o segundo faz referência a incidentes 
com fogo.
Eventos com algum tipo de violência física são os com menores ocorrências.

Os acidentes com escorregões, tropeços e quedas são os que apresentam a maior 
contagem de vítimas, seguidos pelos acidentes que ocorrem com as vítimas que 
estão a bordo do transporte público, os danos pessoais e os acidentes por 
colisões.
'''

# %% Como foi a evolução de incidentes por mês ao longo do tempo?
# Executando consulta SQL
query4 = '''
    SELECT 
        strftime('%m', "Date Of Incident") AS mes,
        strftime('%Y', "Date Of Incident") AS ano,
        strftime('%m-%Y', "Date Of Incident") AS data,
        COUNT(*) AS num_acidentes
    FROM 
        df
    GROUP BY 
        mes, ano
    ORDER BY 
        ano, mes
        '''
resultado4 = pysqldf(query4)
# %% Com Pandas

df['Date Of Incident'] = pd.to_datetime(df['Date Of Incident'])
result = df.groupby([pd.Grouper(key='Date Of Incident', freq='M')])['Date Of Incident'].agg(['count'])
result = result.reset_index()
result['data'] = result['Date Of Incident'].dt.strftime('%m-%Y')
result = result.drop(columns=['Date Of Incident'])
result = result.rename(columns={'count': 'num_acidentes'})
result = result[['data', 'num_acidentes']]

# %%
# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.plot(result['data'], result['num_acidentes'], marker='o',
         linestyle='-', color='b', label='Valores anuais')
plt.title('Date Of Incident')

# Rotacionando o label do eixo x
plt.xticks(rotation=45)

# Removendo apenas os ticks do eixo y, se for o desejado
plt.gca().axes.yaxis.set_visible(True)

# Removendo apenas os ticks do eixo x, se for o desejado
plt.gca().axes.xaxis.set_visible(True)

plt.tight_layout()
# Salvar o gráfico como imagem
plt.savefig('Date Of Incident.png', format='png', dpi=300, bbox_inches='tight')
plt.show()


'''
Ao observar o gráfico de linhas sobre a trajetória dos acidentes ao longo do 
tempo, podemos notar que o maior pico foi observado em julho de 2017 e o menor 
número de incidentes foi registrado em fevereiro de 2015. O maior pico 
contabilizou cerca de 650 vítimas e o menor, 371.

Além disso, em comparação com os anos de 2015 e 2016, o ano de 2017 apresentou 
patamares mais altos no número de incidentes, tendo uma tendência crescente a 
partir de janeiro de 2017.
'''

# %% Quando o incidente foi “Collision Incident” em qual mês houve o maior número de incidentes envolvendo pessoas do sexo feminino?
# Executando consulta SQL
query5 = '''
    SELECT 
        strftime('%m', "Date Of Incident") AS mes,
        COUNT(*) AS num_acidentes
    FROM 
        df
    WHERE
        "Victims Sex" = 'Female' AND
        "Incident Event Type" = 'Collision Incident' 
    GROUP BY 
        mes
    ORDER BY 
        mes 
            ASC
'''

resultado5 = pysqldf(query5)


# %% Com Pandas

result5 = df[(df['Victims Sex'] == 'Female') & 
             (df['Incident Event Type'] == 'Collision Incident')]['Date Of Incident'].dt.month.value_counts().sort_index().reset_index().rename(columns={'index': 'mes', 'Date Of Incident': 'contagem'})


# Adicionando uma coluna com os nomes dos meses
import calendar
result5['mes_nome'] = result5['mes'].apply(lambda x: calendar.month_name[x])
# %% plot 5
# Criar o gráfico de barras horizontal
plt.figure(figsize=(10, 6))
plt.bar(result5['mes_nome'], result5['contagem'], color= 'red')

# Remover as linhas de grade
plt.grid(False)

# Adicionar o título
plt.title('Female: Collision Incident')

# Rotacionando o label do eixo x
plt.xticks(rotation=45)

# Remover o eixo y, ticks e labels
plt.gca().axes.yaxis.set_visible(False)

# Remover eixo x, ticks e labels
plt.gca().axes.xaxis.set_visible(True)

# Remover as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Adicionar os valores de contagem no topo de cada barra
for index, value in enumerate(result5['contagem']):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')
    
plt.tight_layout()

# Salvar o gráfico como imagem
plt.savefig('FemaleCollisionIncident.png', format='png', dpi=300, bbox_inches='tight')

plt.show()


'''
Durante a maior parte da série observada, o número de incidentes envolvendo 
pessoas do gênero feminino manteve-se entre 110 e 130 vítimas contabilizadas. 
No entanto, em setembro, o número de vítimas aproximou-se de 160, sendo esse o
maior pico observado, enquanto em dezembro, o número ficou abaixo das 80 
vítimas contabilizadas.
'''

# %% Qual foi a média de incidentes por mês envolvendo crianças (Child)?
# Executando consulta SQL
query6 = '''
    SELECT 
        strftime('%m-%Y', "Date Of Incident") AS Data,
        AVG(CASE WHEN "Victims Age" = 'Child' THEN 1.0 ELSE 0.0 END) AS avg_child_incidents
    FROM 
        df
    GROUP BY 
        strftime('%Y-%m', "Date Of Incident")
'''

resultado6 = pysqldf(query6)
resultado6

# %%
#Com pandas
df['Data'] = df['Date Of Incident'].dt.strftime('%m-%Y')
df['avg_child_incidents'] = np.where(df['Victims Age'] == 'Child', 1.0, 0.0)
df_grouped = df.groupby([pd.Grouper(key='Date Of Incident', freq='M'), 'Data'])['avg_child_incidents'].mean().reset_index()
result6 = df_grouped.groupby('Data')['avg_child_incidents'].mean().reset_index().rename(columns={'Data': 'Data', 'avg_child_incidents': 'avg_child_incidents'})


# %% Plot 6
# Identificar os valores máximos e mínimos
max_value = result6['avg_child_incidents'].max()
min_value = result6['avg_child_incidents'].min()
max_date = result6.loc[result6['avg_child_incidents'] == max_value, 'Data'].values[0]
min_date = result6.loc[result6['avg_child_incidents'] == min_value, 'Data'].values[0]

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.plot(result6['Data'], result6['avg_child_incidents'], marker='o', linestyle='-', color='b', label='Valores anuais')
plt.title('Children: Average Number of Incidents')

# Rotacionando os rótulos do eixo x
plt.xticks(rotation=45)

# Anotando os pontos de alta e baixa
plt.text(max_date, max_value, f'Máximo: {max_value}', ha='center', va='bottom', color='red', fontsize=10)
plt.text(min_date, min_value, f'Mínimo: {min_value}', ha='center', va='top', color='green', fontsize=10)

# Exibindo os ticks e labels dos eixos x e y
plt.gca().axes.yaxis.set_visible(True)
plt.gca().axes.xaxis.set_visible(True)

plt.tight_layout()

# Salvar o gráfico como imagem
plt.savefig('Children.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

'''
Entre dezembro de 2015 e junho de 2016, houve um aumento na média de incidentes,
 atingindo seu pico em junho de 2016. A partir dessa data, a série apresentou 
 uma trajetória decrescente até janeiro de 2017.

Em relação aos anos de 2016 e 2017, o mês de junho apresentou os maiores picos 
na média de incidentes observados.
'''

# %% Considerando a descrição de incidente como “Injuries treated on scene” (coluna Injury Result Description), qual o total de incidentes de pessoas do sexo masculino e sexo feminino?
# Executando consulta SQL
query7 = '''
    SELECT
        "Victims Sex",
        COUNT(*) AS num_acidentes
    FROM 
        df
    WHERE
        "Injury Result Description" = 'Injuries treated on scene' 
    GROUP BY 
        "Victims Sex"
    
'''

resultado7 = pysqldf(query7)

# Exibindo os resultados
print(resultado7)

# %% Com pandas
result7 = df[(df['Injury Result Description'] == 'Injuries treated on scene')]['Victims Sex'].value_counts()

# %%
plt.figure(figsize=(10, 6))
plt.bar(resultado7["Victims Sex"], resultado7["num_acidentes"], color=['pink', 'blue', 'gray'])
plt.title('Total of On-Site Treated Injury Incidents by Gender')
plt.ylabel('Number of Incidents')

# Remover as linhas de grade
plt.grid(False)
# Remover o eixo y, ticks e labels
plt.gca().axes.yaxis.set_visible(False)
# Remover eixo x, ticks e labels
plt.gca().axes.xaxis.set_visible(True)
# Remover as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# Adicionar os valores de contagem no topo de cada barra
for index, value in enumerate(resultado7["num_acidentes"]):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')
    
plt.tight_layout()

# Salvar o gráfico como imagem
plt.savefig('On-Site Treated.png', format='png', dpi=300, bbox_inches='tight')

plt.show()

'''
As vítimas do sexo feminino representam o maior número das vítimas que tiveram
suas lesões tratadas no local, totalizando cerca de 8.816 vítimas. As vítimas 
do sexo masculino que receberam tratamento no local representam um total 
de 5.632 vítimas, enquanto que 2.888 vítimas não tiveram seu gênero informado.
 
Como vimos anteriormente, as vítimas do sexo feminino representam o maior 
número de vítimas que receberam tratamento no local do incidente, 
correspondendo a aproximadamente 51% das vítimas, enquanto que o sexo 
representa cerca de 33% das vítimas.
'''
# %% No ano de 2017 em qual mês houve mais incidentes com idosos (Elderly)?

# Executando consulta SQL
query8 = '''
    SELECT
        strftime('%m', "Date Of Incident") AS mes,
        COUNT(*) AS num_acidentes_Elderly
    FROM 
        df
    WHERE
        "Victims Age" = 'Elderly' AND
        strftime('%Y', "Date Of Incident") = '2017'
    GROUP BY 
        strftime('%m', "Date Of Incident")
    ORDER BY
        mes
            ASC
'''

resultado8 = pysqldf(query8)

# %% Com pandas
result8 = df[(df['Victims Age'] == 'Elderly') & (df['Year'] == 2017)]['Date Of Incident'].value_counts().sort_index()

# %%
# Convertendo a coluna 'mes' para inteiros
resultado8['mes'] = resultado8['mes'].astype(int)

# Criar a nova coluna 'mes_nome' usando calendar.month_name
resultado8['mes_nome'] = resultado8['mes'].apply(lambda x: calendar.month_name[x])
# %% Plot 6
# Identificar os valores máximos e mínimos
max_value = resultado8['num_acidentes_Elderly'].max()
min_value = resultado8['num_acidentes_Elderly'].min()
max_date = resultado8.loc[resultado8['num_acidentes_Elderly'] == max_value, 'mes'].values[0]
min_date = resultado8.loc[resultado8['num_acidentes_Elderly'] == min_value, 'mes'].values[0]

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.plot(resultado8['mes_nome'], resultado8['num_acidentes_Elderly'], marker='o', linestyle='-', color='b', label='Valores anuais')
plt.title('Incidents involving elderly individuals per month in 2017')

# Rotacionando os rótulos do eixo x
plt.xticks(rotation=45)

# Anotando os pontos de alta e baixa
plt.text(max_date, max_value, f'Máximo: {max_value}',
         ha='center', va='bottom', color='red', fontsize=10)
plt.text(min_date, min_value, f'Mínimo: {min_value}',
         ha='center', va='top', color='green', fontsize=10)
# Exibindo os ticks e labels dos eixos x e y
plt.gca().axes.yaxis.set_visible(True)
plt.gca().axes.xaxis.set_visible(True)
plt.tight_layout()
# Salvar o gráfico como imagem
plt.savefig('elderly individuals in 2017.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

'''
O mês que apresentou o maior número de incidentes envolvendo indivíduos idosos
 foi julho, com mais de 80 vítimas. Já o mês com o menor número de incidentes 
 registrados com idosos foi fevereiro.
'''

# %% Considerando o Operador qual a distribuição de incidentes ao longo do tempo?
# Executando consulta SQL
query9 = '''
    SELECT
        "Operator",
        strftime('%m', "Date Of Incident") AS mes,
        strftime('%Y', "Date Of Incident") AS mes,
        COUNT(*) AS num_acidentes
    FROM 
        df
    GROUP BY 
        "Operator"
    ORDER BY
        num_acidentes
            DESC
   
'''
# %%
resultado9 = pysqldf(query9)

#%%
# Ordenando os dados do maior para o menor
resultado9 = resultado9.sort_values(by='num_acidentes', ascending=True)
# Definindo uma paleta de cores
palette = sns.color_palette("Spectral_r", n_colors=len(resultado9))
# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 6))
plt.barh(resultado9['Operator'], resultado9['num_acidentes'], color=palette)
plt.title('Incident Operator')
# Remover o eixo y, ticks e labels
plt.gca().axes.yaxis.set_visible(True)
# Remover eixo x, ticks e labels
plt.gca().axes.xaxis.set_visible(True)
# Remover as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()

# Salvar o gráfico como imagem
plt.savefig('IncidentOperator.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
'''
Observando a distribuição dos incidentes ao longo do tempo, é possível perceber
que a maioria dos incidentes ocorrem com os operadores Metroline e Arriva 
London North, enquanto que os com menor número de vítimas são 
Sullivan Bus & Coach e Uno Buses.
'''

# %% Qual o tipo de incidente mais comum com ciclistas?
# Executando consulta SQL
query10 = '''
    SELECT
        "Incident Event Type",
        COUNT(*) AS num_acidentes
    FROM 
        df
    WHERE
        "Victim Category" = 'Cyclist'
    GROUP BY 
        "Incident Event Type"
   
'''

resultado10 = pysqldf(query10)
# %%
result10 = df[(df['Victim Category'] == 'Cyclist')]['Incident Event Type'].value_counts()

# %%
# Criar o gráfico de barras horizontal
plt.figure(figsize=(10, 6))
plt.bar(resultado10['Incident Event Type'],
        resultado10['num_acidentes'],
        color=['#d62728', '#1f77b4', '#ff7f0e', '#2ca02c'])

# Definir a cor de fundo como branco
plt.gca().set_facecolor('white')
# Remover as linhas de grade
plt.grid(False)
# Adicionar o título
plt.title('Type of incident involving cyclists')
#Remover o eixo y, ticks e labels
plt.gca().axes.yaxis.set_visible(False)
# Remover eixo x, ticks e labels
plt.gca().axes.xaxis.set_visible(True)
# Remover as bordas (spines) do gráfico
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# Adicionar os valores de contagem no topo de cada barra
for index, value in enumerate(resultado10['num_acidentes']):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

# Salvar o gráfico como imagem
plt.savefig('involving cyclists.png', format='png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()

# %%
# Criando o gráfico
plt.subplots(figsize=(12, 8))
sns.set_style("whitegrid")
sns.barplot(x='Incident Event Type', y='num_acidentes', data=resultado10, palette='Spectral_r')
# Adicionando rótulos e título
plt.title(' Type of incident involving cyclists')
plt.xlabel('Month')
plt.ylabel('Number Victimis')
# Exibindo o gráfico
plt.show()

'''
Ao observar o gráfico acima, fica claro que a maioria dos acidentes envolvendo
ciclistas são colisões. Ou seja, quando ocorre um acidente envolvendo um 
ciclista, há uma grande possibilidade de que esse acidente seja uma colisão.
'''

## Conclusão
'''
Este projeto tem como objetivo analisar dados de acidentes no transporte 
público, visando compreender os tipos de acidentes mais frequentes, a 
faixa etária mais afetada e as características das vítimas. Os resultados da 
análise mostraram que a maioria das vítimas são mulheres, e que os acidentes 
mais frequentes são escorregões, tropeços e quedas. O ano de 2017 teve um 
número maior de incidentes em comparação com os anos anteriores, com picos 
em junho e julho. A análise desses dados pode ser útil para o desenvolvimento 
de medidas preventivas mais eficazes para garantir a segurança dos usuários 
do transporte público.
'''