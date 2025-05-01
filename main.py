from boyi import gamers, game_core, api


def main():
    gamer1 = gamers.randomer.RandomGamer()
    gamer2 = api.ExampleGamer_BetrayLover()
    gamer3 = gamers.tit_for_tat.TitForTat()

    # 创建博弈核心实例
    gc = game_core.GameCore(gamer3, gamer1, game_rounds=100)

    # 开始博弈
    gc.start(show_states=True)


if __name__ == "__main__":
    main()
