import argparse
import sys

from logger import Logger as log
from reports import *
from runconfig import *
from stock import *
from strategy import *
from trader import *
from tradeseq import *

# Command line option parser
cmdline = argparse.ArgumentParser(description="Kuber Trading Analysis")
cmdline.add_argument('--config', help="run config to use")
cmdline.add_argument('--dump_config', action="store_true", help="dump complete config with name default_config.json")
args = cmdline.parse_args()

if args.dump_config:
    # Dump config and exit
    RunConfig().dump()
    sys.exit(0)

# Read config and generate reports
if not args.config:
    log.error("No config specified")
    sys.exit(1)

# Load config and exit on error
config = RunConfig()

log.wait("Loading Config")
if not config.load(args.config):
    # error in loading config, exit
    sys.exit(1)

stock_list:    list[Stock]    = []
strategy_list: list[Strategy] = []
trader_list:   list[Trader]   = []
report_list:   list[Report]   = []
tradeseq_list: list[TradeSeq] = []

log.wait("Loading Traders")
for item in config.getTraderList():
    trader_list.append(TraderFactory.create(item))

log.wait("Loading Strategies")
for item in config.getStrategyList():
    strategy_list.append(StrategyFactory.create(item))

log.wait("Loading Stock")
for item in config.getStockList():
    stock_list.append(StockFactory.create(item))

log.wait("Loading Reports")
for item in config.getReportList():
    report_list.append(ReportFactory.create(item))

log.wait("Applying Strategies")
for stock in stock_list:
    for trader in trader_list:
        for strategy in strategy_list:
            tradeseq_list.append(strategy.apply(trader, stock))

log.wait("Generating Reports")
for report in report_list:
    report.generate(tradeseq_list)
