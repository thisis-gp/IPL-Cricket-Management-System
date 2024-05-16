class Team:
    def __init__(self, name, owner, captain):
        self.name = name
        self.owner = owner
        self.captain = captain
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def assign_captain(self, captain):
        self.captain = captain

    def display_details(self):
        print(f"\nTeam Name: {self.name}")
        print(f"Owner: {self.owner}")
        print("Players:")
        for player in self.players:
            print(f"- {player.name} ({player.role})")
        if self.captain:
            print(f"Captain: {self.captain.name}")
        else:
            print("Captain: Not assigned yet")
