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
        self.__run_name = "config"
        self.__tag_name = "Name"
        self.__tag_report = "Reports"
        self.__tag_stock = "Stocks"
        self.__tag_strategy = "Strategy"
        self.__tag_trader = "Traders"

        self.__report_list: list[str] = []
        self.__strategy_list: list[str] = []
        self.__stock_list: list[str] = []
        self.__trader_list: list[str] = []

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
            log.info("valid", key, "are", ', '.join(valid_names))

        return validated_list, result

    def dump(self):
        """ Dumps all config options available
            default output file is config.json
        """

        json_config = {
            self.__tag_name     : self.__run_name,
            self.__tag_report   : ReportFactory.getNames(),
            self.__tag_stock    : StockFactory.getNames(),
            self.__tag_strategy : StrategyFactory.getNames(),
            self.__tag_trader   : TraderFactory.getNames()
        }

        json_filename = self.__run_name + ".json"
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
    
        self.__run_name = config[self.__tag_name]
        self.__report_list, res1 = self.__validateName(config, ReportFactory.getNames(), self.__tag_report)
        self.__stock_list, res2 = self.__validateName(config, StockFactory.getNames(), self.__tag_stock)
        self.__strategy_list, res3 = self.__validateName(config, StrategyFactory.getNames(), self.__tag_strategy)
        self.__trader_list, res4 = self.__validateName(config, TraderFactory.getNames(), self.__tag_trader)

        return res1 and res2 and res3 and res4

    def getRunName(self):
        return self.__run_name

    def getTraderList(self) -> list[str]:
        return self.__trader_list

    def getStrategyList(self) -> list[str]:
        return self.__strategy_list

    def getStockList(self) -> list[str]:
        return self.__stock_list

    def getReportList(self) -> list[str]:
        return self.__report_list
