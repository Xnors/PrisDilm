from prisdilm.api import *


class Predictive(GamerInterface):
    """
    概率型策略, 根据对手在以往的博弈经验预测对手更倾向于采取什么策略
    第一次博弈选择合作，之后根据对手的背叛的概率选择背叛或者合作
    """

    def __init__(self, name="Predictive"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        length = len(game_states)

        if length == 0:
            return Decision.COOPERATE

        # 计算对手背叛的概率
        betray_count = 0
        for state in game_states:
            od = state.get_other_decision(whoami)
            if od == Decision.BETRAY:
                betray_count += 1

        # 根据对手背叛的概率选择合作或者背叛
        if (betray_count / length) <= 0.5:
            return Decision.COOPERATE
        else:
            return Decision.BETRAY
