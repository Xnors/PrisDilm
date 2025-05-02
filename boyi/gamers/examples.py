from boyi.api import *


class ExampleGamer_CooperationLover(GamerInterface):
    """
    示例博弈者类，继承自GamerInterface, 简单返回合作
    """

    def __init__(self, name="CooperationLover"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        """
        示例决策函数，简单返回合作
        :param game_state: 当前博弈状态
        :return: 博弈者的决策
        """
        return Decision.COOPERATE


class ExampleGamer_BetrayLover(GamerInterface):
    """
    示例博弈者类，继承自GamerInterface, 简单返回背叛
    """

    def __init__(self, name="BetrayLover"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        """
        示例决策函数，简单返回背叛
        :param game_state: 当前博弈状态
        :return: 博弈者的决策
        """
        return Decision.BETRAY
