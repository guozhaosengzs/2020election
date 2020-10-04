import pandas as pd



def main():
    data = pd.read_csv('https://raw.githubusercontent.com/guozhaosengzs/2020election/master/Zhaosen/data/output.csv')

    dict = us_states()
    electoral = state_votes()
    abbrev_electoral = {v: electoral[k] for k,v in dict.items()}

    dem_votes = 0
    rep_votes = 0

    for k,v in abbrev_electoral.items():
        if k == 'DC':
            dem_votes += v
        else:
            R_D_Ratio = data.loc[data['State'] == k].Pred_Ratio_2020.item()
            if R_D_Ratio > 1:
                rep_votes += v
            else:
                dem_votes += v

    print("Electoral Votes for Prediction: \nDemocrat: ", dem_votes, "\nRepublican: ", rep_votes)


def us_states():
    name_to_abbr = {
        'District of Columbia': 'DC',
        'Alabama': 'AL',
        'Montana': 'MT',
        'Alaska': 'AK',
        'Nebraska': 'NE',
        'Arizona': 'AZ',
        'Nevada': 'NV',
        'Arkansas': 'AR',
        'New Hampshire': 'NH',
        'California': 'CA',
        'New Jersey': 'NJ',
        'Colorado': 'CO',
        'New Mexico': 'NM',
        'Connecticut': 'CT',
        'New York': 'NY',
        'Delaware': 'DE',
        'North Carolina': 'NC',
        'Florida': 'FL',
        'North Dakota': 'ND',
        'Georgia': 'GA',
        'Ohio': 'OH',
        'Hawaii': 'HI',
        'Oklahoma': 'OK',
        'Idaho': 'ID',
        'Oregon': 'OR',
        'Illinois': 'IL',
        'Pennsylvania': 'PA',
        'Indiana': 'IN',
        'Rhode Island': 'RI',
        'Iowa': 'IA',
        'South Carolina': 'SC',
        'Kansas': 'KS',
        'South Dakota': 'SD',
        'Kentucky': 'KY',
        'Tennessee': 'TN',
        'Louisiana': 'LA',
        'Texas': 'TX',
        'Maine': 'ME',
        'Utah': 'UT',
        'Maryland': 'MD',
        'Vermont': 'VT',
        'Massachusetts': 'MA',
        'Virginia': 'VA',
        'Michigan': 'MI',
        'Washington': 'WA',
        'Minnesota': 'MN',
        'West Virginia': 'WV',
        'Mississippi': 'MS',
        'Wisconsin': 'WI',
        'Missouri': 'MO',
        'Wyoming': 'WY'
    }

    return name_to_abbr


def state_votes():
    electoral_college = {
        "Alabama":9,
        "Alaska":3,
        "Arizona":11,
        "Arkansas":6,
        "California":55,
        "Colorado":9,
        "Connecticut":7,
        "District of Columbia":3,
        "Delaware":3,
        "Florida":29,
        "Georgia":16,
        "Hawaii":4,
        "Idaho":4,
        "Illinois":20,
        "Indiana":11,
        "Iowa":6,
        "Kansas":6,
        "Kentucky":8,
        "Louisiana":8,
        "Maine":4,
        "Maryland":10,
        "Massachusetts":11,
        "Michigan":16,
        "Minnesota":10,
        "Mississippi":6,
        "Missouri":10,
        "Montana":3,
        "Nebraska":5,
        "Nevada":6,
        "New Hampshire":4,
        "New Jersey":14,
        "New Mexico":5,
        "New York":29,
        "North Carolina":15,
        "North Dakota":3,
        "Ohio":18,
        "Oklahoma":7,
        "Oregon":7,
        "Pennsylvania":20,
        "Rhode Island":4,
        "South Carolina":9,
        "South Dakota":3,
        "Tennessee":11,
        "Texas":38,
        "Utah":6,
        "Vermont":3,
        "Virginia":13,
        "Washington":12,
        "West Virginia":5,
        "Wisconsin":10,
        "Wyoming":3
    }

    return electoral_college


if __name__ == '__main__':
    main()
