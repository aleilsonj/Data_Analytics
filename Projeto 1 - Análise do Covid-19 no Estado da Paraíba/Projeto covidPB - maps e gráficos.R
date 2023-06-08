# Projeto análise de dados: Covid no Estado da Paraíba

# Carregando arquivo de dados
obts <- read.csv2("C:/Users/aleil/Documents/proj_covpb/acumulado PB.csv",
                  sep = ",")

# Carregando pacotes
library(geobr)
library(sf)
library(magrittr)
library(dplyr)
library(ggplot2)
library(fields)
library(tidyr)
# dataset do terriório da PB
municipios = read_municipality(code_muni = "PB", year =  2018)

ggplot() +
  geom_sf(data = municipios, fill = "#2D3E50",
          color = "#FEBF57",
          size =.15, show.legend = F)

# criando dataset: join do dataset -> municípios e obts
juntos <- full_join(municipios, obts, by = "name_muni")

# substituindo valores NA por 0
juntos2 <- replace(x = juntos, list = is.na(juntos), values = 0)

### Gr?fico Para?ba obitos

# Plot por intervalos - fun??o cut
juntos$obitosCovid <- cut(juntos$Obtos,breaks=c(-Inf, 0, 15, 50, 100, Inf),
                          labels = c("0", "1 a 15", "16 a 50", "51 a 100", "Mais de 100"))


ggplot(juntos) +
  geom_sf(aes(fill = obitosCovid )) +
  scale_fill_manual(values = c("#00FF00",
                               "#AAFF00", "#FFAA00", "tomato", "red")) +
  labs( title = "Covid-19 no Estado da Para?ba",
        subtitle = "Óbitos por Covid-19 na PB",
        caption = "Elaboração própria com base nos dados
          da Secretaria de Saúde do Estado",
        x = NULL, y = NULL) + 
  theme_void() +
  theme(legend.position = c(.85, 0.15), legend.key.size = unit(3,"mm")) 



## Plot para casos de covid PB
# 1. criando intervalos 
juntos$CasosCovid <- cut(juntos$Casos,breaks=c(0,100,600,1000,Inf),
                         labels = c("1 a 100", "101 a 600",
                                    "601 a 1000", "Mais de 1000"))

# 1.1. plot de casos no PB
ggplot(juntos) +
  geom_sf(aes(fill = CasosCovid)) +
  scale_fill_manual(values = c("#00FF00",
                               "#AAFF00", "#FFAA00", "#FF0000")) + 
  labs( title = "Covid-19 no Estado da Paraíba",
        subtitle = "Números de casos confirmados", fill = "Casos confirmados", 
        caption = "Elaboração própria com base nos dados
          da Secretaria de Saúde do Estado", x = NULL, y = NULL) + 
  theme_void() +
  theme(legend.position = c(.85, 0.15), legend.key.size = unit(3,"mm"))

# 2. intervalo por obtos
juntos$obitosCovid <- cut(juntos$Obtos,breaks=c(-Inf, 0, 15, 50, 100, Inf),
                          labels = c("0", "1 a 15", "16 a 50", "51 a 100", "Mais de 100"))

# 3. plot de obtos por covid na PB
ggplot(juntos) +
  geom_sf(aes(fill = obitosCovid )) +
  scale_fill_manual(values = c("#00FF00", "#AAFF00", "#FFAA00",
                               "tomato", "red")) +
  labs( title = "Covid-19 no Estado da Paraíba",
        subtitle = "Óbitos por Covid-19 na PB", fill = "Óbitos Confirmados",
        caption = "Elaboração própria com base nos dados da Secretária de saúde do Estado",
        x = NULL, y = NULL) + 
  theme_void() +
  theme(legend.position = c(.85, 0.15), legend.key.size = unit(3,"mm"))

# Gráficos
# Criando base de dados com os Top 10 de maiores casos
top10casos <-juntos %>%
  top_n(Casos, n=15)

# Numero total de casos
sum(juntos$Casos)

# Circular Packing
install.packages("packcircles")
library(packcircles)

# Criando dados
bolhacov <- data.frame(
  categoria=top10casos$name_muni,
  medida=top10casos$Casos
)

# Create packing - calculo da area
packing <- circleProgressiveLayout(bolhacov$medida, sizetype='area')

# ajustando a separa??o das bolhas
bolhacov2 <- cbind(bolhacov, packing)

#centraliza??o das bolhas e c?lculo ao redor do poligono
dat.gg <- circleLayoutVertices(packing, npoints=50)

## Plot
ggplot() + 
  geom_polygon(data = dat.gg, aes(x, y, group = id,
                                  fill=as.factor(id)),
               colour = "White", alpha = 0.6) +
  geom_text(data = bolhacov2, aes(x, y, size=medida, label = categoria, colour = "black"), colour = "black") +
  scale_size_continuous(range = c(3,8)) +
  scale_fill_manual(values = c("#00FF00", "#11EE00", "#22DD00", "#33CC00",
                               "#44BB00", "#55AA00", "#669900", "#778800",
                               "#887700","#996600", "#AA5500", "#BB4400", 
                               "#CC3200", "#DD2100", "#EE1000", "#FF0000")) +
  labs( title = "Covid-19 no Estado da Paraíba",
        subtitle = "Casos Acumulados de Covid-19 na Paraíba",
        caption = "Elaboração própria com Base nos Dados da Secretária Estadual de Saúde"
  ) +
  theme_void() + 
  theme(legend.position="none") +
  coord_equal() 

### LolliPop
Pop <-ggplot(top10casos, aes(x=name_muni, y=Casos)) +
  geom_segment( aes(x=name_muni, xend=name_muni, y=0, yend=Casos), color="skyblue") +
  geom_point( color="yellow", size=4, alpha=0.6) +
  theme_light() +
  coord_flip() +
  theme(
    panel.grid.major.y = element_blank(),
    panel.border = element_blank(),
    axis.ticks.y = element_blank()
  ) +
  xlab("Municípios") +
  ylab("Casos Acumulados") +
  ggtitle("Covid-19 - Casos Acumulados Paraíba")
  #theme_ft_rc()
  #theme(plot.title = element_text(hjust = 0.5))

library(plotly)
ggplotly(Pop)
