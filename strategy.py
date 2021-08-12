from stock import Stock
from trader import Trader
from tradeseq import TradeSeq

class Strategy:
    def apply(self, trader: Trader, stock: Stock) -> TradeSeq:
        pass

class StrategyFactory:
    __strategies: dict[str, Strategy] = {}

    def create(strategy_name: str) -> Strategy:
        return StrategyFactory.__strategies[strategy_name]

    def getNames() -> list[str]:
        return list(StrategyFactory.__strategies.keys())
