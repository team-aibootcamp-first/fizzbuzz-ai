import random

def main():
    NUM_DRAWERS = 10
    NUM_REPETITIONS = int(1E5)

    print('{:15}: {:5} ({})'.format('approach', 'wins', 'ratio'))
    
    # 클래스 구현 후 주석 해제
    # for approach in PrisionersGame.approaches:
    #     num_victories = 0
    #     for _ in range(NUM_REPETITIONS):
    #         game = PrisionersGame(NUM_DRAWERS)
    #         
    #         # num_victories += PrisionersGame.victory(game.play(approach))

    #     print('{:15}: {:5} ({:.2%})'.format(
    #         approach.__name__, num_victories, num_victories / NUM_REPETITIONS))
        

class PrisionersGame:
    pass
        
if __name__ == '__main__':
    main()

    # 작업추가(김회수)
    def play_optimum(self, player_number):
        """ Open the drawer that matches the player number and then open the drawer
        with the revealed number.
        """
        prev_attempt = player_number
        for attempt in range(self.max_attempts):
            if self.drawers[prev_attempt] == player_number:
                return True
            else:
                prev_attempt = self.drawers[prev_attempt]

        return False
