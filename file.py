import csv
with open('portfolio.csv') as pfile:
    csv_reader = csv.reader(pfile,delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {"_".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} has {row[1]} no fo shares at price{row[2]}')
            line_count += 1
    print((f'Read {line_count-1} shares for portfolio'))
