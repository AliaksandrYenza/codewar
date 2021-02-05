import csv
import datetime as DT

if __name__ == '__main__':
    dict_primary_type = {}
    with open('CSVdir/Crimes.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if DT.datetime.strptime(row['Date'], '%m/%d/%Y %I:%M:%S %p').year == 2015:
                if row['Primary Type'] in dict_primary_type.keys():
                    dict_primary_type[row['Primary Type']] += 1
                elif row['Primary Type'] not in dict_primary_type.keys():
                    dict_primary_type[row['Primary Type']] = 1
    print(dict_primary_type)
    max_k = max(dict_primary_type.values())
    print(max_k)
