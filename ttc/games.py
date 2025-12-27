from ttc import game


class PrintingGame(game.Game):
    def __init__(self, scene):
        print("Initializing TTCGame...")
        super().__init__(scene)
        print("Post initialization of TTCGame...")


class TTCGame(PrintingGame):
    pass
