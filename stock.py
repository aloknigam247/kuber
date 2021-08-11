import pandas as pd
import os

class Stock:
    def __init__(self, stock_path: str) -> None:
        self.__df = pd.read_csv(stock_path, header=0, index_col=0, usecols=[2, 3, 4, 5, 6, 7, 8, 9])

class StockFactory:
    __stock_list: list[str] = None
    
    def create(stock_name: str) -> Stock:
        return Stock("stocks/" + stock_name + ".csv")
    
    def getNames() -> list[str]:
        if not StockFactory.__stock_list:
            StockFactory.__stock_list = []
            if os.path.exists("stocks"):
                for f in os.listdir("stocks"):
                    StockFactory.__stock_list.append(f.split('.')[0])
        
        return StockFactory.__stock_list