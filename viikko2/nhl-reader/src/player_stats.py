class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        finnish = filter(lambda player: player.nationality == nationality, self.players)

        sort_list = sorted(finnish, key=lambda player: player.points, reverse=True)
        return sort_list
