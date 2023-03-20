#Proper use of Dunder Main
#Import player and team data
    #import from constants.py
    #should not be hard coded into script
    #changes should be reflected

from constants import TEAMS, PLAYERS
import sys
import random




# Create a clean_data function(ORGANIZE)
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
    # calculates number of players per team 
    # HINT: To find out how many players should be on each team, 
    # divide the length of players by the number of teams. 
    num_players_per_team = len(cleaned) // len(TEAMS)
    # Organize teams based on experienced vs inexperienced players 
    experienced_players = [player for player in cleaned if player['experience']]
    inexperienced_players = [player for player in cleaned if not player['experience']]
    # shuffles the two lists randomly 
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)
    # empty dictionary of teams -- each team name as the key
    teams = {team: [] for team in TEAMS}
    # loops over the teams
    for team in teams:
        num_experienced_players = 0
        # adds players to each team
        # until the team has reached the desired number of players
        while len(teams[team]) < num_players_per_team:
            if experienced_players and (num_experienced_players < num_players_per_team // 2):
                player = experienced_players.pop()
                num_experienced_players += 1
            else:
                player = inexperienced_players.pop()
            teams[team].append(player)
        # return dictionary of teams w/ assinged players
    return teams


# New team created to not mess with origials 
    
# functions, packing, and unpacking
  


# len, min, max
# loops over players to check experience property value
    
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
print("BASKETBALL TEAM STATS TOOL\n")
# ---- MENU ----
print("---- MENU----\n")
# Here are your choices: 
# A) Display Team Stats
# B) Quit
print(" Here are your choices:")
print("  A) Display Team Stats")
print("  B) Quit")

option = input("\nEnter an option: ")

if option == "A":
    print("\nA) Panthers\nB) Bandits\nC) Warriors")
    team_option = input("\nEnter an option: ")

    if team_option == "A":
        team_name = "Panthers"
        #storage for filtered players from prev. balance + clean funtions
        player_list = balance_teams(clean_data())[0]

    elif team_option == "B":
        team_name = "Bandits"
        #storage for filtered players from prev. balance + clean funtions
        player_list = balance_teams(clean_data())[1]

    elif team_option == "C":
        team_name = "Warriors"
        #storage for filtered players from prev. balance + clean funtions
        player_list = balance_teams(clean_data())[2]
    
     else:
        print("Invalid option. Please try again.")
        sys.exit()

    print(f"\nTeam: {team_name} Stats")
    print("--------------------")
    print(f"Total players: {len(player_list.split(', '))}\n")
    print("Players on Team:")
    print(f"  {player_list}")
    input("\nPress ENTER to continue...")
    
elif option == "B":
    print("Goodbye!")
    
else:
    print("Invalid option. Please try again.")
# End of Main Display
#Start of Second Display

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