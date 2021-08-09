class Report:

    def generate(self):
        pass

class ReportFactory:
    __reports: dict[str, Report] = {}

    def create(report_name: str) -> Report:
        if report_name in ReportFactory.__reports:
            return ReportFactory.__reports[report_name]
        else:
            return None

    def getNames() -> list[str]:
        return ReportFactory.__reports.keys()