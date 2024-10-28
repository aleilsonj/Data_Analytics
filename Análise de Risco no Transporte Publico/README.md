<p align="center">
  <img src="https://github.com/user-attachments/assets/1bf86df6-6747-45a4-bd90-fc7f347938c7" alt="acidente" style="width: 900px; height: 250px;">
</p>

# Formação Cientista de Dados da Data Science Academy - Projeto com Feedback 3

# Análise de Acidentes no Transporte Público
## Introdução
Este projeto tem como objetivo analisar dados de acidentes no transporte público da cidade de Londres, no período de 2015 a 2018. A análise visa compreender qual o tipo de acidente mais frequente, qual a faixa etária mais afetada e quais são as características das vítimas que sofrem acidentes. O intuito é gerar insights que possam auxiliar na tomada de decisão para futuras medidas com o objetivo de prevenir acidentes no transporte público e, assim, melhorar a segurança dos usuários.

## Metodologia
### Coleta de dados
Os dados dos acidentes no transporte público de Londres serão coletados do arquivo “TFL Bus Safety.xlsx” referente aos anos de 2015 a 2018.

### Visualização de dados
Serão utilizadas ferramentas de visualização de dados, como o Matplotlib, para a criação de gráficos e visualizações que ajudem na compreensão dos resultados e na apresentação dos insights gerados.

### Implementação
O projeto será implementado utilizando a linguagem Python e a linguagem SQL, a fim de realizar as análises necessárias. Para isso, serão utilizadas as seguintes bibliotecas:

- Pandas: para manipulação de dados;
- Pandasql: para realizar consultas SQL em dataframes do Pandas;
- Matplotlib: para visualização de gráficos;

## EDA
Ao observar os resultados do gráfico a seguir, notamos que a maioria dos incidentes ocorreu com pessoas do gênero feminino. Ao todo, 11.847 vítimas são do gênero feminino, enquanto as vítimas do gênero masculino somam 7.709. Além disso, cerca de 3.602 vítimas não têm informações sobre seu gênero.
#### Gráfico 1
**1 -Qual a quantidade de incidentes por gênero?**

<p align="center">
  <img src="https://github.com/user-attachments/assets/6b548e32-b04a-48e9-8896-b94304b9ead5" alt="Accidents by gender" style="width: 550px; height: auto;">
</p>
Através da análise do gráfico de barras, é evidente que a maior parte das vítimas pertence ao gênero feminino, representando 51,16% do total de vítimas que sofreram algum tipo de incidente. Em contrapartida, o gênero masculino corresponde a 33,29% das vítimas, e 15,55% das vítimas não possuem informações sobre o gênero.

#### Gráfico 2 
**2 - Qual faixa etária esteve mais envolvida nos incidentes?**

O gráfico 2 ilustra o número total de vítimas de incidentes, segmentado por faixa etária. Os dados revelam que os adultos são o grupo mais afetado, enquanto os jovens representam o menor número de vítimas. A análise a seguir detalha a distribuição e os insights sobre cada grupo etário.
<p align="center">
  <img src="https://github.com/user-attachments/assets/4cfc2d54-6020-41ee-a294-ef8b92d1a328" alt="Accidents by gender" style="width: 550px; height: auto;">
</p>
A consulta acima revela o número de vítimas por faixa etária:


- **Adultos**: O grupo mais afetado, totalizando cerca de **10.754 vítimas**.
- **Desconhecido**: O segundo maior grupo, com **7.135 vítimas** cuja faixa etária não foi informada.
- **Jovens**: O grupo que menos sofreu incidentes, contabilizando apenas **319 vítimas**.


Analisando o gráfico de barras, nota-se que as vítimas adultas foram as mais numerosas, superando a marca de 10.000. Por outro lado, os grupos de idosos e crianças apresentaram menos de 3.000 vítimas cada. Os jovens, por sua vez, foram os que menos incidentes registraram durante o período de estudo.

#### Gráfico 3
**Qual o percentual de incidentes por tipo de evento (Incident Event Type)?**

Observando os resultados sobre o percentual por tipo de incidente na query 
acima, vemos:

<p align="center">
  <img src="https://github.com/user-attachments/assets/aac9d0b1-c14f-49d2-99c2-1d12021a96ed" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

- Slip Trip Falls - que representam os incidentes como escorregões, tropeços ou quedas. Esses são aproximadamente 30% do total de incidentes. 
- Onboard Injuries - São as lesões que ocorreram a bordo do veículo, que nesse caso são os transportes públicos. Esse tipo de incidente representa aproximadamente 28% do total. 
- Robbery e Fire - são os incidentes com menor ocorrência. O primeiro se refere aos roubos com ameaças ou uso de força e o segundo faz referência a incidentes com fogo.Eventos com algum tipo de iolência física são os com menores ocorrências.
- Os acidentes com escorregões, tropeços e quedas são os que apresentam a maior contagem de vítimas, seguidos pelos acidentes que correm com as vítimas que estão a bordo do transporte público, os danos pessoais e os acidentes por colisões.

#### Gráfico 4
**Como foi a evolução de incidentes por mês ao longo do tempo?**

