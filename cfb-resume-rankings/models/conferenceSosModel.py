from .model import Model

class ConferenceSosModel(Model):
    def calculateRankings(self):
        conferenceStrength = dict()
        for confID, conference in self.conferences.items():
            conferenceStrength[confID] = 0
            gamesPlayed = 0
            wins = 0
            for team in conference.teams:
                oocSoS = self.teams[team].getOocStrengthOfSchedule()
                conferenceStrength[confID] += oocSoS
                gamesPlayed += self.teams[team].oocGames
                wins += self.teams[team].oocWins
            conferenceStrength[confID] /= float(len(conference.teams))
            conferenceStrength[confID] *= wins / float(gamesPlayed)
        
        for confID, conference in self.conferences.items():
            print('{}: {}'.format(conference.name, conferenceStrength[confID]))
        for teamID, _ in self.teams.items():
            pts = 0
            for _, game in self.games.items():
                opponent = game.getOpponent(teamID)
                if opponent in self.teams:
                    oppConfSoS = conferenceStrength[self.teams[opponent].conference]
                    oppWins = self.teams[opponent].wins
                    if game.winner() == teamID:
                        pts += oppConfSoS * oppWins
            self.teamRankingPoints[teamID]= pts
                