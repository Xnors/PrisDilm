from prisdilm.api import *
import random


class RandomGamer(GamerInterface):
    """
    随机博弈者类，继承自GamerInterface, 随机返回合作或背叛
    """

    def __init__(self, name="Random"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        """
        随机决策函数，随机返回合作或背叛
        :param game_state: 当前博弈状态
        :return: 博弈者的决策
        """
        return random.choice([Decision.COOPERATE, Decision.BETRAY])
