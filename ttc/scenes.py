from ttc import game


class PrintingScene(game.Scene):
    def __init__(self, screen):
        print("Initializing TTCScene...")
        super().__init__(screen)
        print("Post initialization of TTCScene...")


class TTCScene(PrintingScene):
    pass
