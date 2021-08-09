import json
import os

from logger import Logger as log
from reports import ReportFactory
from stock import StockFactory
from strategy import StrategyFactory
from trader import TraderFactory


class RunConfig:
    """ Config manager
    """

    def __init__(self) -> None:
        self.run_name = "config"
        self.tag_name = "Name"
        self.tag_report = "Reports"
        self.tag_stock = "Stocks"
        self.tag_strategy = "Strategy"
        self.tag_trader = "Traders"

        self.report_list: list[str] = []
        self.strategy_list: list[str] = []
        self.stock_list: list[str] = []
        self.trader_list: list[str] = []

    def __validateName(self, config: dict[str, str], valid_names: list[str], key: str) -> tuple[list[str], bool]:
        """ Validate names against valid name list and return valid names

        Args:
            items (list[str]): items to be validated
            valid_names (list[str]): list of valid names
            type (str): type of names, used in printing logs

        Returns:
            tuple[
                list[str]: list of valid names
                bool: result of validation
            ]
        """
        validated_list: list[str] = []
        result = True

        if not key in config:
            log.error(key, "tag does not exists in config file")
            return []

        for item in config[key]:
            if item in valid_names:
                validated_list.append(item)
            else:
                log.error(key, "`" + item + "` is an invalid", key)
                result = False

        if not result:
            log.info("valid", key, "types are", ', '.join(valid_names))

        return validated_list, result

    def dump(self):
        """ Dumps all config options available
            default output file is config.json
        """

        json_config = {
            self.tag_name     : self.run_name,
            self.tag_report   : ReportFactory.getNames(),
            self.tag_stock    : StockFactory.getNames(),
            self.tag_strategy : StrategyFactory.getNames(),
            self.tag_trader   : TraderFactory.getNames()
        }

        json_filename = self.run_name + ".json"
        with open(json_filename, "w") as fp:
            json.dump(json_config, fp, indent=4)
        
        log.info("Config", json_filename, "dumped")



    def load(self, config_file: str) -> bool:
        """ Loads run configurations from the run config file

        Args:
            config_file (str): json format config file

        Returns:
            bool: returns True if load is successfull
        """
        if not os.path.exists(config_file):
            log.error(config_file, "does not exists")
            return False

        with open(config_file, "r") as fp:
            config = json.load(fp)
    
        self.run_name = config[self.tag_name]
        self.report_list, res1 = self.__validateName(config, ReportFactory.getNames(), self.tag_report)
        self.stock_list, res2 = self.__validateName(config, StockFactory.getNames(), self.tag_stock)
        self.strategy_list, res3 = self.__validateName(config, StrategyFactory.getNames(), self.tag_strategy)
        self.trader_list, res4 = self.__validateName(config, TraderFactory.getNames(), self.tag_trader)

        return res1 or res2 or res3 or res4

    def getRunName(self):
        return self.run_name

    def getTraderList(self) -> list[str]:
        return self.trader_list

    def getStrategyList(self) -> list[str]:
        return self.strategy_list

    def getStockList(self) -> list[str]:
        return self.stock_list

    def getReportList(self) -> list[str]:
        return self.report_list
