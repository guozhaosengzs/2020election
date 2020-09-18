library(tidyverse)
library(ggplot2)
library(ISLR)

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

pairs(data=election_combined, margin_revised ~ Trump + Clinton + CNN + WikiLeaks + Make.America.Great.Again + Benghazi + Fox.News +
        Facebook + Instagram + Twitter + fake.news + black.lives.matter + antifa + healthcare + immigration + racism)

election_predict <- lm(margin_revised ~ Trump + CNN + Benghazi + Fox.News +
                         Facebook + Instagram,
                       data=election_combined)

summary(election_predict)
