# Trial Run on Election Data#
library(tidyverse)
library(arsenal)


senate = read_csv('/Users/gzs/Desktop/MATH 503/2020election/z/senate_state.csv')
house = read_csv('/Users/gzs/Desktop/MATH 503/2020election/z/house_district.csv')
president = read_csv('/Users/gzs/Desktop/MATH 503/2020election/z/president_state.csv')


#### "Swing" Analysis #####

# Clean Election data
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

distinct_state = data.frame(table(house_2014$state_po))
names(distinct_state)[1] = "state"
names(distinct_state)[2] = "total"
distinct_state$switched = 0



