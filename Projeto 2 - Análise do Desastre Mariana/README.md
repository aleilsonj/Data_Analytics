# Análise dos Beneficiados do Seguro Defeso após o Desastre de Mariana (MG)
## Introdução
Em 5 de novembro de 2015, ocorreu a ruptura da barragem de rejeitos de Fundão em Mariana (MG), uma das maiores catástrofes ambientais do Brasil. A barragem abrigava cerca de 56,6 milhões de m3 de lama de rejeito de minérios, dos quais 43,7 milhões de m3 vazaram e atingiram o Rio Doce e seus afluentes, destruindo distritos inteiros e deixando milhares de moradores da região sem água e sem moradia. A pesca, uma das principais atividades dos municípios próximos ao Rio Doce, foi fortemente impactada pela lama, e até hoje, cerca de 4 anos após a tragédia, a pesca continua restrita ou proibida na Bacia do Rio Doce.
Como forma de amenizar a situação dos pescadores da Bacia do Rio Doce, foi liberado o recebimento do Seguro Defeso a partir de dezembro de 2015. O Seguro Defeso consiste em uma assistência financeira temporária no valor de um salário mínimo concedida aos pescadores profissionais artesanais que, durante o período de reprodução dos peixes, são obrigados a paralisar sua atividade.

Este projeto tem como objetivo analisar o padrão de recebimentos do Seguro Defeso nos municípios atingidos, comparativamente aos demais municípios da Bacia do Rio Doce.

## Dados
Os seguintes dados foram utilizados neste projeto:

- **seg_defeso.csv**: contém informações sobre os beneficiados do Seguro Defeso de novembro de 2014 a novembro de 2016.
- **municipios_rio_doce.csv**: contém informações sobre os municípios da Bacia do Rio Doce e os mais afetados pela lama.
- **pop_municipios.rda**: população dos municípios, baseada no CENSO 2010.

## Objetivos
Visualizar a evolução mensal do total recebido do Seguro Defeso nos municípios afetados pelo desastre;
Comparar com a evolução mensal dos demais municípios da Bacia do Rio Doce;
Verificar se houve aumento no número de municípios e de indivíduos que passaram a receber Seguro Defeso nos 12 meses seguintes, comparativamente aos 12 meses anteriores;
Apresentar, para os 12 meses seguintes ao desastre, os 10 municípios da Bacia do Rio Doce que mais receberam o auxílio do Seguro Defeso em termos per capita.

## Tecnologias utilizadas neste projeto:

- RStudio: ambiente de desenvolvimento integrado (IDE) para a linguagem R.
- R: linguagem de programação estatística utilizada para manipulação, análise e visualização de dados.
- ggplot2: pacote do R para criação de gráficos estatísticos.
- dplyr: pacote do R para manipulação de dados, incluindo filtragem, seleção, agrupamento e sumarização.
- RMarkdown: ferramenta do R para criação de documentos dinâmicos que integram código, gráficos e texto em um único arquivo.

## Referências:

Agência Nacional de Águas. (2016). Relatório de Situação dos Recursos Hídricos do Brasil 2016. Retrieved from http://www3.ana.gov.br/presentation/publicacoes/RSRH2016.pdf

Instituto Brasileiro de Geografia e Estatística. (2010). Censo Demográfico 2010. Retrieved from https://www.ibge.gov.br/estatisticas/sociais/populacao/9662-censo-demografico-2010.html?=&t=resultados

Ministério da Agricultura, Pecuária e Abastecimento. (2015). Seguro Defeso. Retrieved from http://www.agricultura.gov.br/assuntos/politica-agricola/seguro-defeso

Ministério do Meio Ambiente. (2016). Boletim da Bacia do Rio Doce - Edição 1. Retrieved from http://www.mma.gov.br/informma/item/13639-boletim-da-bacia-do-rio-doce-edi%C3%A7%C3%A3o-1.html

Secretaria de Estado de Meio Ambiente e Desenvolvimento Sustentável de Minas Gerais. (2016). Relatório de Impacto Ambiental - RIMA - Samarco Mineração S.A. Retrieved from http://www.meioambiente.mg.gov.br/images/stories/servicos_e_sistemas/gerenciamento_ambiental/AIA/RIMA_Samarco_Mineracao_S_A_-_Projeto_Germano_-_Distrito_de_Mariana_-_MG.pdf
