# Carregando diretório de trabalho
setwd("C:/Users/ALEILSON/Documents/Disciplinas/Ciencias de Dados/Projeto_1/Dados")
getwd()

library(readr)
library(dplyr)
library(ggplot2)
library(plotly)
library(hrbrthemes)
library(scales)
library(lubridate)
library(zoo)

# carregando df
seg_def <- read.csv("seg_defeso.csv") %>%
  select(-c("CÓDIGO.MUNICÍPIO.SIAFI", "CPF.FAVORECIDO",
            "NIS.FAVORECIDO","NOME.FAVORECIDO", "RGP.FAVORECIDO"))
names(seg_def) <- c("referência", "uf", "muni", "valor_parcela")

desastre_mari <- read_csv("desatre_mari.csv")
str(desastre_mari)
class(desastre_mari)
# 1 - Visualizar a evolução mensal do total recebido do 
# Seguro Defeso nos municípios afetados pelo
# desastre;

evomes <- desastre_mari %>%
  filter(afetado == 1, ano >= 2015) %>% 
  select("ano", "mes", "valor_parcela") %>%
  mutate(mes=as.factor(mes),
         ano= as.factor(ano),
         valor_parcela= as.double(valor_parcela)) %>%
  group_by(ano, mes) %>%
  summarise(total = sum(valor_parcela))
  
str(evomes)

