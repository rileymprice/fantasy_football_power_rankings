import os
import numpy as np
import sleeper_wrapper
from tqdm import tqdm


LEAGUE_ID = os.environ.get("SLEEPER_LEAGUE_ID")
LEAGUE = sleeper_wrapper.League(LEAGUE_ID)
MAX_WEEKS = 13
TEAM_COUNT = 10


def two_step(league_id, max_weeks):
    """Takes league ID and max weeks and provides a dictionary of roster IDs and two step dominance sum"""
    total_results = []
    for week in tqdm(range(1, MAX_WEEKS + 1)):
        weekly_matchups = LEAGUE.get_matchups(week)
        # print(weekly_matchups)
        matchup_results = {}
        for team in weekly_matchups:
            roster_id = team["roster_id"]
            points = team["points"]
            matchup_id = team["matchup_id"]
            if matchup_id in matchup_results:
                matchup_results[matchup_id].append({"team": roster_id, "score": points})
            else:
                matchup_results[matchup_id] = [{"team": roster_id, "score": points}]
        for matchup in matchup_results.values():
            if matchup[0]["score"] > matchup[1]["score"]:
                winner_loser = (matchup[0]["team"], matchup[1]["team"])
            else:
                winner_loser = (matchup[1]["team"], matchup[0]["team"])
            total_results.append(winner_loser)

    team_array = np.zeros((TEAM_COUNT, TEAM_COUNT), dtype=int)
    team_final = {}
    for winning_team, losing_team in np.ndindex(team_array.shape):
        if (winning_team + 1, losing_team + 1) in total_results:
            team_array[winning_team, losing_team] = 1
    square_team_array = np.matmul(team_array, team_array)
    team_index = 1
    for row in team_array:
        for value in row:
            # print(value)
            if team_index in team_final.keys():
                team_final[team_index] += value
            else:
                team_final[team_index] = value
        team_index += 1
    team_index = 1
    for row in square_team_array:
        for value in row:
            if team_index in team_final.keys():
                team_final[team_index] += value
            else:
                team_final[team_index] = value
        team_index += 1
    return team_final
