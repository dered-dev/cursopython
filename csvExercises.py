""" CSV module Exercise """

import csv

def csvfile(filename):
    with open(filename, newline = '') as row:
        rowfile = csv.reader(row)
        list_items = list(rowfile)
    return list_items

def getCsvFile(filename, row_list):
    with open(filename, "w", newline = "") as output:
        writer = csv.writer(output)
        writer.writerows(row_list)

rowList = csvfile('example.csv')
getCsvFile('result.csv', rowList)
print(rowList)