# plot visualização mensal do total recebido do 
# seguro defeso nos municípios afetados
g1 <- evomes %>% ggplot(aes(x= mes, y= total/1000000, fill = ano)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_text(aes(label = c(format(round(total/1000000, 2), nsmall = 2))),
                position = position_dodge(width=1), vjust = -0.1) +
  labs(x="Meses", y="Total (milhões)",
       title="Evolução mensal do Seguro Defeso ",
       subtitle="Período 2015-2016 municípios afetados",
       caption="Elaboração própria") + 
  theme_ipsum(grid="Y") 



# 2 - Comparar com a evolução mensal dos demais municípios da Bacia do Rio Doce
evo_rd <- desastre_mari %>%
  filter(rio_doce == 1, afetado == 0, ano >= 2015) %>% 
  select("ano", "mes", "valor_parcela") %>%
  mutate(mes=as.factor(mes),
         ano= as.factor(ano),
         valor_parcela= as.double(valor_parcela)) %>%
  group_by(ano, mes) %>%
  summarise(total = sum(valor_parcela))

str(evomes)

# plot visualização mensal do total recebido do 
# seguro defeso nos municípios da bacia do rio doce
g2 <- evo_rd %>% ggplot(aes(x= mes, y= total/1000000, fill = ano)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_text(aes(label = c(format(round(total/1000000, 2), nsmall = 2))),
            position = position_dodge(width=1), vjust = -0.1) +
  labs(x="Meses", y="Total (milhões)",
       title="Evolução mensal do Seguro Defeso ",
       subtitle="Período 2015-2016 municípios da Bacía do Rio Doce",
       caption="Elaboração própria") + 
  theme_ipsum(grid="Y")

g2

# 3 - Verificar se houve aumento no número de municípios e de
# indivíduos que passaram a receber Seguro Defeso nos 12 meses seguintes,
# comparativamente aos 12 meses anteriores;
# df sobre o Seguro Defeso
seg_def <- read.csv("seg_defeso.csv") %>%
  select(-c("CÓDIGO.MUNICÍPIO.SIAFI",
            "NIS.FAVORECIDO","NOME.FAVORECIDO", "RGP.FAVORECIDO"))
names(seg_def) <- c("referência", "uf", "muni", "cpf", "valor_parcela")

str(seg_def)


## Subset dos dados para o ano de 2015
muni2 <- desastre_mari %>%
  select(muni, ano) %>% 
  filter(ano == 2015)

# numero de municípios e individuas que recebiam o segdef antes do desastre
num_municipios_anterior <- length(unique(muni2$muni))
num_individuos_anterior <- nrow(muni2)

## Subset dos dados para o ano de 2015
muni3 <- desastre_mari %>%
  select(muni, ano) %>% 
  filter(ano == 2016) 

# numero de municípios e individuas que recebiam o segdef depois do desastre
num_municipios_seguinte <- length(unique(muni3$muni))
num_individuos_seguinte <- nrow(muni3)

# condicional para verificar se houve aumento no numero de municipios
# que recebiam o seguro def
if (num_municipios_seguinte > num_municipios_anterior) {
  print("Houve aumento no número de municípios que receberam Seguro Defeso nos 12 meses seguintes.")
} else {
  print("Não houve aumento no número de municípios que receberam Seguro Defeso nos 12 meses seguintes.")
}

# condicinal para verificar se houve aumento no numero de individuos
# que recebiam o seguro def
if (num_individuos_seguinte > num_individuos_anterior) {
  print("Houve aumento no número de indivíduos que receberam Seguro Defeso nos 12 meses seguintes.")
} else {
  print("Não houve aumento no número de indivíduos que receberam Seguro Defeso nos 12 meses seguintes.")
}

# Apresentar, para os 12 meses seguintes ao desastre,
# os 10 municípios da Bacia do Rio Doce que
# mais receberam o auxílio do Seguro Defeso em termos per capita.

dp_desa <- desastre_mari %>% 
  filter(desastre == "Após o Desastre") %>%
  select("muni","valor_parcela", "pop" ) %>% 
  group_by(muni) %>% 
  summarise (Total = sum(valor_parcela)) 

# Rank: 10 municípios com maiores valores do seguro defeso
muni_rank <- dp_desa %>% 
   arrange(desc(Total)) %>% 
   head(10)
 
# Formatação dos valores
muni_rank$Total <- paste0("R$ ",format(muni_rank$Total, digits = 2,
                                       nsmall = 2, big.mark = ".", 
                                       decimal.mark = ","))


# carregando dados de popilção do muni para calcular em termo per capita
pop_munic <- readRDS("pop_municipios.rda") %>% 
  select("muni", "pop") 

# Join do dois dataset 
munijoin <- left_join(dp_desa, pop_munic)

# top 10 per capita
muni_rankp <- munijoin %>% 
   select("muni","Total", "pop" ) %>% 
   group_by(muni) %>% 
   summarise ("Total Percapita" = Total/pop ) %>% 
   arrange(desc(`Total Percapita`)) %>% 
   head(10)

#Formatação da variavel
muni_rankp$`Total Percapita` <- paste0("R$ ",
                                       format(muni_rankp$`Total Percapita`,
                                                    digits = 2, nsmall = 2,
                                                    big.mark = ".", decimal.mark = ","))

# Calcular valore media para antes e depois do desastre
media_dp <- mean(dp_desa$Total, na.rm = FALSE)
media_dp  <- paste0("R$ ", format(media_dp, digits = 2, nsmall = 2,
                                     big.mark = ".", decimal.mark = ",")) #Depois do desastre


seg_per <- munijoin %>% 
  select("muni","Total", "pop" ) %>% 
  group_by(muni) %>% 
  summarise ("Total Percapita" = Total/pop ) %>% 
  arrange(desc(`Total Percapita`))

mediaper_dp <- mean(seg_per$`Total Percapita`, na.rm = FALSE)

mediaper_dp  <- paste0("R$ ", format(mediaper_dp, digits = 2, nsmall = 2,
                                              big.mark = ".", decimal.mark = ",")) # Depois do desastre


# antes do desastre
at_desa <- desastre_mari %>% 
  filter(desastre == "Antes do Desastre") %>%
  select("muni","valor_parcela", "pop" ) %>% 
  group_by(muni) %>% 
  summarise (Total = sum(valor_parcela))

media_at <- mean(at_desa$Total, na.rm = FALSE)
media_at  <- paste0("R$ ", format(media_at, digits = 2, nsmall = 2,
                                     big.mark = ".", decimal.mark = ","))
#antes do deastre rank
rankat <- at_desa %>% 
  arrange(desc(Total)) %>% 
  head(10)
rankat$Total <- paste0("R$ ",format(rankat$Total, digits = 2, nsmall = 2,
                                              big.mark = ".", decimal.mark = ","))
# Per capita
munijoin2 <- left_join(at_desa, pop_munic)

seg_per2 <- munijoin2 %>% 
  select("muni","Total", "pop" ) %>% 
  group_by(muni) %>% 
  summarise ("Total Percapita" = Total/pop ) %>% 
  arrange(desc(`Total Percapita`))

mediaper_at <- mean(seg_per2$`Total Percapita`, na.rm = FALSE)
mediaper_at  <- paste0("R$ ", format(mediaper_at, digits = 2, nsmall = 2,
                                     big.mark = ".", decimal.mark = ","))

# rankat_per
rankat_per <- seg_per2 %>% 
  arrange(desc(`Total Percapita`)) %>% 
  head(10)
rankat_per$`Total Percapita` <- paste0("R$ ", format(rankat_per$`Total Percapita`, digits = 2, nsmall = 2,
                                     big.mark = ".", decimal.mark = ","))

## Parte serie temp

seg_def$referência = as.character(seg_def$referência)

tab_temp <- seg_def %>% 
  dplyr::mutate(date = lubridate::parse_date_time(referência,"%Y%0m"))

tab_temp$ano_mes <- as.yearmon(tab_temp$date, format = "%Y-%m")

#plot
tab1 <- tab_temp %>% 
  select(ano_mes, valor_parcela) %>%
  group_by(ano_mes) %>% 
  summarise(Total_mes = sum(valor_parcela))

g3 <- ggplot(tab1, aes(x=ano_mes, y=Total_mes)) + 
  geom_line() +
  ggtitle("Evolução Seguro Defeso")+
  xlab("Ano-Mês")+
  ylab("Valores")+
  theme_ft_rc()

