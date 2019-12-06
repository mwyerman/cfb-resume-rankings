from .model import Model

class WinModel(Model):
    def calculateRankings(self):
        for teamID, team in self.teams.items():
            pts = team.wins
            self.teamRankingPoints[teamID] = pts