from datetime import datetime
def main(date):
    if date.month == 10 and date.day == 31:
        return "Bonfire toffee"
    else:
        return "toffee"
print(main(datetime.strptime("2013/10/31", "%Y/%m/%d")))  # "Bonfire toffee"
print(main(datetime.strptime("2012/07/31", "%Y/%m/%d")))  # "toffee"
print(main(datetime.strptime("2011/10/12", "%Y/%m/%d")))  # "toffee"

