from pybaseball import schedule_and_record
import pandas as pd
import glob
import os

def build_data(mlb_teams):
    '''Builds the data for each team'''
    
    for team in mlb_teams:
        data = schedule_and_record(2024, team)
        data.to_csv(f"team_game_logs/{team}.csv", sep=',', encoding="utf-8")


def main():

    mlb_teams = [
        "BAL", "BOS", "CHW", "CLE", "DET", "HOU", "KC", "LAA", "LAD", "MIN", "NYY", "OAK", "SEA", "TBR", "TEX", "TOR",
        "ARI", "ATL", "CHC", "CIN", "COL", "MIA", "MIL", "NYM", "PHI", "PIT", "SDP", "SFG", "STL", "WSN"
    ]
    
    build_data(mlb_teams=mlb_teams)

    exit()
    path = r'team_game_logs/' # use your path
    all_files = glob.glob(os.path.join(path , "*.csv"))

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    frame.to_csv('unrefined_set.csv', sep=',', encoding='utf-8')

    frame.drop_duplicates(subset=['Date', 'Attendance'], keep='first', inplace=True, ignore_index=True)

    frame.to_csv(f'master_set.csv', sep=',', encoding='utf-8')

    print(frame)
    
if __name__=="__main__":
    main()