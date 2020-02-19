import os
import sleeper_wrapper
import medianWL

LEAGUE_ID = os.environ.get("SLEEPER_LEAGUE_ID")
MAX_WEEKS = 13
STATS = sleeper_wrapper.Stats()

LEAGUE = sleeper_wrapper.League(LEAGUE_ID)

TEAMS = LEAGUE.get_rosters()
median_wl = medianWL.medianWL(LEAGUE_ID, MAX_WEEKS)
print(TEAMS)
