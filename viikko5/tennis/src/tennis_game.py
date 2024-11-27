class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_tied_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_endgame_score()
        else:
            return self.get_running_score()
                
    def get_tied_score(self):
        if self.m_score1 < 3:
            return f"{self.get_point_name(self.m_score1)}-All"
        return "Deuce"
        
    def get_endgame_score(self):
        score_difference = self.m_score1 - self.m_score2
        if abs(score_difference) == 1:
            leading_player = self.player1_name if score_difference > 0 else self.player2_name
            return f"Advantage {leading_player}"
        winner = self.player1_name if score_difference > 0 else self.player2_name
        return f"Win for {winner}"

    def get_running_score(self):
        self.m_score1 = self.get_point_name(self.m_score1)
        self.m_score2 = self.get_point_name(self.m_score2)
        return f"{self.m_score1}-{self.m_score2}"
                    
    def get_point_name(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
            
