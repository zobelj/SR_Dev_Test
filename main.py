import pandas as pd
from datetime import datetime

def read_and_combine_tables():
    # Read the data into dataframes
    comps = pd.read_csv('sr_dev_competitions.csv')
    people = pd.read_csv('sr_dev_people.csv')
    stats = pd.read_csv('sr_dev_stats.csv')
    teams = pd.read_csv('sr_dev_teams.csv')

    # Merge the dataframes
    df = pd.merge(stats, people, on='person_id')
    df = pd.merge(df, teams, on="team_id")
    df = pd.merge(df, comps, on="comp_id")

    return df

def create_table(people_id, df):
    # filter by people_id, scope = domestic, and competition = league. sort by season
    df = df[(df['person_id'] == people_id) & (df['scope'] == 'domestic') & (df['competition_format'] == 'league')]
    df = df.sort_values(by=['season'])

    # birthday calculation
    df['birth_date'] = pd.to_datetime(df['birth_date'])
    df['season_start'] = pd.to_datetime('08-01-' + df['season'].str[:4])
    df['age'] = round((df['season_start'] - df['birth_date']).dt.days / 365, 0)

    # initialize the html string output
    output = '''
    <table>
        <tr class="header">
            <th>Season</th>
            <th>Age</th>
            <th>Team</th>
            <th>Country</th>
            <th>Competition</th>
            <th>Games</th>
            <th>Minutes</th>
            <th>Goals</th>
            <th>Assists</th>
            <th>Goals/90</th>
        </tr>
    '''

    for index, row in df.iterrows():
        output += f'''
            <tr>
                <td>{row['season']}</td>
                <td>{row['age']:.0f}</td>
                <td>{row['name_y']}</td>
                <td>{row['country_x']}</td>
                <td>{row['name']}</td>
                <td>{row['games']}</td>
                <td>{row['minutes']}</td>
                <td>{row['goals']}</td>
                <td>{row['assists']:.0f}</td>
                <td>{90 * row['goals'] / row['minutes']:.2f}</td>
            </tr>
        '''

    # add the totals row
    output += f'''
        <tr class="header">
            <td>{df['season'].count()} Seasons</td>
            <td></td>
            <td>{df['name_y'].nunique()} Clubs</td>
            <td></td>
            <td>{df['name'].nunique()} Competitions</td>
            <td>{df['games'].sum()}</td>
            <td>{df['minutes'].sum()}</td>
            <td>{df['goals'].sum()}</td>
            <td>{df['assists'].sum():.0f}</td>
            <td>{90 * df['goals'].sum() / df['minutes'].sum():.2f}</td>
        </tr>
    </table>
    '''

    # add style
    output += '''
    <style>
        * { font-family: Arial, Helvetica, sans-serif }
        .header > * { background-color: #d0d0d0 }

        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            justify-content: center;
            padding: 2px;
        }
        
        th > td { font-weight: bold }
    </style>
    '''

    return output

if __name__ == '__main__':
    df = read_and_combine_tables()

    output = create_table(people_id='dea698d9', df=df)

    print(output)

    # save the output to a file
    with open('joezobelj_sr_test.html', 'w') as f:
        f.write(output)

