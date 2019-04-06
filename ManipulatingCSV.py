import csv
import sys

output = ''.join(sys.argv[1])

with open('weather_small_conditions_2018.csv', 'w') as rez_csv_file:
    with open(output) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print(type(csv_reader))
        line_count = 0
        l1 = ''

        for row in csv_reader:
            l1 = ','.join(row)
            exists = l1.find('2016')

            if exists >= 0:
                l1 = l1.replace("2016", "2018", 1)

            line_count += 1
            print(l1)
            rez_csv_file.write(l1 + '\n')

        rez_csv_file.close()

        print(f"Обработано {line_count} строк.")
