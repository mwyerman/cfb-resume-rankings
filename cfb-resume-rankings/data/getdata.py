import requests
import pprint

from .team import Team
from .game import Game
from .conference import Conference, Division

pp = pprint.PrettyPrinter(indent=2)

def getData(year: int):
    url = 'https://api.collegefootballdata.com/'
    params = { 'year': year }

    r = requests.get(url=url+'teams/fbs', params=params)
    teamData = r.json()
    r = requests.get(url=url+'conferences', params={})
    confData = r.json()
    r = requests.get(url=url+'games', params=params)
    gameData = r.json()

    confRaw = dict()
    confIDs = dict()
    for conference in confData:
        confIDs[conference['name']] = conference['id']
        confRaw[conference['id']] = conference

    confDivisions = dict()
    teamRaw = dict()
    teamIDs = dict()
    for team in teamData:
        t = team
        confID = confIDs[t['conference']]

        dName = t['division'] if t['division'] != None else t['conference']

        if confID not in confDivisions:
            confDivisions[confID] = dict()
        
        if dName not in confDivisions[confID]:
            confDivisions[confID][dName] = []

        confDivisions[confID][dName].append(t['id'])

        t['schedule'] = dict()
        t['wins'] = 0

        teamIDs[t['school']] = t['id']
        teamRaw[t['id']] = t
    
    divIDs = {}
    conferences = {}
    for id, divs in confDivisions.items():
        teams = []
        divisions = {}
        i = 1
        if id not in divIDs:
            divIDs[id] = dict()
        
        for name, div in divs.items():
            divID = (1000 * id) + i
            divIDs[id][name] = divID
            i += 1
            divisions[divID] = Division(divID, name, div)
            teams.extend(div)
        conferences[id] = Conference(confRaw[id], teams, divisions)

    gameRaw = dict()
    for game in gameData:
        g = game
        g['home_division'] = None
        g['away_division'] = None

        if g['home_points'] != None and g['away_points'] != None:
            homeID = 0
            awayID = 0
            if g['home_team'] in teamIDs:
                homeID = teamIDs[g['home_team']]
                homeConfID = confIDs[g['home_conference']]
                homeDiv = teamRaw[homeID]['division'] if teamRaw[homeID]['division'] != None else conferences[homeConfID].name
                homeDivID = divIDs[homeConfID][homeDiv]

                g['home_team'] = homeID
                g['home_conference'] = homeConfID
                g['home_division'] = homeDivID

            if g['away_team'] in teamIDs:
                awayID = teamIDs[g['away_team']]
                awayConfID = confIDs[g['away_conference']]
                awayDiv = teamRaw[awayID]['division'] if teamRaw[awayID]['division'] != None else conferences[awayConfID].name
                awayDivID = divIDs[awayConfID][awayDiv]

                g['away_team'] = awayID
                g['away_conference'] = awayConfID
                g['away_division'] = awayDivID

            if homeID in teamRaw:
                teamRaw[homeID]['schedule'][g['week']] = g['id']
                if g['home_points'] > g['away_points']:
                    teamRaw[homeID]['wins'] += 1

            if awayID in teamRaw:
                teamRaw[awayID]['schedule'][g['week']] = g['id']
                if g['away_points'] > g['home_points']:
                    teamRaw[awayID]['wins'] += 1
            
            gameRaw[g['id']] = g

    games = dict()
    for id, game in gameRaw.items():
        if game['home_points'] != None:
            games[id] = Game(game)
    
    teams = dict()
    for id, team in teamRaw.items():
        teams[id] = Team(team)

    for _, team in teams.items():
        team.calculateOpponentsRecord(teams, games)
    for _, team in teams.items():
        team.calculateOpponentsOpponentsRecord(teams, games)
    
    
    return (teams, conferences, games)
    


    
