# from datetime import datetime
# a = 'Feb 25 2020 4:20PM'
# dek = datetime.strptime(a, '%b %d %Y %I:%M%p')
# print(dek)



# from datetime import datetime,timedelta
# given_date = datetime(2020,2,25)
# res = given_date - timedelta(days=7)
# print(res.date())






from datetime import datetime
def main(dek):
    a = datetime.strftime(dek, '%A')
    return a
print(main(12/072019))






















