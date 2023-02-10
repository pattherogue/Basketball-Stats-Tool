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
# New team created to not mess with origials 
    new_teams = []
# functions, packing, and unpacking
    for fixed in cleaned:
        if fixed['experience'] == True:
            experienced_player.append(fixed)
        elif fixed['experience'] == False:
            inexperienced_player.append(fixed)

# HINT: To find out how many players should be on each team, 
# divide the length of players by the number of teams. 
# len, min, max
# loops over players to check experience property value
    while len(experienced_player) >= 1:
        for team in new_teams:
            try:
            # append to correct list
                team.append(experienced_player.pop(0))
            except IndexError:
                break
    while len(inexperienced_player) >= 1:
        for team in teams:
            try: 
            # append to correct list
                team.append(inexperienced_player.pop(0))
            except IndexError:
                break
    return new_teams
# goal   

#Console readability matters
#Display in nice readable format

#Displaying the stats
    #team's name as a string
    #total players on that team as an integer
    #player names as strings seperated by commas


# FORMAT OF BASKETBALL STATS TOOL

# Beginning Of Main Display 
def basketballStatsTool():
    # Title BASKETBALL TEAM STATS TOOL
    print("BASKETBALL TEAM STATS TOOL")
    print("\n")
    print("---- Menu ----")
    # ---- MENU ----

    # Here are your choices: 

    # A) Display Team Stats
    # B) Quit 

    # Enter an option: A

# End of Main Display

#Start of Second Display

    # A) Panthers
    # B) Bandits
    # C) Warriors

    # Enter an option: A

# End of Second Display 

# Start of Third Display

    # Team: Panther Stats

    # ---------------------

    # Total players: 6

    # Players on Team: 
        # (Plaayer 1, Player 2, ... )

    # Press ENTER to continue...

# End of This Display 