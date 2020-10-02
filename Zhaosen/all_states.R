library(tidyverse)

data <- read.csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/trend_compare.csv', row.names = 1)
data$Class<- as.factor(data$Class)
data$State <- as.factor(data$State)

train_df <- data %>% subset(Class == 'T') 
pred_df <- data %>%  subset(Class == 'P')

model1 = lm(data = train_df, President ~ )