import csv
import string

with open('weather_small_conditions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    l1 = ''
    for row in csv_reader:
        # print(type(row))
        l1 = ''.join(row[0])
        # print(type(l1))

        exists = l1.find('2016')

        if exists >= 0:
            l1 = l1.replace("2016", "2018", 1)
            print(l1, '  -  ', len(l1), '  -  ', type(l1), '  --  ', exists)
            # if line_count == 0:
            #      print(f'Column names are {", ".join(row)}')
            line_count += 1
    # else:
    #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #     line_count += 1
    print(f'Processed {line_count} lines.')
