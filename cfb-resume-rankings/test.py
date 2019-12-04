import pprint

from data.getdata import getData
from models.WtWinRatioModel import WtWinRatioModel

pp = pprint.PrettyPrinter(indent=2)

teams, conferences, games = getData(2019)

# randRankings = WtWinRatioModel(teams, conferences, games)

# rankings = randRankings.getTopNTeams(25)

# def printRankings(rankings):
#     print('{:3}  {:21} {:5} {}'.format('Rnk', 'Team', 'W/L', 'Pts'))
#     for i, entry in rankings.items():
#         team = entry[0]
#         pts = entry[1]
#         for t in team:
#             print('{:3}: {:21} {:>2}-{:<2} {}'.format(i, teams[t].school,teams[t].wins, teams[t].losses, pts))

# printRankings(rankings)

for i, c in conferences.items():
    c.genStandings(games)
    print('\n')
    print(c.getInfo())
    for t, wl in c.standings.items():
        print(teams[t].school, wl)

