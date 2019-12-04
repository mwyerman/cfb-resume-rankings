from typing import Dict, List, Tuple
from random import randint

class Model:
    teamRankingPoints: Dict[int, float]
    def __init__(self, teams, conferences, games) -> None:
        self.teams = teams
        self.conferences = conferences
        self.games = games
        self.teamRankingPoints = dict()

        self.calculateRankings()
    
    # randomized rankings with ties
    def calculateRankings(self) -> None:
        for t in self.teams:
            self.teamRankingPoints[t] = randint(0, 50)
        
    def getTopNTeams(self, n:int=None) -> Dict[int, Tuple[List[int], float]]:
        rankings = dict()
        ranked = set()
        currentRank = 1
        num = n if n != None else len(self.teamRankingPoints)
        while currentRank <= num:
            highestPts = 0
            teams = []
            for t, pts in self.teamRankingPoints.items():
                if t not in ranked:
                    if pts > highestPts:
                        highestPts = pts
                        teams = [t]
                    elif pts == highestPts:
                        teams.append(t)
            rankings[currentRank] = (teams, highestPts)
            for t in teams:
                ranked.add(t)
            currentRank += len(teams)
        return rankings