from .randomer import RandomGamer
from .tit_for_tat import TitForTat
from .examples import ExampleGamer_BetrayLover, ExampleGamer_CooperationLover

all_gamers = [
    RandomGamer(),
    TitForTat(),
    ExampleGamer_BetrayLover(),
    ExampleGamer_CooperationLover(),
]
