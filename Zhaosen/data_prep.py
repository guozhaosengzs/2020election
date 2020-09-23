import pandas as pd


def house(df):
    years = [2002, 2006, 2010, 2014, 2018]
    states = ['PA', 'AZ']
    st_dfs = []

    for st in states:
        st_df = pd.DataFrame(columns=['RD_vote_r', 'RD_dist_diff'], index=[2006, 2010, 2014, 2018])

        for yr in years:
            subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
            subset = subset[['state_po', 'district', 'party', 'candidatevotes']]
            subset_vr = subset.groupby(['party'])[['candidatevotes']].agg('sum')
            subset_dd = subset[subset.groupby(['district'])['candidatevotes'].transform(max) == subset['candidatevotes']]

            st_df.loc[yr, 'RD_vote_r'] = int(subset_vr.loc['republican']) / int(subset_vr.loc['democrat'])

            district = subset_dd['party'].value_counts()
            st_df.loc[yr, 'RD_dist_diff'] = int(district.loc['republican']) - int(district.loc['democrat'])

        st_dfs.append(st_df)

    return st_dfs


def senate(df):
    years1 = [2000, 2006, 2012, 2018]
    years3 = [1998, 2004, 2010, 2016]
    states = ['PA', 'AZ']
    st_dfs = []

    for st in states:
        st_df = pd.DataFrame(columns=['RD_vote_r', 'Class'], index=[1998, 2000, 2004, 2006, 2010, 2012, 2016, 2018])

        for yr in years1:
            if yr == 2000 and st == 'AZ':
                st_df.loc[yr, 'RD_vote_r'] = 3.83558994197
                st_df.loc[yr, 'Class'] = 1
            else:
                subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
                subset = subset[['state_po', 'party', 'candidatevotes']]
                subset = subset.groupby(['party'])[['candidatevotes']].agg('sum')

                st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democrat'])
                st_df.loc[yr, 'Class'] = 1

        for yr in years3:
            subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
            subset = subset[['state_po', 'party', 'candidatevotes']]
            subset = subset.groupby(['party'])[['candidatevotes']].agg('sum')

            st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democrat'])
            st_df.loc[yr, 'Class'] = 3


        st_dfs.append(st_df)

    return st_dfs


def potus(df):
    years = [2000, 2004, 2008, 2012, 2016]
    states = ['PA', 'AZ']
    st_dfs = []

    for st in states:
        st_df = pd.DataFrame(columns=['RD_vote_r'], index=[2000, 2004, 2008, 2012, 2016])

        for yr in years:
            subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
            subset = subset[['state_po', 'party', 'candidatevotes']]
            subset = subset.groupby(['party'])[['candidatevotes']].agg('sum')

            st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democrat'])

        st_dfs.append(st_df)

    return st_dfs


def main():
    house_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/house_district.csv', encoding = "ISO-8859-1")
    senate_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/senate_state.csv', encoding = "ISO-8859-1")
    potus_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/president_state.csv', encoding = "ISO-8859-1")


    # pa_house, az_house = house(house_raw)
    # pa_house.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/pa_house.csv')
    # az_house.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/az_house.csv')

    pa_senate, az_senate = senate(senate_raw)
    pa_senate.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/pa_senate.csv')
    az_senate.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/az_senate.csv')

    pa_potus, az_potus = potus(potus_raw)
    pa_potus.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/pa_potus1.csv')
    az_potus.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/az_potus1.csv')



if __name__ == '__main__':
    main()
