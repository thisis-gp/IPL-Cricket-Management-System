class Auction:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams
        self.remaining_players = players.copy()

    def start_auction(self):
        while self.remaining_players:
            for team in self.teams:
                print(f"\n{team.name}'s turn to bid.")

                # Display remaining players
                print("Remaining players:")
                for idx, player in enumerate(self.remaining_players, start=1):
                    print(f"{idx}. {player.name} - {player.price}")

                # Prompt for player selection
                player_choice = int(input("Enter the number of the player you want to bid for (0 to pass): "))
                if player_choice == 0:
                    print("Passing the bid.")
                    continue

                # Get the selected player
                selected_player = self.remaining_players[player_choice - 1]

                # Perform bidding
                bid_amount = int(input("Enter your bid amount: "))
                if bid_amount > selected_player.price:
                    # Allocate player to the team
                    team.add_player(selected_player)
                    print(f"You won the bid for {selected_player.name} with a bid of {bid_amount}.")
                    self.remaining_players.remove(selected_player)
                else:
                    print("Your bid was not successful. Try again.")

                # Check if each team has reached the maximum player limit
                if all(len(team.players) >= 5 for team in self.teams):
                    print("Maximum player limit reached for all teams.")
                    return
