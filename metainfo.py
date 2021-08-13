from numpy import NaN
from stock import Stock


class MetaInfo:
    def generate(stock: Stock):
        pass

class NDayAverage(MetaInfo):
    def generate(stock: Stock):
        price_arr = stock.getCol(Stock.price)

        for nday in [2, 5, 10, 20, 50]:
            j: int = 0
            sum: float = 0
            avg_list: list[float] = []

            for i in range(nday-1):
                sum += price_arr[i]
                avg_list.append(NaN)

            for i in range(nday-1, len(price_arr)):
                sum += price_arr[i]
                avg = sum/nday
                avg_list.append(avg)
                sum = sum - price_arr[j]
                j += 1

            stock.appendCol(str(nday) + " day avg", avg_list)

class MetaInfoFactory:
    __metainfo_list: dict[str, MetaInfo] = {
        "NDayAverage": NDayAverage
    }

    def create(metainfo: str) -> MetaInfo:
        return MetaInfoFactory.__metainfo_list[metainfo]

    def getNames() -> list[str]:
        return list(MetaInfoFactory.__metainfo_list.keys())
