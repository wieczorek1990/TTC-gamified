from ttc import games, game, exceptions, scenes


class Main:
    def __init__(self, scene_class, game_class):
        self.scene_class = scene_class
        self.game_class = game_class

    def main(self):
        try:
            game.main(self.scene_class, self.game_class)
        except exceptions.GameException:
            pass


class PrintingMain(Main):
    def main(self):
        print("Press CMD+W to quit.")
        super().main()
        print("Exited successfully.")
