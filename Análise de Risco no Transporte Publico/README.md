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
Serão utilizadas ferramentas de visualização de dados, como o Matplotlib e Seaborn, para a criação de gráficos e visualizações que ajudem na compreensão dos resultados e na apresentação dos insights gerados.

### Implementação
O projeto será implementado utilizando a linguagem Python e a linguagem SQL, a fim de realizar as análises necessárias. Para isso, serão utilizadas as seguintes bibliotecas:

- Pandas: para manipulação de dados;
- Pandasql: para realizar consultas SQL em dataframes do Pandas;
- Matplotlib: para visualização de gráficos;
- Seaborn: para visualização de gráficos;

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

## Conclusão
A análise dos dados dos acidentes no transporte público de Londres permitiu identificar que a maioria das vítimas são mulheres e que os acidentes mais frequentes são escorregões, tropeços e quedas. Além disso, foi possível observar que o ano de 2017 teve um número maior de incidentes em comparação com os anos anteriores, com picos em junho e julho. Esses resultados podem ser úteis para o desenvolvimento de medidas preventivas mais eficazes para garantir a segurança dos usuários do transporte público.
