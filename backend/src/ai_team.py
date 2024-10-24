class AITeam:
    def __init__(self):
        self.team_members = []

    def add_member(self, member):
        self.team_members.append(member)

    def get_team_size(self):
        return len(self.team_members)

    # Add more methods as needed for your AI team functionality
