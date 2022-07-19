from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []


    def add_player(self, player: Player):
        for team_player in self.__players:
            if team_player.name == player.name:
                return f"Player {self.__name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for team_player in self.__players:
            if team_player.name == player_name:
                self.__players.remove(team_player)
                return team_player
        return f"Player {player_name} not found"


