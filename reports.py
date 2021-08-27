from logger import Logger as log
from trade import TradeAction
from stock import Stock

import plotly.express as px
import plotly.graph_objects as go
import os

class Report:
    def __init__(self, dump_dir: str) -> None:
        if not os.path.exists(dump_dir):
            os.mkdir(dump_dir)
        self._dump_dir = dump_dir

    def generate(self, stock: Stock) -> None:
        pass

class LineChart(Report):
    def generate(self, stock: Stock) -> None:
        df = stock.getData()
        fig = px.line(df, title=stock.getName())
        fig.write_html(self._dump_dir + "/" + stock.getName() + ".html")

class TradeMarker(Report):
    def generate(self, stock: Stock) -> None:
        index_arr = stock.getIndex()
        graph_list: list[go.Scatter] = []
        data_set: set[str] = set()
        for tname, tseq in stock.getTrades().items():
            log.info("Generating trade marker", tname)
            value_arr = stock.getCol(tseq.getPriceColName())
            buy_xdata = []
            buy_ydata = []
            sell_xdata = []
            sell_ydata = []

            for data in tseq.getDataList():
                data_set.add(data)

            for trade in tseq.getSeq():
                if trade.action == TradeAction.Buy:
                    buy_xdata.append(index_arr[trade.index])
                    buy_ydata.append(value_arr[trade.index])
                else:
                    sell_xdata.append(index_arr[trade.index])
                    sell_ydata.append(value_arr[trade.index])

            graph_list.append(go.Scatter(x=buy_xdata, y=buy_ydata, mode='markers', name=tname + ' Buy'))
            graph_list.append(go.Scatter(x=sell_xdata, y=sell_ydata, mode='markers', name=tname + ' Sell'))

        df = stock.getData()
        fig = px.line(df, title=stock.getName(), y=list(data_set))
        fig.add_traces(graph_list)
        fig.write_html(self._dump_dir + "/" + stock.getName() + ".html")

class ReportFactory:
    __reports: dict[str, Report] = {
        "LineChart": LineChart,
        "TradeMarker": TradeMarker
    }

    def create(report_name: str, dump_dir: str) -> Report:
        report = ReportFactory.__reports[report_name]
        return report(dump_dir + "/" + report_name)

    def getNames() -> list[str]:
        return list(ReportFactory.__reports.keys())
