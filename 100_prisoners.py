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
    #         # num_victories += PrisionersGame.victory(game.play(approach

    #     print('{:15}: {:5} ({:.2%})'.format(
    #         approach.__name__, num_victories, num_victories / NUM_REPETITIONS))
        

class PrisionersGame:
    pass

@classmethod
def victory(csl, results):
    """Defines a victory of a game: all players won"""
    return all(results)

    approaches = [play_naive, play_naive_mem, play_optimum]

def play(self, approach):
    """Plays this game and returns a list of booleans with
    True if a player one, False otherwise"""
    return [approach(self, player) for player in self.drawer_ids]

if __name__ == '__main__':
    main()

