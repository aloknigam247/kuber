from enum import Enum

class TradeAction(Enum):
    Buy = 0
    Sell = 1

class Trade:
    def __init__(self, i: int, act: TradeAction) -> None:
        self.index = i
        self.action = act

class TradeSeq:
    
    def __init__(self, name, data_list) -> None:
        self.__seq: list[Trade] = []
        self.__col_name: str = name
        self.__data_list = data_list

    def trade(self, trade: Trade):
        self.__seq.append(trade)
    
    def getSeq(self) -> list[Trade]:
        return self.__seq
    
    def getPriceColName(self) -> str:
        return self.__col_name
    
    def getDataList(self) -> list[str]:
        return self.__data_list
