library(tidyverse)
library(ggplot2)
library(ISLR)
library(rpart)
library(rpart.plot)

output <- read.csv("~/GitHub/2020election/Zhaosen/data/output.csv")
state_searches2020 <- read.csv("~/GitHub/2020election/matt/state_searches2020.csv")

state_searches2020$geoName <- state.abb[match(state_searches2020$geoName, state.name)]
st <- na.omit(state_searches2020)

pcmodel <- prcomp(st[,-1], center = T, scale = T )

PCscores <- predict(pcmodel)
PCscores <- data.frame(PCscores)
PCscores <- PCscores %>% select(names(PCscores)[1:2])
PCscores$state <- st$geoName

output_whole <- merge(output, st, by.x="State", by.y="geoName")
output_whole <- merge(output_whole, PCscores, by.x="State", by.y="state")

safe_states <- list('CA', 'CT', 'DE', 'HI', 'IL', 'MD', 'MA', 'NJ', 'NY', 'RI', 'VT', 'WA', 'AL', 'AK', 'ID', 'KS', 'MT', 'ND', 'SD', 'TN', 'WY')
safe_states <- do.call(rbind.data.frame, safe_states)
names(safe_states)[1] <- 'state'
train_set <- output_whole[output_whole$State %in% safe_states$state,]
lm <- lm(data=train_set[,!(names(train_set) %in% c("State"))], formula =  Pred_Ratio_2020 ~ PC1 + PC2)
summary(lm)

output_whole$Pred_Ratio_2020_2 <- predict(lm, output_whole)
output_output <- output_whole[,(names(output_whole) %in% c("State", "Pred_Ratio_2020", "Pred_Ratio_2020_2"))]
output_output$agree <- (output_output$Pred_Ratio_2020 >= 1 & output_output$Pred_Ratio_2020_2 >= 1) | 
  (output_output$Pred_Ratio_2020 < 1 & output_output$Pred_Ratio_2020_2 < 1)
output_output$avg_ratio <- output_output$Pred_Ratio_2020 * .6 + output_output$Pred_Ratio_2020_2 * .4
output_output$reelection <- ifelse(output_output$avg_ratio > 1, TRUE, FALSE)

write.csv(output_output, "output2.csv")

