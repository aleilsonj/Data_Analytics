###=============================================###
###                                             ###
###                   Projeto                   ### 
###               Desastre Mariana              ###
###                                             ###
###=============================================###


# Carregando o diretório de trabalho
setwd("C:/Users/ALEILSON/Documents/Disciplinas/Ciências de Dados/Projeto_1/Dados")
getwd()

# Instalando pacotes para o projeto
library(tidyverse)
library(stringr)

# Parte 1 - carregando dados:

# df sobre os municípios do Rio Doce
muni_rd <-read.csv2("municipios_rio_doce.csv", sep = ",") %>%
           select(-c("micro", "meso", "regiao","uf_cod","cod_ibge"))

names(muni_rd) <- c("muni", "rio_doce", "uf", "afetado")

muni_r_d
class(muni_r_d)
str(muni_r_d)
typeof(muni_r_d)

# df sobre o tamanho populacional do entrono do RD
pop_munic <- readRDS("pop_municipios.rda") %>% 
              select("muni", "pop")
pop_munic

# df sobre o Seguro Defeso
seg_def <- read.csv("seg_defeso.csv") %>%
  select(-c("CÓDIGO.MUNICÍPIO.SIAFI", "CPF.FAVORECIDO",
            "NIS.FAVORECIDO","NOME.FAVORECIDO", "RGP.FAVORECIDO"))
names(seg_def) <- c("referência", "uf", "muni", "valor_parcela")

str(seg_def)

# Parte 2 - Transformação do dados
# novas variáveis para o seg_def
## variável para antes e dps do desastre
seg_def <- mutate(seg_def,
                  desastre = case_when(seg_def$referência <= 201511 ~ "Antes do Desastre",
                                       seg_def$referência > 201511 ~ "Após o Desastre"))

## separando o período em Ano e Mês
seg_def <- mutate(seg_def,
                  ano = stringr::str_sub(seg_def$referência, 1, 4),
                  mes = stringr::str_sub(seg_def$referência, 5, 6))

## novo df com valore de parcela sumarizado por mês e município
seg_def2 <- seg_def %>% 
  select("muni", "ano","mes", "valor_parcela", "desastre", "uf") %>% 
  group_by(muni, mes, ano, desastre, uf) %>% 
  summarise(valor_parcela = sum(valor_parcela))

seg_def2 = tbl_df(seg_def2)

# join seg_def2 e muni_rd
muni2 <- seg_def2 %>% left_join(muni_rd, by = c("muni" = "muni", "uf" = "uf"))


# join muni2 e pop_munic
muni2 <- muni2 %>% left_join(pop_munic,
          by = c("muni" = "muni"))

# removendo valores NA de muni 2: aqui eu decidi substituir os valores dos vetores 
# rio_dece e afetado por zero.  
muni2 <- mutate_at(muni2, c("rio_doce", "afetado"), ~replace(., is.na(.), 0))

# Parte 3 - Salvando novo df
library(readr)
write_csv(muni2,'desatre_mari.csv')




  
  