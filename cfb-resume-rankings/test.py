import pprint

from data.getdata import getData
from models.SosModel import SosModel

pp = pprint.PrettyPrinter(indent=2)

teams, conferences, games = getData(2019)

randRankings = SosModel(teams, conferences, games)

rankings = randRankings.getTopNTeams(25)

def printRankings(rankings):
    print('{:3}  {:21} {:5} {}'.format('Rnk', 'Team', 'W/L', 'Pts'))
    for i, entry in rankings.items():
        team = entry[0]
        pts = entry[1]
        for t in team:
            print('{:3}: {:21} {:>2}-{:<2} {}'.format(i, teams[t].school,teams[t].wins, teams[t].losses, pts))

printRankings(rankings)

# sos = dict()
# for _, team in teams.items():
#     #print('{}: OR={}-{} OOR={}-{}'.format(team.school, team.opponentsWins, team.opponentsLosses, team.opponentsOpponentsWins, team.opponentsOpponentsLosses))
#     sos[team.school] = team.getStrengthOfSchedule()

# i = 0
# done = set()
# while i < len(sos):
#     best = 0
#     team = ''
#     for t, s in sos.items():
#         if s > best and t not in done:
#             best = s
#             team = t
#     done.add(team)
#     i += 1
#     print('{}: {} - {}'.format(i, team, best))