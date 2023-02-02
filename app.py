#Proper use of Dunder Main
#Import player and team data
    #import from constants.py
    #should not be hard coded into script
    #changes should be reflected

from constants import TEAMS, PLAYERS

#Create a clean_data function
def clean_data(data):
    #read existing player data from PLAYERS im constants.py
    #clean player data w/o changing original data
    cleaned = []
    for player in PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["gaurdians"] = player["gaurdians"]
        #save new collection
        #height -- saved as an integer
        height = int(player['height'].split(" ")[0])
        
    return cleaned


  
        #experience -- saved as a boolean value (True or False)

#Create balance_teams function
#Console readability matters
#Displaying the stats
    #team's name as a string
    #total players on that team as an integer
    #player names as strings seperated by commas
