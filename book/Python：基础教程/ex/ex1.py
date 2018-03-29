months=['January','February','March','April','May','June','July',
        'August','Septemper','October','November','December']
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+17*['th']+['st']
year=input('Year:')
month=input('Month(1-12):')
day=input('Day(1-31):')

month_num=int(month)
day_num=int(day)
month_name=months[month_num-1]
ordel=day+endings[day_num-1]
print(month_name+' '+ordel+','+year)
