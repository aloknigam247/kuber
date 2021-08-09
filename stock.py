import os

class Stock:
    pass

class StockFactory:
    __stock_list: list[str] = None
    
    def create(stock_name: str) -> Stock:
        pass
    
    def getNames() -> list[str]:
        if not StockFactory.__stock_list:
            StockFactory.__stock_list = []
            if os.path.exists("stocks"):
                for f in os.listdir("stocks"):
                    StockFactory.__stock_list.append(f.split('.')[0])
        
        return StockFactory.__stock_list