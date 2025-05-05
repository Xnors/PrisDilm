from prisdilm.api import *


class TwoForOne(GamerInterface):
    """
    一报还两报博弈者类，继承自GamerInterface

    该博弈者在第一次博弈中选择合作，之后只有对手连续两次选择背叛才在下一轮选择背叛
    """

    def __init__(self, name="TwoForOne"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        if len(game_states) < 2:
            # 第一次博弈，选择合作
            return Decision.COOPERATE

        last_deci = game_states[-1].get_other_decision(whoami)
        llast_deci = game_states[-2].get_other_decision(whoami)
        if last_deci == Decision.BETRAY and llast_deci == Decision.BETRAY:
            # 连续两次背叛，选择背叛
            return Decision.BETRAY
        else:
            # 其他情况，选择合作
            return Decision.COOPERATE


class TwoForOne_ButLoveBetray(GamerInterface):
    """
    一报还两报博弈者类变体

    该博弈者在第一次博弈中选择合作，之后只有对手连续两次选择背叛才在下一轮选择背叛, 但是在对手连续两次选择合作时，会选择背叛
    """

    def __init__(self, name="TwoForOne_B"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        if len(game_states) < 2:
            # 第一次博弈，选择合作
            return Decision.COOPERATE

        last_deci = game_states[-1].get_other_decision(whoami)
        llast_deci = game_states[-2].get_other_decision(whoami)
        if last_deci == Decision.BETRAY and llast_deci == Decision.BETRAY:
            # 连续两次背叛，选择背叛
            return Decision.BETRAY
        elif last_deci == Decision.COOPERATE and llast_deci == Decision.COOPERATE:
            # 连续两次合作，选择背叛
            return Decision.BETRAY
        else:
            # 其他情况，选择合作
            return Decision.COOPERATE
