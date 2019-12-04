from .model import Model

class WtWinPctModel(Model):
    def calculateRankings(self):
        for teamID, team in self.teams.items():
            pts = 0
            for _, gameID in team.schedule.items():
                game = self.games[gameID]
                opp = game.getOpponent(teamID)
                if game.winner() == teamID:
                    if isinstance(opp, int):
                        oppWinPct = self.teams[opp].winPct
                    else:
                        oppWinPct = 0
                    pts += oppWinPct
            self.teamRankingPoints[teamID] = pts