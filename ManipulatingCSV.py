import csv

with open('weather_small_conditions_2018.csv', mode='w') as rez_csv_file:
    data_writer = csv.writer(rez_csv_file)

    with open('weather_small_conditions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        l1 = ''
        for row in csv_reader:
            l1 = ','.join(row)

            exists = l1.find('2016')

            if exists >= 0:
                l1 = l1.replace("2016", "2018", 1)

            line_count += 1
            print(l1, '  -  ', len(l1), '  --  ', exists)

        # else:
        #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #     line_count += 1
        print(f"Обработано {line_count} строк.")
