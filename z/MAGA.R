# Trial Run on Election Data#
library(tidyverse)
library(arsenal)


senate = read_csv('/Users/gzs/Desktop/MATH 503/2020election/z/senate_state.csv')
house = read_csv('/Users/gzs/Desktop/MATH 503/2020election/z/house_district.csv')
president = read_csv('/Users/gzs/Desktop/MATH 503/2020election/z/president_state.csv')


#### "Swing" Analysis #####

# House Election data
house_10_14 = house %>% 
  filter(year == "2010" | year == "2014") %>% 
  select(year, state_po, district, party, candidatevotes, totalvotes)

house_10_14$ID = paste(house_10_14$year, house_10_14$state_po, house_10_14$district, sep = '_')
house_10_14 = house_10_14[order(house_10_14[,'ID'],-house_10_14[,'candidatevotes']),]
house_10_14 = house_10_14[!duplicated(house_10_14$ID),]

house_10_14$ID = paste(house_10_14$state_po, house_10_14$district, sep = '_')
house_10_14 = house_10_14[order(house_10_14[,'ID']),]


house_2010 = subset(house_10_14, house_10_14$year == 2010)
house_2014 = subset(house_10_14, house_10_14$year == 2014)
house_compare = inner_join(house_2010, house_2014, by = "ID")
house_compare$changed = if_else(house_compare$party.x == house_compare$party.y, 0, 1)
house_compare = house_compare %>% mutate(changed = ifelse(changed == 0, 0, state_po.y))


district_state = data.frame(table(house_2014$state_po))
names(district_state)[1] = "state"
names(district_state)[2] = "total"

changed_ds = data.frame(table(house_compare$changed))
names(changed_ds)[1] = "state"
names(changed_ds)[2] = "switched"
changed_ds = changed_ds[changed_ds$state != "0",]

house_changes_fin = left_join(district_state, changed_ds, by = "state")
house_changes_fin = house_changes_fin %>% mutate_all(~replace(., is.na(.), 0))
house_changes_fin$ratio = house_changes_fin$switched / house_changes_fin$total
sum(house_changes_fin$total)
# Senate Election data
senate_04_08 = senate %>% 
  filter(year == 2004 | year == 2006 | year == 2008) %>% 
  select(year, state_po, party, candidatevotes, totalvotes)

senate_04_08$ID = paste(senate_04_08$year, senate_04_08$state_po, sep = '_')
senate_04_08 = senate_04_08[order(senate_04_08[,'ID'],-senate_04_08[,'candidatevotes']),]
senate_04_08 = senate_04_08[!duplicated(senate_04_08$ID),]

seats_04_08 = rename(count(senate_04_08, state_po, party), seats = n)

senate_10_14 = senate %>% 
  filter(year == 2010 | year == 2012 | year == 2014) %>% 
  select(year, state_po, party, candidatevotes, totalvotes)

senate_10_14$ID = paste(senate_10_14$year, senate_10_14$state_po, sep = '_')
senate_10_14 = senate_10_14[order(senate_10_14[,'ID'],-senate_10_14[,'candidatevotes']),]
senate_10_14 = senate_10_14[!duplicated(senate_10_14$ID),]

seats_10_14 = rename(count(senate_10_14, state_po, party), seats = n)

# Resolving an NA value due to write-in candidate winning
seats_10_14 = seats_10_14[-2,]
seats_10_14[1,3] = 2           

