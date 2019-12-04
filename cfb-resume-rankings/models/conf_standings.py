

class ConfStandings:
    def __init__(self, teams, conferences, games):
        standings = dict()
        divs = dict()
        for i, c in conferences.items():
            for t in c.teams:
                team = teams[t]
                for week, g in team.schedule.items():
                    game = games[g]
                    

