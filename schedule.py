class Schedule:
    def __init__(self, teams):
        self.teams = teams

    def generate_schedule(self):
        group1 = self.teams[:len(self.teams) // 2]
        group2 = self.teams[len(self.teams) // 2:]

        print("\nGroup 1 Matches:")
        for i in range(len(group1)):
            for j in range(i + 1, len(group1)):
                print(f"{group1[i].name} vs {group1[j].name}")

        print("\nGroup 2 Matches:")
        for i in range(len(group2)):
            for j in range(i + 1, len(group2)):
                print(f"{group2[i].name} vs {group2[j].name}")