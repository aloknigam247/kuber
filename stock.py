import pandas as pd
import os

class Stock:
    price = "Average Price"

    def __init__(self, name:str, stock_path: str) -> None:
        self.__df = pd.read_csv(stock_path, header=0, index_col=0, usecols=[2, 3, 4, 5, 6, 7, 8, 9])
        self.__name = name

    def appendCol(self, title, data):
        self.__df[title] = data

    def getCol(self, col: str):
        return self.__df[col].values

    def getData(self) -> pd.DataFrame:
        return self.__df

    def getName(self) -> str:
        return self.__name

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