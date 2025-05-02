# 开发文档

## 1. 接口 (_prisdilm\api.py_)

### 1. Decision 博弈决策 `:enum.Enum`

> 博弈方做出的决策

```python
from enum import Enum, auto

class Decision(Enum):
    COOPERATE = auto()  # 合作
    BETRAY = auto()  # 背叛
```

### 2. WhoAmI 博弈方序号 `:enum.Enum`

> 博弈方在一轮博弈中的序号 <br>
> 因为博弈方可能为 _gamer1_ 或者 _gamer2_ , 在开发过程中发现博弈者无法区分自己和对手，因此引入了序号来区分博弈者<br>
> 在博弈的时候, `Gamer` 的 `decide` 方法会接受这个参数. 详见 [GamerInterface](#5-gamerinterface-博弈者接口-abcabc)

```python
from enum import Enum, auto

class WhoAmI(Enum):
    GAMER1 = auto()  # 玩家1
    GAMER2 = auto()  # 玩家2
```

### 3. StateInfo 博弈状态 `collections.namedtuple("StateInfo", ["p1", "p2"])`

> **单次** 博弈状态信息，包括两个玩家的决策

```python
from collections import namedtuple

class StateInfo(namedtuple("StateInfo", ["p1", "p2"])):
    p1: Decision # 玩家1的决策
    p2: Decision # 玩家2的决策
```

### 4. GameStates 博弈状态序列

> 博弈状态类, 包含曾经的所有双方决策信息

```python
class GameStates:
    def __init__(self, state_info: list[StateInfo] | None = None): ...
    def print_out(self): ...
    def append(self, state_info: StateInfo): ...
```

- `print_out(self)`

  打印出当前的博弈状态序列

  示例输出格式:

  > 历次博弈状态信息如下: <br>
  > 状态(决策(COOPERATE), 决策(BETRAY))<br>
  > 状态(决策(BETRAY), 决策(COOPERATE))<br>

- `append(self, state_info: StateInfo)`

  添加博弈状态信息到博弈状态序列中

### 5. GamerInterface 博弈者接口 `abc.ABC`

> 博弈者接口, 定义博弈者的决策方法 <br>
> 任何博弈者都要继承这个接口

```python
from abc import ABC, abstractmethod

class GamerInterface(ABC):
    def __init__(self, name): ...

    @abstractmethod
    def decide(self, game_states: GameStates, whoami: WhoAmI) -> Decision: ...
```

- `decide(self, game_states: GameStates, whoami: WhoAmI) -> Decision`

  博弈者决策方法, 输入博弈状态和博弈方序号, 返回博弈决策

## 2. 博弈运行核心 (prisdilm/game_core.py)

### 1. SingleGameCore 单局游戏核心

> 单局游戏核心, 实现了博弈的核心逻辑, 包括博弈者的决策、博弈状态的更新等 <br>
> 注: 博弈规则详见 [博弈规则](../README.md#博弈规则)

```python
class SingleGameCore:
    def __init__(
        self,
        gamer1: GamerInterface,
        gamer2: GamerInterface,
        game_rounds=10,
    ): ...
    def start(self, show_states=False) -> dict[str, int]: ...
    def summary(self, print_out=True) -> Literal[1] | Literal[2] | Literal[0]: ...
```

#### 参数说明

- `gamer1` 博弈者 1
- `gamer2` 博弈者 2
- `game_rounds` 博弈轮数

#### 方法说明

- `start(self, show_states=False) -> dict[str, int]`

  开始博弈

  - `show_states` 是否打印出博弈状态序列

  - 返回格式:

    ```python
        {
            "gamer1_score": self.gamer1_score,
            "gamer2_score": self.gamer2_score,
            "stat": win_fail_signal,
        }
    ```

- `summary(self, print_out=True) -> Literal[1] | Literal[2] | Literal[0]`

  打印出博弈结果

  - `print_out` 是否打印输出结果, 若为 `False` 则只返回结果

  - 返回格式:

    ```python
        Literal[1] | Literal[2] | Literal[0]
    ```

    - `1` 玩家 1 胜利
    - `2` 玩家 2 胜利
    - `0` 平局

### 2. GameCore 所有博弈策略竞技场

> 所有博弈策略竞技场, 实现了多个博弈者之间的两两对弈, 并返回结果 <br>
> 注: 两两博弈匹配规则由 `itertools.product` 实现

```python
class GameCore:
    def __init__(self, gamers_list: list[GamerInterface], every_game_rounds=10):
        ...
        self.results: list[dict[str, int]] = []

    def start(self): ...

    def plot(self): ...
```

#### 参数说明

- `gamers_list` 博弈者列表
- `every_game_rounds` 每场比赛的轮数

#### 方法说明

- `start(self)`:

  开始所有博弈

- `plot(self)`:

  > 注: 此方法依赖 `matplotlib` 库, 若没有安装则无法使用, 安装详见: [部署说明](../README.md#安装)

  绘制所有博弈结果的统计图

  > 统计图包括热力图和柱状图
  >
  > - 热力图: 展示每场博弈的胜负情况, 左边为玩家一,它所在的横排表示博弈者一和下方各个对手博弈的得分
  > - 柱状图: 展示每个博弈者的总得分
