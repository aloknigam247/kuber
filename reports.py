import os

import plotly.express as px

from stock import Stock


class Report:
    def __init__(self, dump_dir: str) -> None:
        if not os.path.exists(dump_dir):
            os.mkdir(dump_dir)
        self._dump_dir = dump_dir

    def generate(self, stock: Stock):
        pass

class LineChart(Report):
    def generate(self, stock: Stock):
        df = stock.getData()
        fig = px.line(df, title=stock.getName())
        fig.write_html(self._dump_dir + "/" + stock.getName() + ".html")

class ReportFactory:
    __reports: dict[str, Report] = {
        "LineChart": LineChart
    }

    def create(report_name: str, dump_dir: str) -> Report:
        report = ReportFactory.__reports[report_name]
        return report(dump_dir + "/" + report_name)

    def getNames() -> list[str]:
        return list(ReportFactory.__reports.keys())
