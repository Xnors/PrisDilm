from .randomer import RandomGamer
from .tit_for_tat import TitForTat
from .examples import ExampleGamer_BetrayLover, ExampleGamer_CooperationLover
from .predictive import Predictive
from .two_for_one import TwoForOne, TwoForOne_ButLoveBetray

all_gamers = [
    RandomGamer(),
    TitForTat(),
    TwoForOne(),
    TwoForOne_ButLoveBetray(),
    # ExampleGamer_BetrayLover(), # 过于极端, 影响测试结果
    # ExampleGamer_CooperationLover(),  # 它太老实了, 不能总是欺负老实人对吧 (doge
    Predictive(),
]
