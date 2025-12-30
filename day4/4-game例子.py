class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("This is a good game")

    @classmethod
    def show_top_score(cls):
        print(f'目前游戏最高分为{cls.top_score}')

    def start_game(self):
        print("Welcome to this game")
        Game.show_help()
        sscore = int(input("please input your ideal score"))
        if sscore > Game.top_score:
            Game.top_score = sscore
        Game.show_top_score()


if __name__ == '__main__':
    player1 = Game("Player 1")
    player2 = Game("Player 2")
    player1.start_game()
    player2.start_game()
    # Game.show_top_score()