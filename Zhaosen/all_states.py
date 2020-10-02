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
            subset_vr = subset.groupby(['party'])[['candidatevotes']].agg('sum')

            pl = subset_vr.index.tolist()
            if 'democrat' in pl:
                st_df.loc[yr, 'RD_vote_r'] = int(subset_vr.loc['republican']) / int(subset_vr.loc['democrat'])
            if 'democrat' not in pl and 'democratic-farmer-labor' in pl:
                st_df.loc[yr, 'RD_vote_r'] = int(subset_vr.loc['republican']) / int(subset_vr.loc['democratic-farmer-labor'])
            elif 'democrat' not in pl and 'democratic-nonpartisan league' in pl:
                st_df.loc[yr, 'RD_vote_r'] = int(subset_vr.loc['republican']) / int(subset_vr.loc['democratic-nonpartisan league'])
            elif 'democrat' not in pl and 'democratic-npl' in pl:
                st_df.loc[yr, 'RD_vote_r'] = int(subset_vr.loc['republican']) / int(subset_vr.loc['democratic-npl'])

            st_df.loc[yr, 'State'] = st

        state_df.append(st_df)

    return pd.concat(state_df)


def potus(df):
    years = [2004, 2008, 2012, 2016]
    states = df.state_po.unique()
    st_dfs = []

    for st in states:
        st_df = pd.DataFrame(columns=['RD_vote_r', 'State'], index=years)
        st_df.index.name = 'Year'

        for yr in years:
            subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
            subset = subset[['state_po', 'party', 'candidatevotes']]
            subset = subset.groupby(['party'])[['candidatevotes']].agg('sum')

            pl = subset.index.tolist()
            if 'democrat' in pl:
                st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democrat'])
            if 'democrat' not in pl and 'democratic-farmer-labor' in pl:
                st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democratic-farmer-labor'])

            st_df.loc[yr, 'State'] = st

        st_dfs.append(st_df)

    return pd.concat(st_dfs)


def main():
    house_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/house_district.csv', encoding = "ISO-8859-1")
    house_df = house(house_raw)
    # house_df.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/house_02_18.csv')

    potus_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/president_state.csv', encoding = "ISO-8859-1")
    potus_df = potus(potus_raw)
    # potus_df.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/potus_04_16.csv')

    change_trend = pd.DataFrame(columns=['House', 'President', 'State', 'Type'])
    states = house_df.State.unique()
    house_yrs = sorted(list(set(house_df.index.tolist())))
    potus_yrs = sorted(list(set(potus_df.index.tolist())))

    print(house_yrs, potus_yrs)
    # for st in states:
    #     for i in range(len(potus_yrs)):
    #         hy0 = house_yrs[i]
    #
    #         if i < 3:
    #
    #         else:
    #
    #         change_trend.append(new_row, ignore_index=True)
    #



if __name__ == '__main__':
    main()
