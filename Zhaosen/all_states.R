library(tidyverse)

data <- read.csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/trend_compare.csv', row.names = 1)
data$Class<- as.factor(data$Class)
data$State <- as.factor(data$State)

train_df <- data %>% subset(Class == 'T') 
pred_df <- data %>%  subset(Class == 'P')

model1 <- lm(data = train_df, President ~ House)
summary(model1)
layout(matrix(c(1,3,2,4),2,2))
plot(model1)

model2 <- lm(data = train_df, President ~ House + State)
summary(model2)
plot(model2)

p_04_16 <- read.csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/potus_04_16.csv')
p_2016 <- p_04_16 %>% subset(Year == 2016) 
p_2016 <- p_2016 %>% subset(State != 'DC') 

pred_df$President <- predict(model2, pred_df)

temp <- full_join(pred_df, p_2016, by="State")
temp$Pred_Ratio_2020 <- paste(temp$President + temp$RD_vote_r)

output <- temp %>% select(State, Pred_Ratio_2020)
write.csv(output,'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/output.csv', row.names = FALSE)
