import os
import yaml

from logger import Logger as log
from metainfo import MetaInfoFactory
from reports import ReportFactory
from stock import StockFactory
from strategy import StrategyFactory
from trader import TraderFactory


class RunConfig:
    def __init__(self) -> None:
        self.__config_name = "config.yaml"
        self.__run_name = "reports"
        self.__tag_metainfo = "MetaInfo"
        self.__tag_name = "Name"
        self.__tag_report = "Reports"
        self.__tag_stock = "Stocks"
        self.__tag_strategy = "Strategy"
        self.__tag_trader = "Traders"

        self.__metainfo_list: list[str] = []
        self.__report_list: list[str] = []
        self.__stock_list: list[str] = []
        self.__strategy_list: list[str] = []
        self.__trader_list: list[str] = []

    def __validateName(self, config: dict[str, str], valid_names: list[str], key: str) -> tuple[list[str], bool]:
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
        yaml_config = {
            self.__tag_name     : self.__run_name,
            self.__tag_metainfo : MetaInfoFactory.getNames(),
            self.__tag_report   : ReportFactory.getNames(),
            self.__tag_stock    : StockFactory.getNames(),
            self.__tag_strategy : StrategyFactory.getNames(),
            self.__tag_trader   : TraderFactory.getNames()
        }

        with open(self.__config_name, "w") as fp:
            yaml.safe_dump(yaml_config, fp, indent=4)
        
        log.info("Config", self.__config_name, "dumped")



    def load(self, config_file: str) -> bool:
        if not os.path.exists(config_file):
            log.error(config_file, "does not exists")
            return False

        with open(config_file, "r") as fp:
            config = yaml.safe_load(fp)
    
        self.__run_name = config[self.__tag_name]
        self.__metainfo_list, res5 = self.__validateName(config, MetaInfoFactory.getNames(), self.__tag_metainfo)
        self.__report_list, res1 = self.__validateName(config, ReportFactory.getNames(), self.__tag_report)
        self.__stock_list, res2 = self.__validateName(config, StockFactory.getNames(), self.__tag_stock)
        self.__strategy_list, res3 = self.__validateName(config, StrategyFactory.getNames(), self.__tag_strategy)
        self.__trader_list, res4 = self.__validateName(config, TraderFactory.getNames(), self.__tag_trader)

        return res1 and res2 and res3 and res4 and res5

    def getRunName(self):
        return self.__run_name

    def getMetaInfoList(self) -> list[str]:
        return self.__metainfo_list

    def getReportList(self) -> list[str]:
        return self.__report_list

    def getStockList(self) -> list[str]:
        return self.__stock_list

    def getStrategyList(self) -> list[str]:
        return self.__strategy_list

    def getTraderList(self) -> list[str]:
        return self.__trader_list
