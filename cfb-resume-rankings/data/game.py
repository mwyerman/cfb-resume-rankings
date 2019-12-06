from typing import List, Tuple, Dict

class Game:
    id: int
    season: int
    week: int
    season_type: str
    start_date: str
    neutral_site: bool
    conference_game: bool
    attendance: int
    venue_id: int
    venue: str
    home_team: int
    home_conference: int
    home_division: int
    home_points: int
    home_line_scores: List[int]
    home_post_win_prob: float
    away_team: int
    away_conference: int
    away_division: int
    away_points: int
    away_line_scores: List[int]
    away_post_win_prob: float

    def __init__(self, obj) -> None:
        for k, v in obj.items():
            setattr(self, k, v)
    
    def marginOfVictory(self) -> int:
        return abs(self.home_points - self.away_points)
    
    def winner(self) -> int:
        if self.home_points > self.away_points:
            return self.home_team
        else:
            return self.away_team
    
    def getOpponent(self, teamID):
        if teamID == self.home_team:
            return self.away_team
        elif teamID == self.away_team:
            return self.home_team

    def isSameConference(self):
        return self.home_conference == self.away_conference

    def isSameDivision(self):
        return self.home_division == self.away_division

    def result(self):
        return (self.winner(), self.marginOfVictory())

    def getInfo(self) -> Dict[str, int]:
        return {
            'home_team': self.home_team,
            'away_team': self.away_team,
            'home_points': self.home_points,
            'away_points': self.away_points,
            'home_conference': self.home_conference,
            'away_conference': self.away_conference,
            'home_division': self.home_division,
            'away_division': self.away_division,
            'same_conference': self.isSameConference(),
            'same_division': self.isSameDivision(),
        }