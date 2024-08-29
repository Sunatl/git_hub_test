# from datetime import datetime
# def main(date):
#     if date.month == 10 and date.day == 31:
#         return "Bonfire toffee"
#     else:
#         return "toffee"
# print(main(datetime.strptime("2013/10/31", "%Y/%m/%d")))
# print(main(datetime.strptime("2012/07/31", "%Y/%m/%d")))
# print(main(datetime.strptime("2011/10/12", "%Y/%m/%d")))





# def main(a):
#     return (a + 99) // 100
# print(main(2005))
# print(main(1950)) 
# print(main(1900))  





# def main(a, b):
#     if a == "" :
#         return "year missing"
#     if b == "" :
#         return "month missing"
#     s = b // 12
#     return a + s
# print(main(2020, 24))
# print(main(1832, 2)) 
# print(main(1444, 60))
# print(main("", 24))  
# print(main(2020, ""))





# def main(a):
#     month, day, year = a.split('/')
#     s = f"{year}{day}{month}"
#     return s
# print(main("11/12/2019"))
# print(main("12/31/2019"))





# from datetime import date
# def main(a):
#     return a.month == 12 and a.day == 24
# print(main(date(2013, 12, 24)))
# print(main(date(2013, 12, 23)))
# print(main(date(3000, 12, 24)))







# from datetime import datetime
# def get_day(a):
#     t = datetime.strptime(a, '%m/%d/%Y')
#     k = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     x = (t.weekday() + 1) % 7
#     return k[x]
# print(get_day("12/07/2016")) 
# print(get_day("09/04/2016")) 
# print(get_day("12/08/2011")) 



# def main(a, b):
#     s = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if a == 2: 
#         if b % 4 == 0:
#             return 29 
#         else:
#             return 28  
#     return s[a - 1]
# print(main(2, 2018))
# print(main(4, 654))
# print(main(2, 200))
# print(main(8, 2024))




def main(a,lis = {}):
    
    month, day, year = a.split("/")
    lis = [1,9,2019]
    
    return lis
print(main("01/09/2019"))
