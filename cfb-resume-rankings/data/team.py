import requests

class Team:
    id: int
    school: str
    mascot: str = None
    abbreviation: str = None
    alt_name_1: str = None
    alt_name_2: str = None
    alt_name_3: str = None
    conference: str
    division: str
    color: str = None
    alt_color: str = None
    logos: list = None
    schedule: dict = dict()
    wins: int
    losses: int
    winPct: float

    def __init__(self, args):
        for k, v in args.items():
            setattr(self, k, v)
        self.losses = len(self.schedule) - self.wins
        self.winPct = float(self.wins) / float(len(self.schedule)) if len(self.schedule) != 0 else 0

    def getInfo(self):
        return {
            'id': self.id,
            'school': self.school,
            'conference': self.conference,
            'division': self.division,
        }