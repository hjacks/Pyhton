import csv
from datetime import datetime
import matplotlib.pyplot as plt
# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index,column_reader in enumerate(header_row):
    #     print(index,column_reader)
    # 从文件中获取最高气温和日期和最低气温
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            high = int(row[1])
            highs.append(high)
            low = int(row[3])

        except ValueError:
            print(current_date,'missing data')
        else:
            lows.append(low)
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            dates.append(current_date)
# print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()# 绘制斜的日期标签
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)# 设置坐标轴刻度大学
plt.show()