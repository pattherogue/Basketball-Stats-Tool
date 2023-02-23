#Proper use of Dunder Main
#Import player and team data
    #import from constants.py
    #should not be hard coded into script
    #changes should be reflected

from constants import TEAMS, PLAYERS
import sys


# Create a clean_data function
def clean_data():
    # read existing player data from PLAYERS im constants.py
    # clean player data w/o changing original data
    cleaned = []
    for player in PLAYERS:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians']
        #save new collection
        #height -- saved as an integer
        fixed['height'] = int(player['height'].split(" ")[0])
        #experience -- saved as a boolean value (True or False)
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else: 
            fixed['experience'] = False
    
    cleaned.append(fixed)
    #data returned cleaned
    return cleaned

# Create balance_teams function
def balance_teams(cleaned):
# Balance players across three teams: Panthers, Bandits, and  Warriors
    team_panthers = []
    team_bandits = []
    team_warriors = []
# Organize teams based on experienced vs inexperienced players 
    experienced_player = []
    inexperienced_player = []
# New team created to not mess with origials 
    new_teams = [team_panthers, team_bandits, team_warriors]
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
        for team in new_teams:
            try: 
            # append to correct list
                team.append(inexperienced_player.pop(0))
            except IndexError:
                break
    return new_teams
# goal   

if __name__ == "__main__":
    clean_data()
    balance_teams(clean_data())
#Console readability matters
#Display in nice readable format

#Displaying the stats
    #team's name as a string
    #total players on that team as an integer
    #player names as strings seperated by commas


# FORMAT OF BASKETBALL STATS TOOL

# Beginning Of Main Display 

# Title BASKETBALL TEAM STATS TOOL
print("\n")
print("BASKETBALL TEAM STATS TOOL")
while True:
    # ---- MENU ----
    print("\n---MENU---\n")
    # Here are your choices: 
    print("Here are your choices: \nA) Display Team Stats \nB) Quit" )
    # A) Display Team Stats
    # B) Quit 
    print("\n")
    while True: 
        # Enter an option: A
        option = raw_input("Enter an option A or B: ")
        if option.upper() == 'A':
            print("""
            Please choose a team: 
                A) Panthers
                B) Bandits
                C) Warriors
            """)
           
            break
        elif option.upper() == 'B':
            print('\nEnd of Basketball Stats Tool')
            break
        else:
            print("Invalid response. Please choose 'A' or 'B")
            continue
   
# End of Main Display


#Start of Second Display
    while True:
        choose_team = raw_input('\n\nSelect a team by choosing a letter: ')
        if choose_team.upper() == 'A':
            #storage for filtered players from prev. balance + clean funtions
            team_panthers = balance_teams(clean_data())[0]
            #gather total players from filtered (balance + clean functions)
            total_players = len(team_panthers)
            #list number of players on team (seperated by comma)
            display_team_members = team_panthers.split()
            print("""
                #Team: Panther Stats
                #--------------------
                #Total players: {total_players}

                #Players on Team: {display_team_members}
            """)
            break
        elif choose_team.upper() == 'B':
            team_bandits = balance_teams(clean_data())[1]
            total_players = len(team_bandits)
            display_team_members = ', '.join(team_bandits)
            print("""
                #Team: Bandit Stats
                #--------------------
                #Total players: {total_players}

                #Players on Team: {display_team_members}
            """)
            break
        elif choose_team.upper() == 'C':
            team_warriors = balance_teams(clean_data())[1]
            total_players = len(team_warriors)
            display_team_members = ', '.join(team_warriors)
            print("""
                #Team: Bandit Stats
                #--------------------
                #Total players: {total_players}

                #Players on Team: {display_team_members}
            """)
            break
        else:
            print("Invalid response. Please try again.")
            continue

# Team Panthers
# Team Bandits
# Team Warriors

# Need to show
    #Team Name (as string)
        #print(Team Name)
    #Team Total Players (as integer)
        #total_players = len(team)
    #List players of selected team (string seperated by comma)
        #list_players = team.split()





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