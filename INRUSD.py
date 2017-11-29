#!/usr/bin/env python
"""
this file is used to read the data from .csv file and do trend analysis for data between 1973 - 2017
and predict trends for future from 2017 to 2047
"""
# generator method to generate year, month for future prediction
def month_year_iter( start_month, start_year, end_month, end_year ):
    ym_start= 12*start_year + start_month - 1
    ym_end= 12*end_year + end_month - 1
    for ym in range( ym_start, ym_end ):
        y, m = divmod( ym, 12 )
        yield y, m+1

def calcTrends(file_to_read,file_to_write):
    """
    This method calculates the trends from csv files and predicts the future trends into another csv file
    :param file_to_read:
    :param file_to_write:
    :return: avg_change(in percent)
    """
    file = open(file_to_read, 'r')
    count = 0
    total_change = 0
    print("The major devaluation dates and percentage change:")
    for line in file:
        # print(line)
        list = line.split(',')
        # print(list[5][:-1].strip('%'))
        change = float(list[5][:-1].strip('%'))
        total_change = total_change + change
        count += 1
        if count == 1:
            last_value = float(list[1])

        if change > 10.00:
            print("{} : {}".format(list[0],change))

    avg_change = total_change/count
    print("avg change per month  = {0:.2f}".format(avg_change))
    file.close()
    monthly_value = last_value

    # start of predicting trends till Aug 2047
    file = open(file_to_write, 'w')
    for day in month_year_iter(8,2017,8,2047):
        monthly_value = monthly_value + monthly_value*(avg_change/100)
        data = "{} : {}".format(day, monthly_value)
        file.write(data)
        file.write('\n')
    file.close()
    return avg_change

if __name__ == '__main__':
    print("#############################\nCalculating trend analysis for INR to USD\n##################################")
    file_to_read_inr = 'inr_usd.csv'
    file_to_write_inr = 'inr_usd_predict.csv'
    avg_inr_change = calcTrends(file_to_read_inr, file_to_write_inr)
    print("The predicted data for INR value is in the {}".format(file_to_write_inr))
    file_to_read_cny = 'cny_usd.csv'
    file_to_write_cny = 'cny_usd_predict.csv'
    print("\n\n#############################\nCalculating trend analysis for CNY to USD\n##################################")
    avg_cny_change = calcTrends(file_to_read_cny, file_to_write_cny)
    print("INR avg = {}\nCNY avg = {}".format(avg_inr_change, avg_cny_change))
    print("The predicted data for CNY value is in the {}".format(file_to_write_cny))
