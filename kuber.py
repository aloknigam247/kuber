import argparse
import sys

from logger import Logger as log
from metainfo import *
from reports import *
from runconfig import *
from stock import *
from strategy import *
from trader import *

# Command line option parser
cmdline = argparse.ArgumentParser(description="Kuber Trading Analysis")
cmdline.add_argument('--config', help="run config to use")
cmdline.add_argument('--dump_config', action="store_true", help="dump complete config with name default_config.yaml")
args = cmdline.parse_args()

# Dump config and exit
if args.dump_config:
    RunConfig().dump()
    sys.exit(0)

# Read config and generate reports
if not args.config:
    log.error("No config specified")
    sys.exit(1)

config = RunConfig()

# Load config and exit on error
log.wait("Loading Config")
if not config.load(args.config):
    sys.exit(1)

log.wait("Loading Stocks")
stock_list: list[Stock] = []
for item in config.getStockList():
    stock_list.append(StockFactory.create(item))

log.wait("Generating Meta info")
for item in config.getMetaInfoList():
    meta = MetaInfoFactory.create(item)
    for stock in stock_list:
        meta.generate(stock)

log.wait("Applying Strategies")
for stock in stock_list:
    for s in config.getStrategyList():
        strategy = StrategyFactory.create(s)
        strategy.apply(stock, stock)

dump_dir = config.getRunName()
if not os.path.exists(dump_dir):
    os.mkdir(dump_dir)

log.wait("Generating Reports")
for item in config.getReportList():
    report = ReportFactory.create(item, dump_dir)
    for stock in stock_list:
        report.generate(stock)
