library(tidyverse)
library(ggplot2)
library(ISLR)

#Search terms from 9/1/2016-11/1/2016


election2016 <- read.csv(file = 'https://raw.githubusercontent.com/gitcnk/Data/master/election2016.csv')


# Let's create a smaller dataset.
election_small <- election2016 %>%
  select(state, winner, vote_margin, pct_margin)

election_small$winner_binary <- ifelse(election_small$winner == "Trump", 1, 0)

election_small <- merge(election_small, TrumpSearch, by="state")
election_small <- merge(election_small, ClintonSearch, by="state")
election_small <- merge(election_small, wikileakssearch, by="state")
election_small <- merge(election_small, BillClinton, by="state")
election_small <- merge(election_small, FacebookSearch, by="state")

plot(election_small$wikileaks, election_small$winner_binary)
plot(election_small$ClintonSearch, election_small$winner_binary)
plot(election_small$TrumpSearch, election_small$winner_binary)
plot(election_small$BillClinton, election_small$winner_binary)
plot(election_small$facebook, election_small$winner_binary)
