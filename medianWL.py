import sleeper_wrapper
from statistics import median
from tqdm import tqdm
from collections import defaultdict


def medianWL(league_id, max_week):
    """Given League ID and # weeks, returns dictionary of team IDs and number of wins to the median score each week"""
    total_ranking = defaultdict(int)
    LEAGUE = sleeper_wrapper.League(league_id)
    for week in tqdm(range(max_week + 1)):
        score_list = []
        team_scores = {}
        weekly_matchups = LEAGUE.get_matchups(week)
        if weekly_matchups:
            for matchup in weekly_matchups:
                score = matchup["points"]
                roster_id = matchup["roster_id"]
                score_list.append(score)
                team_scores[roster_id] = score
            median_score = median(score_list)
            for team_id, score in team_scores.items():
                if score > median_score:
                    total_ranking[team_id] += 1
    return total_ranking
