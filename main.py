from boyi import gamers, game_core, api


def main():
    gamer1 = gamers.RandomGamer()
    gamer2 = gamers.ExampleGamer_BetrayLover()
    gamer3 = gamers.TitForTat()

    print(f"{gamer1.name}, {gamer2.name}, {gamer3.name}")
    # 创建博弈核心实例
    gc = game_core.GameCore(gamer3, gamer1, game_rounds=10)

    # 开始博弈
    gc.start(show_states=True)


if __name__ == "__main__":
    main()
