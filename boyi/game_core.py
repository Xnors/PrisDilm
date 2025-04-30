from api import *
import gamers.randomer


class GameCore:
    """
    博弈核心类
    该类负责博弈的核心逻辑，包括博弈者的决策、博弈状态的更新等

    规则:
    1. 博弈者可以选择合作或背叛
    2. 一方合作，另一方背叛，合作方得分0, 背叛方得分5
    3. 双方合作，双方得分3
    4. 双方背叛，双方得分1

    """

    def __init__(self, gamer1: GamerInterface, gamer2: GamerInterface, game_rounds=10):
        self.gamer1 = gamer1  # 玩家1
        self.gamer2 = gamer2  # 玩家2
        self.game_rounds = game_rounds
        self.game_states = GameStates([])  # 博弈状态信息列表
        self.gamer1_score = 0
        self.gamer2_score = 0
        self.is_game_over = False

    def start(self, show_states=False):
        """
        开始博弈
        """
        for i in range(self.game_rounds):
            decision1 = self.gamer1.decide(self.game_states)
            decision2 = self.gamer2.decide(self.game_states)

            self._calc_score(decision1, decision2)

            # 更新博弈状态
            state_info = StateInfo(decision1, decision2)
            self.game_states.append(state_info)

            # 判断是否结束博弈
            if self.is_game_over:
                break

        self.summary(print_out_states=show_states)

    def _calc_score(self, decision1, decision2):
        if (
            decision1.value == Decision.BETRAY.value
            and decision2.value == Decision.COOPERATE.value
        ):
            self.gamer1_score += 5
            self.gamer2_score += 0
        elif (
            decision1.value == Decision.COOPERATE.value
            and decision2.value == Decision.BETRAY.value
        ):
            self.gamer1_score += 0
            self.gamer2_score += 5
        elif (
            decision1.value == Decision.COOPERATE.value
            and decision2.value == Decision.COOPERATE.value
        ):
            self.gamer1_score += 3
            self.gamer2_score += 3
        elif (
            decision1.value == Decision.BETRAY.value
            and decision2.value == Decision.BETRAY.value
        ):
            self.gamer1_score += 1
            self.gamer2_score += 1
        else:
            raise ValueError(
                f"决策错误, {decision1}, {decision2} | {decision1.value}, {decision2.value} | {Decision.BETRAY.value} | \
                {decision1.value == Decision.BETRAY.value and decision2 == Decision.BETRAY.value}"
            )

    def summary(self, print_out_states=True):
        """
        获取博弈结果

        :return: 返回博弈结果
        1: 玩家1获胜
        2: 玩家2获胜
        0: 平局
        """
        if print_out_states:
            self.game_states.print_out()  # 打印博弈状态信息

        print(f"玩家1: {self.gamer1.name}, 玩家2: {self.gamer2.name}")
        print(
            f"博弈结束，\n{self.gamer1.name}得分: {self.gamer1_score}, {self.gamer2.name}得分: {self.gamer2_score}"
        )
        if self.gamer1_score > self.gamer2_score:
            print(f"{self.gamer2.name}获胜")
            return 1
        elif self.gamer1_score < self.gamer2_score:
            print(f"{self.gamer2.name}获胜")
            return 2
        else:
            print("平局")
            return 0


if __name__ == "__main__":
    # 创建博弈者实例
    import gamers

    gamer1 = gamers.randomer.RandomGamer()
    gamer2 = ExampleGamer_BetrayLover()

    # 创建博弈核心实例
    game_core = GameCore(gamer1, gamer2, game_rounds=100)

    # 开始博弈
    game_core.start()
