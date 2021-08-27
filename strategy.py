from stock import Stock
from trade import *

import metainfo as mi

class Strategy:
    def apply(self, stock: Stock) -> None:
        pass

class Best(Strategy):
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

        stock.addTrade("Best", tseq)

class NDayAverage(Strategy):
    def apply(self, stock: Stock) -> None:
        nday_list = [2, 5, 10, 20, 50]
        mi.nDayAverageInfo(stock, nday_list)

        l = len(nday_list)
        for i in range(l-1):
            for j in range(i+1, l):
                d1 = nday_list[i]
                d2 = nday_list[j]
                col1 = str(d1) + " day avg"
                col2 = str(d2) + " day avg"
                d1_arr = stock.getCol(col1)
                d2_arr = stock.getCol(col1)
                tseq:TradeSeq = TradeSeq(Stock.price, [Stock.price, col1, col2])

                d2_len = len(d2_arr)
                # skip NaN values of d2
                for t in range(d2_len)):
                    if d2_arr[t]:
                        break
                
                # find first buy point
                if d1_arr[t] > d2_arr[t]:
                    tseq.trade(Trade(t, TradeAction.Buy))
                else:
                    for t in range(t, len(d2_arr)):
                        if d1_arr[t] > d2_arr[t]:
                            tseq.trade(Trade(t, TradeAction.Buy))
                            break
                
                status = "buy"
                # trade as usual, when you have already bought
                for t in range(t, d2_len):
                    if d1_arr[t] > d2_arr[t]:
                        if status == "sell":
                            tseq.trade(Trade(t, TradeAction.Buy))
                            status = "buy"
                    else:
                        if status == "buy":
                            tseq.trade(Trade(t, TradeAction.Sell))
                            status = "sell"

                # Check if exit sell available
                if status == "buy" and d1_arr[t] > d2_arr[t]:
                    tseq.trade(Trade(t, TradeAction.Sell))
                
                stock.addTrade(str(d1) + " vs " + str(d2), tseq)

class StrategyFactory:
    __strategies: dict[str, Strategy] = {
        "Best": Best,
        "NDayAverage": NDayAverage
    }

    def create(strategy_name: str) -> Strategy:
        return StrategyFactory.__strategies[strategy_name]

    def getNames() -> list[str]:
        return list(StrategyFactory.__strategies.keys())
