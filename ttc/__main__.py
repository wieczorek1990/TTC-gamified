import os

from ttc import mains, scenes, games, game, cli

if __name__ == "__main__":
    if cli.debug:
        main_class = mains.PrintingMain
        scene_class = scenes.PrintingScene
        game_class = games.PrintingGame
    else:
        main_class = mains.Main
        scene_class = game.Scene
        game_class = game.Game

    # Entrypoint here.
    main_class(scene_class, game_class).main()
