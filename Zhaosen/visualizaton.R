library(tidyverse)

pa_house <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/pa_house.csv')
pa_potus <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/pa_potus.csv')

az_house <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/az_house.csv')
az_potus <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/az_potus.csv')

names(pa_house)[names(pa_house)=="X1"] <- "Year"
pa_e_2012 <- pa_house %>% filter(Year == 2006 | Year == 2010)
pa_e_2016 <- pa_house %>% filter(Year == 2010 | Year == 2014)
pa_e_2020 <- pa_house %>% filter(Year == 2014 | Year == 2018)

names(pa_potus)[names(pa_potus)=="X1"] <- "Year"
names(az_house)[names(az_house)=="X1"] <- "Year"
names(az_potus)[names(az_potus)=="X1"] <- "Year"


pa <- ggplot() +
  geom_line(data = pa_e_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1)) +
  geom_line(data = pa_e_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1)) +
  geom_line(data = pa_e_2020, mapping = aes(x = factor(Year), y = RD_vote_r, group=1)) +
  geom_point(data = pa_house, mapping = aes(x = factor(Year), y = RD_vote_r, size = 1, shape=15)) +
  geom_point(data = pa_potus, mapping = aes(x = factor(Year), y = RD_vote_r, size = 1)) +
  scale_shape_identity()
  
  xlab('Year of the election') +
  ylab('Republicans to Democrat Votes Ratio')
  
pa

