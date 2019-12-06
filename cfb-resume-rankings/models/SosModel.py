from .model import Model

class SosModel(Model):
    def calculateRankings(self):
        for teamID, _ in self.teams.items():
            pts = 0
            for _, game in self.games.items():
                opponent = game.getOpponent(teamID)
                if opponent in self.teams:
                    oppSOS = self.teams[opponent].getStrengthOfSchedule()
                    oppWins = self.teams[opponent].wins
                    if game.winner() == teamID:
                        pts += oppSOS * oppWins
            self.teamRankingPoints[teamID]= pts
                