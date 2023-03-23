#Proper use of Dunder Main
#Import player and team data
    #import from constants.py
    #should not be hard coded into script
    #changes should be reflected

from constants import TEAMS, PLAYERS
import sys
import random

# Create a clean_data function(ORGANIZE)
def clean_data(players):
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
        if player['experience'] == 'Yes':
            fixed['experience'] = True
        else: 
            fixed['experience'] = False
    
        cleaned.append(fixed)
    #data returned cleaned
    return cleaned

# Create balance_teams function
def balance_teams(players):
    # Balance players across three teams: Panthers, Bandits, and  Warriors
    # calculates number of players per team 
    # HINT: To find out how many players should be on each team, 
    # divide the length of players by the number of teams. 
    num_teams = len(TEAMS)
    num_players_per_team = len(players) // num_teams
    # Organize teams based on experienced vs inexperienced players 
    experienced_players = [player for player in players if player['experience']]
    inexperienced_players = [player for player in players if not player['experience']]
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

if __name__ == "__main__":
    players = clean_data(PLAYERS)
    teams = balance_teams(players)

    #Displaying the stats
    #team's name as a string
    #total players on that team as an integer
    #player names as strings seperated by commas

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

    while True:
        option = input("\nEnter an option: ").strip().lower()
        if option == 'a':
            print("\nA) Panthers\nB) Bandits\nC) Warriors")
            team_option = input("Enter an option: ").strip().lower()
            if team_option in ["a", "b", "c"]:
                team_name = {'a': 'Panthers', 'b': 'Bandits', 'c': 'Warriors'}[team_option]
                player_list = teams[team_name]
                print(f"\nTeam: {team_name} Stats")
                print("--------------------")
                print(f"Total players: {len(player_list)}\n")
                print("Players on Team:")
                player_names = [player['name'] for player in player_list]
                player_names_str = ", ".join(player_names)
                print(f"  {player_names_str}")
                input("\nPress ENTER to continue...")
            else:
                print("Invalid option. Please try again.")         
        elif option == 'b':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")
