import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_search_nonexistent_player(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_team_players(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertTrue(all(player.team == "EDM" for player in players))

    def test_team_no_players(self):
        players = self.stats.team("BOS")
        self.assertEqual(len(players), 0)

    def test_top_by_points(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  
        self.assertEqual(top_players[1].name, "Lemieux")  
        self.assertEqual(top_players[2].name, "Yzerman")  

    def test_top_by_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")  
        self.assertEqual(top_players[1].name, "Yzerman")  
        self.assertEqual(top_players[2].name, "Kurri")    

    def test_top_by_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  
        self.assertEqual(top_players[1].name, "Yzerman")  
        self.assertEqual(top_players[2].name, "Lemieux") 

if __name__ == "__main__":
    unittest.main()
