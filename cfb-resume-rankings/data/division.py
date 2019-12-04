from typing import List

class Division:
    id: int
    name: str
    teams: List[int] = []

    def __init__(self, id, name, teams=[]):
        self.id = id
        self.name = name
        self.teams = teams

    def getInfo(self):
        return {
            'id': self.id,
            'name': self.name,
            'schools': self.teams,
        }