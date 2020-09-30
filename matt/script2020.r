library(tidyverse)
library(ggplot2)
library(ISLR)
library(rpart)
library(rpart.plot)

#Search terms from 9/1/2016-11/1/2016


election2020 <- read.csv(file = 'https://raw.githubusercontent.com/gracejanes/Test1/master/presidential_poll_averages_2020.csv')
state_searches <- read.csv("~/GitHub/2020election/matt/state_searches2020.csv")
names(state_searches)[1] <- 'state'
election2020 <- election2020 %>% filter(modeldate == '9/29/2020')
biden2020 <- election2020 %>% filter(candidate_name == 'Joseph R. Biden Jr.')
trump2020 <- election2020 %>% filter(candidate_name == 'Donald Trump')

election2020compare <- merge(biden2020, trump2020, by='state')
names(election2020compare)[6] <- 'biden_pct'
names(election2020compare)[11] <- 'trump_pct'

election2020compare$poll_margin <- election2020compare$trump_pct - election2020compare$biden_pct

election2020combined <- merge(election2020compare, state_searches, by='state')

election2020combined <- election2020combined %>% select(names(election2020combined)[12:39])


model <- rpart(poll_margin ~ . , data=election2020combined)
rpart.plot(model)

election2020_revised <- election2020combined[,!(names(election2020combined) %in% c("Trump", "Fox.News", "social.distancing"))]
model_t <- rpart(poll_margin ~ . , data=election2020_revised)
rpart.plot(model_t)

election2020_revised <- election2020_revised[,!(names(election2020_revised) %in% c("NASDAQ", "Dow.Jones", "immigration"))]
model_t <- rpart(poll_margin ~ . , data=election2020_revised)
rpart.plot(model_t)

model_f <- lm(poll_margin ~ Trump + Fox.News + social.distancing + NASDAQ + Dow.Jones + immigration +
                racism + Instagram + Russia, data=election2020combined)
summary(model_f)
plot(model_f)

