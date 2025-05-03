from prisdilm import gamers, game_core


def main():
    gc = game_core.GameCore(gamers_list=gamers.all_gamers, every_game_rounds=100)

    # 开始博弈
    gc.start()
    gc.plot()


if __name__ == "__main__":
    main()
