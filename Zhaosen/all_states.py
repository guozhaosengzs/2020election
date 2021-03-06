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

    # house_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/house_district.csv', encoding = "ISO-8859-1")
    # house_df = house(house_raw)
    # house_df.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/house_02_18.csv')

    # potus_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/president_state.csv', encoding = "ISO-8859-1")
    # potus_df = potus(potus_raw)
    # potus_df.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/potus_04_16.csv')

    # Using produced data from above
    house_df = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/house_02_18.csv')
    potus_df = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/potus_04_16.csv')

    change_trend = pd.DataFrame(columns=['House', 'President', 'State', 'Class'])
    states = house_df.State.unique()
    house_yrs = sorted(house_df.Year.unique())
    potus_yrs = sorted(potus_df.Year.unique())

    for st in states:
        for i in range(len(potus_yrs)):

            hy0 = house_df[(house_df.Year == house_yrs[i]) & (house_df.State == st)].RD_vote_r.item()
            hy1 = house_df[(house_df.Year == house_yrs[i + 1]) & (house_df.State == st)].RD_vote_r.item()
            hdiff = hy1 - hy0

            if i < 3:
                py0 = potus_df[(potus_df.Year == potus_yrs[i]) & (potus_df.State == st)].RD_vote_r.item()
                py1 = potus_df[(potus_df.Year == potus_yrs[i + 1]) & (potus_df.State == st)].RD_vote_r.item()
                pdiff = py1 - py0

                nrow = {'House': hdiff, 'President' : pdiff, 'State': st, 'Class': 'T'}

            else:
                nrow = {'House': hdiff, 'President' : None, 'State': st, 'Class': 'P'}

            change_trend = change_trend.append(nrow, ignore_index=True)

    change_trend.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/trend_compare.csv')


if __name__ == '__main__':
    main()