Vejamos a seguir a evolução de acidentes ao londo do tempo:

<p align="center">
  <img src="https://github.com/user-attachments/assets/e63c8084-a4d3-4155-8134-9d0865552867" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

Ao observar o gráfico de linhas sobre a trajetória dos acidentes ao longo do tempo, podemos notar que o maior pico foi observado em julho de 2017 e o menor número de incidentes foi registrado em fevereiro de 2015. O maior pico contabilizou cerca de 650 vítimas e o menor, 371.

Além disso, em comparação com os anos de 2015 e 2016, o ano de 2017 apresentou patamares mais altos no número de incidentes, tendo uma tendência crescente a partir de janeiro de 2017.

#### Gráfico 5
**Quando o incidente foi “Collision Incident” em qual mês houve o maior número de incidentes envolvendo pessoas do sexo feminino?**

Vejamos a seguir:

<p align="center">
  <img src="https://github.com/user-attachments/assets/93a4d206-12c2-4766-8036-4508437ec434" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

Durante a maior parte da série observada, o número de incidentes envolvendo pessoas do gênero feminino manteve-se entre 110 e 130 vítimas contabilizadas. No entanto, em setembro, o número de vítimas aproximou-se de 160, sendo esse o maior pico observado, enquanto em dezembro, o número ficou abaixo das 80 vítimas contabilizadas.

#### Gráfico 6
**Qual foi a média de incidentes por mês envolvendo crianças (Child)?**

os dados mostraram um crescimento acentuado nos incidentes, com um pico significativo em junho, vejamos a seguir:

<p align="center">
  <img src="https://github.com/user-attachments/assets/85368822-72a4-4b34-bb82-19a6e1d9e816" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

Entre dezembro de 2015 e junho de 2016, houve um aumento na média de incidentes, atingindo seu pico em junho de 2016. A partir dessa data, a série apresentou uma trajetória decrescente até janeiro de 2017.

Em relação aos anos de 2016 e 2017, o mês de junho apresentou os maiores picos na média de incidentes observados.

#### Gráfico 7
**Considerando a descrição de incidente como “Injuries treated on scene” (coluna Injury Result Description), qual o total de incidentes de pessoas do sexo masculino e sexo feminino?**

A análise dos dados de atendimento revela uma disparidade significativa entre os gêneros entre as vítimas tratadas no local dos incidentes:

<p align="center">
  <img src="https://github.com/user-attachments/assets/a38f8d0e-acad-4b5d-9471-3e7044971401" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

As vítimas do sexo feminino representam o maior número das vítimas que tiveram suas lesões tratadas no local, totalizando cerca de 8.816 vítimas. As vítimas do sexo masculino que receberam tratamento no local representam um total de 5.632 vítimas, enquanto que 2.888 vítimas não tiveram seu gênero informado.
 
Como vimos anteriormente, as vítimas do sexo feminino representam o maior número de vítimas que receberam tratamento no local do incidente, correspondendo a aproximadamente 51% das vítimas, enquanto que o sexo representa cerca de 33% das vítimas.

#### Gráfico 8
**No ano de 2017 em qual mês houve mais incidentes com idosos (Elderly)**

Vamos analisar o gráfico 8: 

<p align="center">
  <img src="https://github.com/user-attachments/assets/70fbbc68-775c-44a7-9a2e-3b7ec4f614a5" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

O mês que apresentou o maior número de incidentes envolvendo indivíduos idosos foi julho, com mais de 80 vítimas. Já o mês com o menor número de incidentes registrados com idosos foi fevereiro.


#### Gráfico 9
**Considerando o Operador qual a distribuição de incidentes ao longo do tempo?**

A análise da distribuição temporal dos incidentes revela que os operadores Metroline e Arriva London North são os mais afetados:

<p align="center">
  <img src="https://github.com/user-attachments/assets/0fa2f04e-beb8-4635-b50b-c278fc31789f" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

Observando a distribuição dos incidentes ao longo do tempo, é possível perceber que a maioria dos incidentes ocorrem com os operadores Metroline e Arriva London North, enquanto que os com menor número de vítimas são Sullivan Bus & Coach e Uno Buses.

#### Gráfico 10 
**Qual o tipo de incidente mais comum com ciclistas?**

Vejamos a seguir:

<p align="center">
  <img src="https://github.com/user-attachments/assets/73408d2a-5482-40db-bd1c-33cb2bcca57e" alt="Accidents by gender" style="width: 650px; height: auto;">
</p>

Ao observar o gráfico acima, fica claro que a maioria dos acidentes envolvendo ciclistas são colisões. Ou seja, quando ocorre um acidente envolvendo um ciclista, há uma grande possibilidade de que esse acidente seja uma colisão.

## Conclusão
A análise dos dados dos acidentes no transporte público de Londres permitiu identificar que a maioria das vítimas são mulheres e que os acidentes mais frequentes são escorregões, tropeços e quedas. Além disso, foi possível observar que o ano de 2017 teve um número maior de incidentes em comparação com os anos anteriores, com picos em junho e julho. Esses resultados podem ser úteis para o desenvolvimento de medidas preventivas mais eficazes para garantir a segurança dos usuários do transporte público.
