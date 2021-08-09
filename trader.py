import os

class Trader:
    pass

class TraderFactory:
    __trader_list: list[str] = None

    def create(trader_name: str) -> Trader:
        pass
    
    def getNames() -> list[str]:
        if not TraderFactory.__trader_list:
            TraderFactory.__trader_list = os.listdir("traders") if os.path.exists("traders") else []
        
        return TraderFactory.__trader_list
