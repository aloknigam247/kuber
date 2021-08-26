from stock import Stock
from trade import *

class Strategy:
    def apply(self, stock: Stock) -> None:
        pass

class IdealStrategy(Strategy):
    def apply(self, stock: Stock) -> None:
        tseq:TradeSeq = TradeSeq(Stock.price, [Stock.price])
        price_arr = stock.getCol(Stock.price)

        # initial values
        index = 0
        last_price = price_arr[0]
        last_dir = "up" if price_arr[1] > price_arr[0] else "down"

        # find first buy point
        if last_dir == "down":
            for price in price_arr[index+1:]:
                dir = "up" if price > last_price else "down"
                if dir == "up":
                    break
                index += 1
        tseq.trade(Trade(index, TradeAction.Buy))

        # trade as usual, when you have already bought
        for price in price_arr[index+1:]:
            dir = "up" if price > last_price else "down"

            if last_dir == dir:
                pass
            elif last_dir == "up" and dir == "down":
                tseq.trade(Trade(index, TradeAction.Sell))
            else:
                tseq.trade(Trade(index, TradeAction.Buy))

            last_price = price
            last_dir = dir
            index += 1
        
        # Check if exit sell available
        if price_arr[index] > price_arr[index-1]:
            tseq.trade(Trade(index, TradeAction.Sell))

        stock.addTrade("IdealTrade", tseq)

class StrategyFactory:
    __strategies: dict[str, Strategy] = {
        "IdealStrategy": IdealStrategy
    }

    def create(strategy_name: str) -> Strategy:
        return StrategyFactory.__strategies[strategy_name]

    def getNames() -> list[str]:
        return list(StrategyFactory.__strategies.keys())
