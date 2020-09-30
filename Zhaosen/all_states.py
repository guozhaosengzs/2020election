import pandas as pd
import numpy as np

def house(raw):
    years = [2002, 2006, 2010, 2014, 2018]
    states = raw.state_po.unique()
    state_df = []

    for st in states:
        st_df = pd.DataFrame(columns=['RD_vote_r', 'State'], index=years)
        st_df.index.name = 'Year'

        for yr in years:
            subset = raw.loc[(raw['year'] == yr) & (raw['state_po'] == st)]
            subset = subset[['state_po', 'party', 'candidatevotes']]
            print(subset)
            subset_vr = subset.groupby(['party'])[['candidatevotes']].agg('sum')
            print(subset_vr)

            party_list = list(subset_vr.index.values)

            if 'republican' in party_list and 'democrat' in party_list:
                st_df.loc[yr, 'RD_vote_r'] = int(subset_vr.loc['republican']) / int(subset_vr.loc['democrat'])
            else:
                st_df.loc[yr, 'RD_vote_r'] = np.NaN

            st_df.loc[yr, 'State'] = st

        state_df.append(st_df)
        break
    return pd.concat(state_df)

def main():
    house_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/house_district.csv', encoding = "ISO-8859-1")

    house_df = house(house_raw)
    house_df.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/house_02_18.csv')


if __name__ == '__main__':
    main()
