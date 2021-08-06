class RunConfig:

    def dump(self):
        pass

    def load(self, config_file: str) -> bool:
        return True

    def getTraderList(self) -> list[str]:
        return []

    def getStrategyList(self) -> list[str]:
        return []

    def getStockList(self) -> list[str]:
        return []

    def getReportList(self) -> list[str]:
        return []