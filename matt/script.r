library(tidyverse)
library(ggplot2)
library(ISLR)
library(rpart)
library(rpart.plot)

#Search terms from 9/1/2016-11/1/2016


election2016 <- read.csv(file = 'https://raw.githubusercontent.com/gitcnk/Data/master/election2016.csv')
state_searches <- read.csv("~/GitHub/2020election/matt/state_searches.csv")
names(state_searches)[1] <- 'state'


# Let's create a smaller dataset.
election_small <- election2016 %>%
  select(state, winner, vote_margin, pct_margin)

election_small$winner_binary <- ifelse(election_small$winner == "Trump", 1, 0)
election_small$margin_revised <- ifelse(election_small$winner == "Clinton", -1 * election_small$pct_margin, election_small$pct_margin)

election_combined <- merge(election_small, state_searches, by='state')

for (name in names(election_combined)[7:30]) {
  print(cor(election_combined$margin_revised, election_combined[name]))
}



election_search <- election_combined %>% select(names(election_combined)[6:30])
model <- rpart(margin_revised ~ . , data=election_search)
rpart.plot(model)

election_search_revised <- election_search[,!(names(election_search) %in% c("Trump", "Fox.News", "Facebook", "Russia"))]
model_t <- rpart(margin_revised ~ . , data=election_search_revised)
rpart.plot(model_t)

model_f <- lm(margin_revised ~ China + Crimea + CNN + Fox.News + Russia + Trump + Facebook, data=election_search)
summary(model_f)
plot(model_f)
