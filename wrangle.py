
import json
import pandas as pd

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
        i = 1
        for game_id, stats in match_stats.items():
            for key,val in stats.items():
                    if key in top_ids.values():
                        season_games[file][key][i] = {'possession': val['aggregate_stats']['possession_percentage'],
                                                      'total_pass': val['aggregate_stats']['total_pass'],
                                                      'total_tackle': val['aggregate_stats']['total_tackle'],
                                                      'shots_off_target': val['aggregate_stats']['shot_off_target'],
                                                      'corners': val['aggregate_stats']['won_corners'],
                                                      'goals': val['aggregate_stats']['goals'],
                                                      'accurate_pass': val['aggregate_stats']['accurate_pass'],
                                                      'yellow_card':0,
                                                      'red_card':0,
                                                      'fouls':0,
                                                      'total_offside': val['aggregate_stats']['total_offside']
                                                    }
                    for player_name in val['Player_stats']:
                        print(file,player_name,key)
                        if 'yellow_card' in val['Player_stats'][player_name]['Match_stats']:
                                season_games[file][key][i]['yellow_card'] += 1
                        if 'red_card' in val['Player_stats'][player_name]['Match_stats']:
                            season_games[file][key][i]['red_card'] += 1

                    i += 1

    print('he''[')
if __name__ == '__main__':
    wrangle()