from typing import List, Dict, Tuple

from .division import Division

class Conference:       
    id: int
    name: str
    teams: List[int] = []
    divisions: Dict[int, Division]
    standings: Dict[int, Tuple[int, int] ]

    def __init__(self, args, teams, divisions):
        for k, v in args.items():
            setattr(self, k, v)
        self.divisions = divisions
        self.teams = teams
        self.standings = { t: (0, 0) for t in teams }
    
    def isIndependent(self):
        return id == 18

    def getInfo(self):
        return {
            'id': self.id,
            'name': self.name,
            'divisions': [d.getInfo() for _, d in self.divisions.items()],
        }

    def genStandings(self, games):
        if self.isIndependent():
            return 
        for game in games:
            g = games[game]
            if g.home_conference == self.id and g.isSameConference():
                winner = g.winner()
                winnerWL = self.standings[winner]
                winnerNewWL = ( winnerWL[0] + 1, winnerWL[1] )
                self.standings[winner] = winnerNewWL

                loser = g.getOpponent(winner)
                loserWL = self.standings[loser]
                loserNewWL = ( loserWL[0], loserWL[1] + 1 )
                self.standings[loser] = loserNewWL

