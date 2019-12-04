from .model import Model

class WtWinRatioModel(Model):
    def calculateRankings(self):
        for teamID, team in self.teams.items():
            pts = 0
            for _, gameID in team.schedule.items():
                game = self.games[gameID]
                opp = game.getOpponent(teamID)
                if game.winner() == teamID:
                    if isinstance(opp, int):
                        oppWins = self.teams[opp].wins
                        oppLosses = self.teams[opp].losses
                    else:
                        oppWins = 0
                        oppLosses = 0
                    pts += oppWins / oppLosses if oppLosses != 0 else oppWins
            self.teamRankingPoints[teamID] = pts