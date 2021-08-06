import inspect
import json
import os

import reports
import strategy
from logger import Logger as log

class RunConfig:
    """ Config manager
    """

    def __init__(self) -> None:
        self.run_name = "config"

    def dump(self):
        """ Dumps all config options available
            default output file is config.json
        """
        report_list = [m[0] for m in inspect.getmembers(reports, inspect.isclass) if m[1].__module__ == "reports"]
        strategy_list = [m[0] for m in inspect.getmembers(strategy, inspect.isclass) if m[1].__module__ == "strategy"]

        stock_list = os.listdir("./stocks") if os.path.exists("./stocks") else []
        trader_list = os.listdir("./traders") if os.path.exists("./traders") else []

        json_config = {
            "Name":     self.run_name,
            "Reports":  report_list[1:],
            "Stock":    stock_list,
            "Strategy": strategy_list[1:],
            "Traders":  trader_list
        }

        json_filename = self.run_name + ".json"
        fp = open(json_filename, "w")

        json.dump(json_config, fp, indent=4)
        fp.close()

        log.info("Config dumped with name", json_filename)

    def load(self, config_file: str) -> bool:
        self.run_name = ""
        return True

    def getRunName(self):
        return self.run_name

    def getTraderList(self) -> list[str]:
        return []

    def getStrategyList(self) -> list[str]:
        return []

    def getStockList(self) -> list[str]:
        return []

    def getReportList(self) -> list[str]:
        return []