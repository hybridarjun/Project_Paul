
import json
import pandas as pd
import pprint
def wrangle():
    files_list = ['14-15','15-16','16-17','17-18']
    team_ids = {}
    matches = {}
    top_ids = {'Chelsea': '15', 'Arsenal': '13', 'Liverpool': '26', 'Manchester United': '32', 'Manchester City':'167', 'Tottenham': '30'}
    season_games = {}
    games = {}
    for file in files_list:
        with open('datafile/season{}/season_match_stats.json'.format(file), 'r') as in_file:

            match_data = json.load(in_file)
        with open('datafile/season{}/season_stats.json'.format(file), 'r') as in_file:

            match_stats = json.load(in_file)



        for key, val in match_data.items():

            if val['home_team_name'] not in team_ids:
                team_ids[val['home_team_name']] = val['home_team_id']

            if val['away_team_name'] not in team_ids:
                team_ids[val['away_team_name']] = val['away_team_id']

            matches[key] = [val['home_team_id'],val['away_team_id']]
        if file not in season_games:
            season_games[file] = {}

        for top_id in top_ids.values():
            i = 1
            for game_id, stats in match_stats.items():
                for key,val in stats.items():
                        if key == top_id:
                            if key not in season_games[file]:
                                season_games[file][key] = {}
                            print(key,i)
                            season_games[file][key][i] = {'possession': val['aggregate_stats']['possession_percentage'],
                                                      'total_pass': val['aggregate_stats']['total_pass'],
                                                      'total_tackle': val['aggregate_stats']['total_tackle'],
                                                      'shots_off_target': 0,
                                                      'corners': 0,
                                                      'goals': 0,
                                                      'accurate_pass': val['aggregate_stats']['accurate_pass'],
                                                      'yellow_card':0,
                                                      'red_card':0,
                                                      'fouls':0,
                                                      'total_offside': 0
                                                    }
                            if 'shot_off_target' in val['aggregate_stats']:
                                season_games[file][key][i]['shots_off_target'] += 1
                            if 'corners' in val['aggregate_stats']:
                                season_games[file][key][i]['corners'] += 1
                            if 'total_offside' in val['aggregate_stats']:
                                season_games[file][key][i]['total_offside'] += 1

                            if 'goals' in val['aggregate_stats']:
                                season_games[file][key][i]['goals'] += 1

                            for player_name in val['Player_stats']:
                                #print(file,player_name,key)
                                if 'yellow_card' in val['Player_stats'][player_name]['Match_stats']:
                                    season_games[file][key][i]['yellow_card'] += 1
                                if 'red_card' in val['Player_stats'][player_name]['Match_stats']:
                                    season_games[file][key][i]['red_card'] += 1

                            i += 1

    df = pd.DataFrame.from_dict(season_games['15-16']['15'])

    pprint.pprint(len(season_games['15-16']['15']))
    print('he''[')
if __name__ == '__main__':
    wrangle()