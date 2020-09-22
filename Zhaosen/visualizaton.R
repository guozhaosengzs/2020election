library(tidyverse)

pa_house <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/pa_house.csv')
pa_potus <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/pa_potus.csv')

az_house <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/az_house.csv')
az_potus <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/az_potus.csv')

names(pa_house)[names(pa_house)=="X1"] <- "Year"
pa_h_2008 <- pa_house %>% filter(Year == 2002 | Year == 2006)
pa_h_2012 <- pa_house %>% filter(Year == 2006 | Year == 2010)
pa_h_2016 <- pa_house %>% filter(Year == 2010 | Year == 2014)
pa_h_2020 <- pa_house %>% filter(Year == 2014 | Year == 2018)

names(pa_potus)[names(pa_potus)=="X1"] <- "Year"
pa_p_2008 <- pa_potus %>% filter(Year == 2004 | Year == 2008)
pa_p_2012 <- pa_potus %>% filter(Year == 2008 | Year == 2012)
pa_p_2016 <- pa_potus %>% filter(Year == 2012 | Year == 2016)

names(az_house)[names(az_house)=="X1"] <- "Year"
names(az_potus)[names(az_potus)=="X1"] <- "Year"


pa <- ggplot() +
  geom_line(data = pa_h_2008, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 1.5, linetype = "solid") +
  geom_line(data = pa_h_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 1.5 , linetype = "longdash") +
  geom_line(data = pa_h_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 1.5, linetype = "dotdash") +
  geom_line(data = pa_h_2020, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 1.5, linetype = "dotted") +
  geom_point(data = pa_house, mapping = aes(x = factor(Year), y = RD_vote_r, shape="House Election"), size = 5) +
  
  geom_line(data = pa_p_2008, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 2, linetype = "solid") +
  geom_line(data = pa_p_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 2, linetype = "longdash") +
  geom_line(data = pa_p_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 2, linetype = "dotdash") +
  geom_line(mapping = aes(x = factor(c(2016, 2020)), y = c(1.0151351, 0.85), group=1), color = "blue", size = 2, linetype = "dotted") +
  geom_point(data = pa_potus, mapping = aes(x = factor(Year), y = RD_vote_r, shape = "Presidential Election"), size = 5) +
  
  
  geom_hline(yintercept=1)+
  
  scale_shape_manual("", 
                     breaks = c("House Election", "Presidential Election"),
                     values = c(18, 19)) +

  xlab('Year of the election') +
  ylab('Republicans to Democrat Votes Ratio')
  
pa

