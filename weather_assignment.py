import json

with open('precipitation.json', encoding = 'utf-8') as file:
    list_of_dictionary = json.load(file)

from csv import DictReader

with open('stations.csv') as file:
    reader = DictReader(file)
#    list_of_dictionary = list(reader)

#print(list_of_dictionary)

#PART 1: Seattle
#total_monthly_precipitation = 0
#for dictionary in list_of_dictionary:
#    total_monthly_precipitation += dictionary['GHCND:US1WAKG0038']  
#    #list_of_dictionary['lines_total']

#total_seattle_sum = 0
#for dictionary in list_of_dictionary():
#    if seattle = dictionary[]["GHCND:US1WAKG0038"]


#for dictionary in list_of_dictionary:
#    total_seattle_sum = total_seattle_sum + dictionary ["value"]

#print (total_seattle_sum)

seattle = []
for measurement in list_of_dictionary:
    station_id = measurement["station"]
    if station_id == "GHCND:US1WAKG0038":
        seattle.append(measurement)

#x = range(12)
#precipitation = []
#for month in x:
#    month_value = []
#    precipitation.append(month_value)

#month_dict = {}
#for values in precipitation:
#    month = values[month_value]
#    values[month] = month
#
#    print (month_dict)
#for measurement in seattle:
#    date = str(measurement["date"])
#    date = date.split("-")
#    for month in x: 
#        if date[1] == (f"0{month}") or (f"{month}"):
#            precipitation[month].append(measurement["value"])



#print(precipitation[4])
#list_sum = []
#monthly_sum = 0
#for value in month_value:
#    for day in month_value:
#        monthly_sum = monthly_sum + day
#        list_sum.append(monthly_sum)
    


#dates = []
#for measurement in seattle:
#    date = measurement["date"] 
#    if date == date.startswith):
#        dates.append(measurement)
#print (dates)

#total_monthly_precipitation = 0
#for dictionary in seattle:
#    total_monthly_precipitation += dictionary['value']  



list_of_months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for months in seattle:
    date = str(months['date'])
    date_split = date.split('-')
    month = date_split[1]
    month = int(month)
    index = month -1
    value = months['value']
    list_of_months[index] += value
print('The total monthly values are:', list_of_months)