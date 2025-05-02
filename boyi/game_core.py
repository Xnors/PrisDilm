from .api import *
from .gamers import randomer
from .gamers import tit_for_tat
from itertools import product


class SingleGameCore:
    """
    博弈核心类
    该类负责博弈的核心逻辑，包括博弈者的决策、博弈状态的更新等

    规则:
    1. 博弈者可以选择合作或背叛
    2. 一方合作，另一方背叛，合作方得分0, 背叛方得分5
    3. 双方合作，双方得分3
    4. 双方背叛，双方得分1

    """

    def __init__(
        self,
        gamer1: GamerInterface,
        gamer2: GamerInterface,
        game_rounds=10,
    ):
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

        返回:
        return {
            "gamer1_score": self.gamer1_score,
            "gamer2_score": self.gamer2_score,
            "stat" : win_fail_signal
        }
        """
        for i in range(self.game_rounds):
            decision1 = self.gamer1.decide(self.game_states, whoami=WhoAmI.GAMER1)
            decision2 = self.gamer2.decide(self.game_states, whoami=WhoAmI.GAMER2)

            self._calc_score(decision1, decision2)

            # 更新博弈状态
            state_info = StateInfo(decision1, decision2)
            self.game_states.append(state_info)

            # 判断是否结束博弈
            if self.is_game_over:
                break

        win_fail_signal = self.summary(print_out_states=show_states)

        return {
            "gamer1_score": self.gamer1_score,
            "gamer2_score": self.gamer2_score,
            "stat": win_fail_signal,
        }

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

        def output_when_could(s, *args, **kwargs):
            if print_out_states:
                print(s, *args, **kwargs)

        if print_out_states:
            self.game_states.print_out()  # 打印博弈状态信息

            output_when_could(f"玩家1: {self.gamer1.name}, 玩家2: {self.gamer2.name}")
            output_when_could(
                f"博弈结束，\n{self.gamer1.name}得分: {self.gamer1_score}, {self.gamer2.name}得分: {self.gamer2_score}"
            )
        if self.gamer1_score > self.gamer2_score:
            output_when_could(f"{self.gamer1.name}获胜")
            return 1
        elif self.gamer1_score < self.gamer2_score:
            output_when_could(f"{self.gamer2.name}获胜")
            return 2
        else:
            output_when_could("平局")
            return 0


class GameCore:
    """
    所有博弈策略竞技场

    让所有博弈方互相博弈
    """

    def __init__(self, gamers_list: list[GamerInterface], every_game_rounds=10):
        self.gamers_list = gamers_list
        self.every_game_rounds = every_game_rounds
        self.results: list[dict[str, int]] = []

    def start(self):
        games_iter = product(self.gamers_list, repeat=2)

        for i in games_iter:
            gamer1, gamer2 = i
            game_core = SingleGameCore(
                gamer1, gamer2, game_rounds=self.every_game_rounds
            )
            result: dict[str, int] = game_core.start(show_states=False)
            self.results.append(result)
            print(
                f"博弈者: {gamer1.name} vs {gamer2.name}, 结果: {result['stat']}, {gamer1.name}得分: {result['gamer1_score']}, {gamer2.name}得分: {result['gamer2_score']}"
            )

        return self.results

    def plot(self):
        """
        画出博弈结果, 热力图和柱状图, 使用灰度图像, 不要用 numpy, 并将两者画在同一张图中
        """
        print(self.results)
        import matplotlib.pyplot as plt

        # 计算博弈结果
        results = self.results
        gamers_num = len(self.gamers_list)
        score_matrix = [[0 for _ in range(gamers_num)] for _ in range(gamers_num)]

        # 填充 score_matrix
        for k, result in enumerate(results):
            gamer1, gamer2 = list(product(self.gamers_list, repeat=2))[k]
            i = self.gamers_list.index(gamer1)
            j = self.gamers_list.index(gamer2)
            score_matrix[i][j] = result["gamer1_score"]

        # 创建画布
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # 画出灰度热力图
        im = ax1.imshow(score_matrix, cmap="gray", interpolation="nearest")
        ax1.set_title("RESULTS (Heatmap)")
        ax1.set_xticks(range(gamers_num))
        ax1.set_yticks(range(gamers_num))
        ax1.set_xticklabels([g.name for g in self.gamers_list], rotation=15)
        ax1.set_yticklabels([g.name for g in self.gamers_list])

        # 在色块上添加数字
        for i in range(gamers_num):
            for j in range(gamers_num):
                ax1.text(
                    j,
                    i,
                    f"{score_matrix[i][j]}",
                    ha="center",
                    va="center",
                    color=(
                        "yellow"
                        if score_matrix[i][j] < (self.every_game_rounds * 2.5)
                        else "black"
                    ),
                )

        fig.colorbar(im, ax=ax1)

        # 计算每种策略的总得分
        total_scores = {g.name: 0 for g in self.gamers_list}
        for k, result in enumerate(results):
            gamer1, gamer2 = list(product(self.gamers_list, repeat=2))[k]
            total_scores[gamer1.name] += result["gamer1_score"]
            total_scores[gamer2.name] += result["gamer2_score"]

        # 按总得分排序
        sorted_scores = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)

        # 画柱状图
        ax2.bar([x[0] for x in sorted_scores], [x[1] for x in sorted_scores], color="skyblue")
        ax2.set_xlabel("Strategies")
        ax2.set_ylabel("Total Scores")
        ax2.set_title("Total Scores by Strategy")
        ax2.set_xticks(range(len(sorted_scores)))
        ax2.set_xticklabels([x[0] for x in sorted_scores], rotation=15)

        # 显示图表
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # 创建博弈者实例
    import gamers

    gamer1 = gamers.randomer.RandomGamer()
    gamer3 = gamers.tit_for_tat.TitForTat()

    # 创建博弈核心实例
    game_core = SingleGameCore(gamer3, gamer1, game_rounds=100)

    # 开始博弈
    game_core.start()
