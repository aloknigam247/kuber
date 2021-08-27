from trade import TradeSeq

import pandas as pd
import os

class Stock:
    price = "Average Price"

    def __init__(self, name: str, stock_path: str) -> None:
        self.__df: pd.DataFrame = pd.read_csv(stock_path, header=0, index_col=0, usecols=[2, 3, 4, 5, 6, 7, 8, 9])
        self.__name: str = name
        self.__tradeSeq: dict[str, TradeSeq] = dict()

    def appendCol(self, title: str, data: list[str]) -> None:
        self.__df[title] = data
    
    def addTrade(self, name:str, trade:TradeSeq) -> None:
        self.__tradeSeq[name] = trade

    def getCol(self, col: str):
        return self.__df[col].values

    def getData(self) -> pd.DataFrame:
        return self.__df

    def getName(self) -> str:
        return self.__name

    def getIndex(self) -> pd.Index:
        return self.__df.index

    def getAllTrades(self) -> dict[str, TradeSeq]:
        return self.__tradeSeq

class StockFactory:
    __stock_list: list[str] = None
    
    def create(stock_name: str) -> Stock:
        return Stock(stock_name, "stocks/" + stock_name + ".csv")
    
    def getNames() -> list[str]:
        if not StockFactory.__stock_list:
            StockFactory.__stock_list = []
            if os.path.exists("stocks"):
                for f in os.listdir("stocks"):
                    StockFactory.__stock_list.append(f.split('.')[0])
        
        return StockFactory.__stock_list
