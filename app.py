#Proper use of Dunder Main
#Import player and team data
    #import from constants.py
    #should not be hard coded into script
    #changes should be reflected

from constants import TEAMS, PLAYERS

#Create a clean_data function
def clean_data(data):
    cleaned = []
    for user in data:
        fixed = {}
        fixed["email"] = user["email"]
        fixed["first_name"] = user["name"].split(" ")[0]

    #read existing player data from PLAYERS im constants.py
    #clean player data w/o changing original data
    #save new collection
        #height -- saved as an integer
        #experience -- saved as a boolean value (True or False)

#Create balance_teams function
#Console readability matters
#Displaying the stats
    #team's name as a string
    #total players on that team as an integer
    #player names as strings seperated by commas
