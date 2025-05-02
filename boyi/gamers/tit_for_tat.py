from boyi.api import *


class TitForTat(GamerInterface):
    """
    以牙还牙博弈者类，继承自GamerInterface

    该博弈者在第一次博弈中选择合作，之后的每次博弈都选择与对方上次的决策相同的策略
    """

    def __init__(self, name="TitForTat"):
        super().__init__(name)

    def decide(self, game_states, whoami) -> Decision:
        if len(game_states.state_info) == 0:
            # 第一次博弈，选择合作
            return Decision.COOPERATE
        if whoami == WhoAmI.GAMER1:
            last_deci = game_states.state_info[-1].p2
            return last_deci
        else:
            last_deci = game_states.state_info[-1].p1
            return last_deci
