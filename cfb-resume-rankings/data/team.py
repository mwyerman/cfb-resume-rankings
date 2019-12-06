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
    oocWins: int
    oocGames: int
    losses: int
    winPct: float
    opponentsWins: int
    opponentsOpponentsWins: int
    opponentsLosses: int
    opponentsOpponentsLosses: int
    oocOW: int
    oocOL: int
    oocOOW: int
    oocOOL: int

    def __init__(self, args):
        for k, v in args.items():
            setattr(self, k, v)
        self.losses = len(self.schedule) - self.wins
        self.winPct = float(self.wins) / float(len(self.schedule)) if len(self.schedule) != 0 else 0
        self.oocOW = 0
        self.oocOL = 0
        self.oocOOW = 0
        self.oocOOL = 0
        self.opponentsWins = 0
        self.opponentsOpponentsWins = 0
        self.opponentsLosses = 0
        self.opponentsOpponentsLosses = 0

    def calculateOpponentsRecord(self, teams, games):
        for _, gameID in self.schedule.items():
            opponentID = games[gameID].getOpponent(self.id)
            if opponentID != self.id and opponentID in teams:
                opponentsWins = teams[opponentID].wins
                opponentsLosses = teams[opponentID].losses
                self.opponentsWins += opponentsWins
                self.opponentsLosses += opponentsLosses
                if not games[gameID].isSameConference():
                    self.oocOW += opponentsWins
                    self.oocOL += opponentsLosses
            elif opponentID not in teams:
                self.opponentsLosses += 6 #add 6 losses for FCS team
                self.oocOL += 6
    
    def calculateOpponentsOpponentsRecord(self, teams, games):
        for _, gameID in self.schedule.items():
            opponentID = games[gameID].getOpponent(self.id)
            if opponentID != self.id and opponentID in teams:
                opponentsOpponentsWins = teams[opponentID].opponentsWins
                opponentsOpponentsLosses = teams[opponentID].opponentsLosses
                self.opponentsOpponentsWins += opponentsOpponentsWins
                self.opponentsOpponentsLosses += opponentsOpponentsLosses
                if not games[gameID].isSameConference():
                    self.oocOOW += opponentsOpponentsWins
                    self.oocOOL += opponentsOpponentsLosses
            elif opponentID not in teams:
                self.opponentsOpponentsLosses += 6 * 11 #add 6 losses per FCS opponent's opponent
                self.oocOOL += 6 * 11

    def getStrengthOfSchedule(self):
        opponentsRecord = self.opponentsWins / float(self.opponentsWins + self.opponentsLosses)
        opponentsOpponentsRecord = self.opponentsOpponentsWins / float(self.opponentsOpponentsWins + self.opponentsOpponentsLosses)
        return ( (2 * opponentsRecord) + opponentsOpponentsRecord ) / 3.0

    def getOocStrengthOfSchedule(self):
        opponentsRecord = self.oocOW / float(self.oocOW + self.oocOL)
        opponentsOpponentsRecord = self.oocOOW / float(self.oocOOW + self.oocOOL)
        return ( (2 * opponentsRecord) + opponentsOpponentsRecord ) / 3.0

    def getInfo(self):
        return {
            'id': self.id,
            'school': self.school,
            'conference': self.conference,
            'division': self.division,
    }