from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple


# 博弈决策枚举(合作/背叛)
class Decision(Enum):
    COOPERATE = auto()  # 合作
    BETRAY = auto()  # 背叛

    def __str__(self):
        return f"决策({self.name})"


class WhoAmI(Enum):
    GAMER1 = auto()  # 博弈者1
    GAMER2 = auto()  # 博弈者2

    def __str__(self):
        return f"我方为({self.name})"


class StateInfo(namedtuple("StateInfo", ["p1", "p2"])):
    """
    博弈状态信息类, 包含双方决策信息
    """

    p1: Decision  # 博弈者1的决策
    p2: Decision  # 博弈者2的决策

    def __str__(self):
        return f"状态({self.p1}, {self.p2})"

    def get_own_decision(self, whoami: WhoAmI) -> Decision:
        """
        获取指定博弈者的决策
        :param whoami: 指定博弈者
        :return: 指定博弈者的决策
        """
        if whoami == WhoAmI.GAMER1:
            return self.p1
        elif whoami == WhoAmI.GAMER2:
            return self.p2
        else:
            raise ValueError("whoami参数错误")

    def get_other_decision(self, whoami: WhoAmI) -> Decision:
        """
        获取另一博弈者的决策
        :param whoami: 指定博弈者
        :return: 另一博弈者的决策
        """
        if whoami == WhoAmI.GAMER1:
            return self.p2
        elif whoami == WhoAmI.GAMER2:
            return self.p1
        else:
            raise ValueError("whoami参数错误")


class GameStates:
    """
    博弈状态类, 包含曾经的所有双方决策信息
    """

    def __init__(
        self, state_info: list[StateInfo] | None = None, states_limit: int | None = None
    ):
        """
        :param state_info: 博弈状态信息列表
        :param states_limit: 博弈状态信息的最大长度, 默认为None, 表示无限制
        """
        if state_info is None:
            state_info = []
        self.state_info: list[StateInfo] = state_info  # 博弈状态信息

        self.states_limit = states_limit  # 博弈状态信息的最大长度

    def __str__(self):
        s = ""
        for i in self.state_info:
            s += str(i) + ","
        return f"博弈状态({s})"

    def __getitem__(self, item):
        return self.state_info[item]

    def __len__(self):
        return len(self.state_info)

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
        if (self.states_limit is not None) and (
            len(self.state_info) >= self.states_limit
        ):
            self.state_info.pop(0)
        self.state_info.append(state_info)


class GamerInterface(ABC):
    """
    博弈者的接口类
    """

    def __init__(self, name):
        self.name = name  # 博弈者名称

    @abstractmethod
    def decide(self, game_states: GameStates, whoami: WhoAmI) -> Decision:
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

    gs = GameStates([state_info, state_info, state_info])

    gs.append(StateInfo(Decision.BETRAY, Decision.COOPERATE))
    gs.append(StateInfo(Decision.BETRAY, Decision.COOPERATE))
    gs.append(StateInfo(Decision.BETRAY, Decision.COOPERATE))
    gs.append(StateInfo(Decision.BETRAY, Decision.COOPERATE))
    gs.print_out()
