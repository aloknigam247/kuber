from stock import Stock
from trader import Trader
from tradeseq import TradeSeq


class Strategy:
    pass

    def apply(self, trader: Trader, stock: Stock) -> TradeSeq:
        pass