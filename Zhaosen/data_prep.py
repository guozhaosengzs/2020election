import pandas as pd


def main():
    house_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/house_district.csv', encoding = "ISO-8859-1")
    senate_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/senate_state.csv', encoding = "ISO-8859-1")
    potus_raw = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/president_state.csv', encoding = "ISO-8859-1")


    # House-district data set 2010 vs 2014 for 2016
    list = [(2010, 'PA'), (2014, 'PA'),(2010, 'AZ'), (2014, 'AZ')]
    dfs_district = []
    dfs_tvotes = []

    for i in range(4):
        year, state = list[i]

        df = house_raw.loc[(house_raw['year'] == year) & (house_raw['state_po'] == state)]
        df = df[['year', 'state_po', 'district', 'party', 'candidatevotes']]
        dfv = df.groupby(['party'])[['candidatevotes']].agg('sum')
        df = df[df.groupby(['district'])['candidatevotes'].transform(max) == df['candidatevotes']]
        df.reset_index(drop=True, inplace=True)

        dfs_district.append(df)
        dfs_tvotes.append(dfv)

    house_2010_pa = dfs_district[0]
    house_2014_pa = dfs_district[1]
    house_2010_az = dfs_district[2]
    house_2014_az = dfs_district[3]

    pa_2010 = house_2010_pa['party'].value_counts().to_frame()
    pa_2014 = house_2014_pa['party'].value_counts().to_frame()
    pa_house = pd.concat([pa_2010, pa_2014, dfs_tvotes[0], dfs_tvotes[1]], join = 'inner', axis = 1)
    pa_house.columns = ['2010D', '2014D', '2010V', '2014V']






    az_2010 = house_2010_az['party'].value_counts().to_frame()
    az_2014 = house_2014_az['party'].value_counts().to_frame()
    az_house = pd.concat([az_2010, az_2014, dfs_tvotes[2], dfs_tvotes[3]], join = 'inner', axis = 1)
    az_house.columns = ['2010D', '2014D', '2010V', '2014V']

    print(az_house)



if __name__ == '__main__':
    main()
