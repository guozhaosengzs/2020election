library(tidyverse)

#### PA House vs Presidential ####
pa_house <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/pa_house.csv')
pa_potus <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/pa_potus.csv')

names(pa_house)[names(pa_house)=="X1"] <- "Year"
pa_h_2008 <- pa_house %>% filter(Year == 2002 | Year == 2006)
pa_h_2012 <- pa_house %>% filter(Year == 2006 | Year == 2010)
pa_h_2016 <- pa_house %>% filter(Year == 2010 | Year == 2014)
pa_h_2020 <- pa_house %>% filter(Year == 2014 | Year == 2018)

names(pa_potus)[names(pa_potus)=="X1"] <- "Year"
pa_p_2008 <- pa_potus %>% filter(Year == 2004 | Year == 2008)
pa_p_2012 <- pa_potus %>% filter(Year == 2008 | Year == 2012)
pa_p_2016 <- pa_potus %>% filter(Year == 2012 | Year == 2016)




pa_h_graph <- ggplot() +
  geom_line(data = pa_h_2008, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 1.5, linetype = "solid") +
  geom_line(data = pa_h_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 1.5 , linetype = "longdash") +
  geom_line(data = pa_h_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 1.5, linetype = "dotdash") +
  geom_line(data = pa_h_2020, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 1.5, linetype = "dotted") +
  geom_point(data = pa_house, mapping = aes(x = factor(Year), y = RD_vote_r, shape="House Election"), size = 8) +
  
  geom_line(data = pa_p_2008, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 2, linetype = "solid") +
  geom_line(data = pa_p_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 2, linetype = "longdash") +
  geom_line(data = pa_p_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 2, linetype = "dotdash") +
  geom_segment(mapping=aes(x = factor(2016), y = c(1.0151351), xend=factor(2020), yend=0.85), arrow = arrow(length = unit(0.7, "cm"), type="closed"), size=1.5, color="blue", linetype = "dotted") +  geom_point(data = pa_potus, mapping = aes(x = factor(Year), y = RD_vote_r, shape = "Presidential Election"), size = 8) +
  
  
  geom_hline(yintercept=1)+
  
  scale_shape_manual("", 
                     breaks = c("House Election", "Presidential Election"),
                     values = c(18, 19)) +
  labs(title = "Pennsylvanian Total Votes for the House and the Presidency: \n
       Presidential Election Results Compared to Changes in the House 6 to 2 Years Prior", x = 'Year of the Election', 
         y = 'Republicans to Democrat Votes Ratio') +
  theme(plot.title = element_text(hjust = 0.5))

pa_h_graph







#### AZ House vs Presidential ####
az_house <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/az_house.csv')
az_potus <- read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/az_potus.csv')
names(az_house)[names(az_house)=="X1"] <- "Year"
names(az_potus)[names(az_potus)=="X1"] <- "Year"

names(az_house)[names(az_house)=="X1"] <- "Year"
az_h_2008 <- az_house %>% filter(Year == 2002 | Year == 2006)
az_h_2012 <- az_house %>% filter(Year == 2006 | Year == 2010)
az_h_2016 <- az_house %>% filter(Year == 2010 | Year == 2014)
az_h_2020 <- az_house %>% filter(Year == 2014 | Year == 2018)

names(az_potus)[names(az_potus)=="X1"] <- "Year"
az_p_2008 <- az_potus %>% filter(Year == 2004 | Year == 2008)
az_p_2012 <- az_potus %>% filter(Year == 2008 | Year == 2012)
az_p_2016 <- az_potus %>% filter(Year == 2012 | Year == 2016)

az_h_graph <- ggplot() +
  geom_line(data = az_h_2008, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 1.5, linetype = "solid") +
  geom_line(data = az_h_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 1.5 , linetype = "longdash") +
  geom_line(data = az_h_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 1.5, linetype = "dotdash") +
  geom_line(data = az_h_2020, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 1.5, linetype = "dotted") +
  geom_point(data = az_house, mapping = aes(x = factor(Year), y = RD_vote_r, shape="House Election"), size = 8) +
  
  geom_line(data = az_p_2008, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 2, linetype = "solid") +
  geom_line(data = az_p_2012, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "red", size = 2, linetype = "longdash") +
  geom_line(data = az_p_2016, mapping = aes(x = factor(Year), y = RD_vote_r, group=1), color = "blue", size = 2, linetype = "dotdash") +
  geom_segment(mapping=aes(x = factor(2016), y = c(1.078532), xend=factor(2020), yend=0.90), arrow = arrow(length = unit(0.7, "cm"), type="closed"), size=1.5, color="blue", linetype = "dotted") +
  geom_point(data = az_potus, mapping = aes(x = factor(Year), y = RD_vote_r, shape = "Presidential Election"), size = 8) +
  
  
  geom_hline(yintercept=1)+
  
  scale_shape_manual("", 
                     breaks = c("House Election", "Presidential Election"),
                     values = c(18, 19)) +
  labs(title = "Arizona Total Votes for the House and the Presidency: \n
       Presidential Election Results Comazred to Changes in the House 6 to 2 Years Prior", x = 'Year of the Election', 
       y = 'Republicans to Democrat Votes Ratio') +
  theme(plot.title = element_text(hjust = 0.5))

az_h_graph
