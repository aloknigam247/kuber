import argparse
import os.path as path
import sys

from logger import Logger as log
from reports import Report
from runconfig import RunConfig
from stock import Stock
from strategy import Strategy
from trader import Trader
from tradeseq import TradeSeq

# Command line option parser
cmdline = argparse.ArgumentParser(description="Kuber Trading Analysis")
cmdline.add_argument('--config', help="run config to use")
cmdline.add_argument('--dump_config', action="store_true", help="dump complete config with name default_config.json")
args = cmdline.parse_args()

if args.dump_config:
    # Dump config and exit
    config = RunConfig()
    config.dump()
    sys.exit()

# Read config and generate reports
if not args.config:
    log.error("No config specified")
    sys.exit()

# Load config and exit on error
config = RunConfig()

log.wait("Loading Config")
if not config.load(args.config):
    # error in loading config, exit
    sys.exit()

stock_list     = []
strategy_list  = []
trader_list    = []
report_list    = []
tradeseq_list  = []

log.wait("Loading Traders")
for item in config.getTraderList():
    trader_list.append(item)

log.wait("Loading Strategies")
for item in config.getStrategyList():
    strategy_list.append(item)

log.wait("Loading Stock")
for item in config.getStockList():
    stock_list.append(item)

log.wait("Loading Reports")
for item in config.getReportList():
    report_list.append(item)

log.wait("Applying Strategies")
for stock in stock_list:
    for trader in trader_list:
        for strategy in strategy_list:
            tradeseq = strategy.apply(trader, stock)
            tradeseq.dump()


log.wait("Generating Reports")
for report in report_list:
    report.generate(tradeseq_list)