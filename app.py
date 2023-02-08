#Proper use of Dunder Main
#Import player and team data
    #import from constants.py
    #should not be hard coded into script
    #changes should be reflected

from constants import TEAMS, PLAYERS

#Create a clean_data function
def clean_data():
    #read existing player data from PLAYERS im constants.py
    #clean player data w/o changing original data
    cleaned = []
    for player in PLAYERS:
        fixed = {}
        fixed['name'] = player
        fixed['gaurdians'] = player['gaurdians']
        #save new collection
        #height -- saved as an integer
        fixed['height'] = height_data
        height_data = int(player['height'].split(" ")[0])
        #experience -- saved as a boolean value (True or False)
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else: 
            fixed['experience'] = False
    
    cleaned.append(fixed)
    #data returned cleaned
    return cleaned

#Create balance_teams function
def balance_teams():
# Balance players across three teams: Panthers, Bandits, and  Warriors
    team_panthers = []
    team_bandits = []
    team_warriors = []
# Organize teams based on experienced vs inexperienced players 
    experienced_player = []
    inexperienced_player = []
# functions, packing, and unpacking


# HINT: To find out how many players should be on each team, 
# divide the length of players by the number of teams. 
# Ex: num_players_team = len(PLAYERS) / len(TEAMS)

#Console readability matters
#Displaying the stats
    #team's name as a string
    #total players on that team as an integer
    #player names as strings seperated by commas



