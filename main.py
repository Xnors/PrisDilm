from prisdilm import gamers, game_core


def main():
    gc = game_core.GameCore(gamers_list=gamers.all_gamers, every_game_rounds=100)

    # 开始博弈
    gc.start()
    gc.plot()

    # gc2 = game_core.SingleGameCore(
    #     gamer1=gamers.ExampleGamer_BetrayLover(), gamer2=gamers.TitForTat(), game_rounds=20
    # )
    # gc2.start()
    # gc2.summary()


if __name__ == "__main__":
    main()
