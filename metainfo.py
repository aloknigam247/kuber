from numpy import NaN
from stock import Stock

def nDayAverageInfo(stock: Stock, day_list):
    price_arr = stock.getCol(Stock.price)

    for nday in day_list:
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