from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple


# 博弈决策枚举(合作/背叛)
class Decision(Enum):
    COOPERATE = auto()  # 合作
    BETRAY = auto()  # 背叛

    def __str__(self):
        return f"决策({self.name})"


class StateInfo(namedtuple("StateInfo", ["s", "p"])):
    """
    博弈状态信息类, 包含双方决策信息
    s: 自己的决策
    p: 对方的决策
    """

    s: Decision  # 自己的决策
    p: Decision  # 对方的决策

    def __str__(self):
        return f"状态({self.s}, {self.p})"


class GameStates:
    """
    博弈状态类, 包含曾经的所有双方决策信息
    """

    def __init__(self, state_info: list[StateInfo] | None = None):
        if state_info is None:
            state_info = []
        self.state_info = state_info  # 博弈状态信息

    def __str__(self):
        s = ""
        for i in self.state_info:
            s += str(i) + ","
        return f"博弈状态({s})"

    def print_out(self):
        """
        打印博弈状态信息
        """
        print("历次博弈状态信息如下:")
        for i in self.state_info:
            print(i)

    def append(self, state_info: StateInfo):
        """
        添加博弈状态信息
        :param state_info: 博弈状态信息
        """
        self.state_info.append(state_info)


class GamerInterface(ABC):
    """
    博弈者的接口类
    """

    def __init__(self, name):
        self.name = name  # 博弈者名称

    @abstractmethod
    def decide(self, game_states: GameStates) -> Decision:
        """
        决策函数，返回博弈者的决策
        :param game_state: 当前博弈状态
        :return: 博弈者的决策
        """
        pass


if __name__ == "__main__":
    # 测试决策枚举
    print(Decision.COOPERATE)  # 输出: Decision(COOPERATE)
    print(Decision.BETRAY)  # 输出: Decision(BETRAY)

    # 测试博弈状态信息类
    state_info = StateInfo(Decision.COOPERATE, Decision.BETRAY)
    print(state_info)  # 输出: 博弈状态信息(Decision(COOPERATE), Decision(BETRAY))

    gs = GameStates([state_info, state_info])
    gs.print_out()
