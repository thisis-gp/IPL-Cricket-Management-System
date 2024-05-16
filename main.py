from player import Player
from team import Team
from auction import Auction
from schedule import Schedule
import random


# Load teams data from file
def load_teams_data(file_path):
    teams = []
    with open(file_path, 'r') as file:
        for line in file:
            name, owner = line.strip().split(',')
            teams.append(Team(name, owner, None))
    return teams


# Load players data from file
def load_players_data(file_path):
    players = []
    with open(file_path, 'r') as file:
        for line in file:
            name, role, price = line.strip().split(',')
            players.append(Player(name, role, int(price)))
    return players


try:
    # Load teams and players data
    teams = load_teams_data('teams_data.txt')
    players = load_players_data('players_data.txt')

    # Create an instance of Auction and perform auction
    auction = Auction(players, teams)
    auction.start_auction()

    # Assign captains randomly for each team
    for team in teams:
        captain = random.choice(team.players)
        team.assign_captain(captain)

    # Display team details
    for team in teams:
        team.display_details()

    # Generate and display schedule
    schedule = Schedule(teams)
    schedule.generate_schedule()
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Program Completed")
