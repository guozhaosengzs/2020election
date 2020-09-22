import pandas as pd


def house(df):
    years = [2006, 2010, 2014, 2018]
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

# def senate(df):
#     years = [2012, 2016]
#     states = ['PA', 'AZ']
#     st_dfs = []
#
#     for st in states:
#         st_df = pd.DataFrame(columns=['RD_vote_r'], index=[2012, 2016])
#
#         for yr in years:
#             subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
#             subset = subset[['state_po', 'party', 'candidatevotes']]
#             subset = subset.groupby(['party'])[['candidatevotes']].agg('sum')
#
#             st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democrat'])
#
#         st_dfs.append(st_df)
#
#     return st_dfs




def potus(df):
    years = [2008, 2012, 2016]
    states = ['PA', 'AZ']
    st_dfs = []

    for st in states:
        st_df = pd.DataFrame(columns=['RD_vote_r'], index=[2012, 2016])

        for yr in years:
            subset = df.loc[(df['year'] == yr) & (df['state_po'] == st)]
            subset = subset[['state_po', 'party', 'candidatevotes']]
            subset = subset.groupby(['party'])[['candidatevotes']].agg('sum')

            st_df.loc[yr, 'RD_vote_r'] = int(subset.loc['republican']) / int(subset.loc['democrat'])

        st_dfs.append(st_df)

    return st_dfs

    # for i in range(4):
    #     year, state = list[i]
    #
    #     df = house_raw.loc[(house_raw['year'] == year) & (house_raw['state_po'] == state)]
    #     df = df[['year', 'state_po', 'district', 'party', 'candidatevotes']]
    #     dfv = df.groupby(['party'])[['candidatevotes']].agg('sum')
    #     df = df[df.groupby(['district'])['candidatevotes'].transform(max) == df['candidatevotes']]
    #     df.reset_index(drop=True, inplace=True)
    #
    #     dfs_district.append(df)
    #     dfs_tvotes.append(dfv)
    #
    # house_2010_pa = dfs_district[0]
    # house_2014_pa = dfs_district[1]
    # house_2010_az = dfs_district[2]
    # house_2014_az = dfs_district[3]
    #
    # pa_2010 = house_2010_pa['party'].value_counts().to_frame()
    # pa_2014 = house_2014_pa['party'].value_counts().to_frame()
    # pa_house = pd.concat([pa_2010, pa_2014, dfs_tvotes[0], dfs_tvotes[1]], join = 'inner', axis = 1)
    # pa_house.columns = ['2010D', '2014D', '2010V', '2014V']
    #
    # az_2010 = house_2010_az['party'].value_counts().to_frame()
    # az_2014 = house_2014_az['party'].value_counts().to_frame()
    # az_house = pd.concat([az_2010, az_2014, dfs_tvotes[2], dfs_tvotes[3]], join = 'inner', axis = 1)
    # az_house.columns = ['2010D', '2014D', '2010V', '2014V']
    #
    # pa_house.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/pa_house.csv')
    # az_house.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/az_house.csv')



def main():
    house_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/house_district.csv', encoding = "ISO-8859-1")
    senate_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/senate_state.csv', encoding = "ISO-8859-1")
    potus_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/president_state.csv', encoding = "ISO-8859-1")


    pa_house, az_house = house(house_raw)
    pa_house.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/pa_house.csv')
    az_house.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/az_house.csv')


    # pa_senate, az_senate = senate(senate_raw)
    pa_potus, az_potus = potus(potus_raw)
    pa_potus.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/pa_potus.csv')
    az_potus.to_csv(r'/Users/gzs/Desktop/MATH 503/2020election/Zhaosen/data/az_potus.csv')



if __name__ == '__main__':
    main()
