import csv


def check_year(year):
    with open('rainfall.csv', newline='') as file:
        reader = csv.DictReader(file)
        for y in reader:
            if y["Year"] == year:
                return y
        print("In Particular date no data available in the dataset")


def total_rainfall(yer):
    y = check_year(yer)
    if y:
        list = []
        for i in y:
            list.append(y[i])
        sum1 = 0
        for i in range(1, 13):
            sum1 = sum1 + float(list[i])
        print("Annual rainfall for the year " + str(yer) + " = " + str(round(sum1, 1)))


def winter_rain(yer):
    y = check_year(yer)
    if y:
        sum1 = float(y["Jan"]) + float(y["Feb"])
        print("Annual winter rain for the year " + str(yer) + " = " + str(round(sum1, 1)))


def pre_monsoon_rain(yer):
    y = check_year(yer)
    if y:
        sum1 = float(y["Mar"]) + float(y["Apr"]) + float(y["May"])
        print("Annual pre-monsoon rain for the year " + str(yer) + " = " + str(round(sum1, 1)))


def south_west_monsoon(yer):
    y = check_year()
    if y:
        sum1 = float(y["Jun"]) + float(y["Jul"]) + float(y["Aug"]) + float(y["Sep"])
        print("Annual south west monsoon rain for the year " + str(yer) + " = " + str(round(sum1, 1)))


def north_east_monsoon(yer):
    y = check_year(yer)
    if y:
        sum1 = float(y["Oct"]) + float(y["Nov"]) + float(y["Dec"])
        print("Annual north west monsoon rain for the year " + str(yr) + " = " + str(round(sum1, 1)))


def monthly_rain(yer):
    y = check_year(yer)
    if y:
        a = []
        months = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for i in y:
            a.append(y[i])
        for i in range(13):
            print(months[i] + " : " + a[i])


yr = input("Enter year:")
total_rainfall(yr)
winter_rain(yr)
pre_monsoon_rain(yr)
south_west_monsoon(yr)
north_east_monsoon(yr)
monthly_rain(yr)
