# 博弈者文档

## RandomGamer `randomer.py`

随机博弈者，随机选择合作或背叛, 仅用于测试。

- **name:** Random
- **author:** [Fexcode](https://github.com/Fexcode)
- **create_at:** 2025.5.2

## TitForTat `tit_for_tat.py`

以牙还牙, 即该博弈者在第一次博弈中选择合作，之后的每次博弈都选择与对方上次的决策相同的策略.

- **name:** TitForTat
- **author:** [Fexcode](https://github.com/Fexcode)
- **create_at:** 2025.5.2

## Predictive `predictive.py`

预测博弈者，根据对方的历史记录预测对方的下一步行动，并选择最有可能的策略.<br>
第一次博弈选择合作，之后根据对手的背叛的概率选择背叛或者合作

> **例如:** 10 轮博弈中, 对手选择了 6 次背叛, 则该博弈者选择背叛.
>
> **注意:** 10 轮博弈中, 若对手选择了 5 次背叛, 则该博弈者选择合作.

- **name:** Predictive
- **author:** [Fexcode](https://github.com/Fexcode)
- **create_at:** 2025.5.3

## TwoForOne `two_for_one.py`

一报还两报博弈者，该博弈者在第一次博弈中选择合作，之后只有对手连续两次选择背叛才在下一轮选择背叛。

- **name:** TwoForOne
- **author:** [Fexcode](https://github.com/Fexcode)
- **create_at:** 2025.5.5

## TwoForOne_ButLoveBetray `two_for_one.py`

一报还两报博弈者类变体，继承自 GamerInterface。该博弈者在第一次博弈中选择合作，之后只有对手连续两次选择背叛才在下一轮选择背叛，但是在对手连续两次选择合作时，会选择背叛。

- **name:** TwoForOne_B
- **author:** [Fexcode](https://github.com/Fexcode)
- **create_at:** 2025.5.5
