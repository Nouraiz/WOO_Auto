import os
import pandas as pd
import csv
import shutil
path_all = "C:\\Temp\\all_products"
path_output = "C:\Temp\\all_products\\output\\14-15"
path_cat = "C:\\Temp\\data\\stock_1415.csv"

# c = raw_input()
# if os.path.isfile(c):
#     f = open(c, "r+")
# else:print('Directory doesnot exist')
# path_cat = c
# print(path_cat)
all_products = []
x = 0

directory: object

# Getting all products
print("Loading All Products")
for root, directory, files in os.walk(path_all):
    for filename in files:
        all_products.append(filename)

total_removed = 0
print('Length before removal: ', len(all_products))
# for entry in all_products:
#     if len(entry) > 25:
#         #print(all_products[entry.find(entry)], 'delete\n')
#         all_products.remove(entry)
#         total_removed += 1
#
# print('Total Removed: ', total_removed)
# total_removed = 0

# Getting stock 2-3
print("Loading 2-3 Stock")
nooffiles = 0
out_products = []
with open(path_cat, newline='\n') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        current_product = (str(row)[5:-4])
        current_product = current_product.strip('-')
        #print(current_product)
        for entry in all_products:
            # print(entry, '\n')
            if len(entry) < 25:
                temp = entry.find(current_product)
                if temp != -1:
                    source = ''.join([path_all, '\\', entry])
                    dest = ''.join([path_output, '\\', entry])
                    #print(current_product, ' is in ', temp, 'index', source)
                    #print(dest)
                    shutil.copyfile(source, dest)
                    #print('Copied')
                    nooffiles += 1
                    break

print(nooffiles, "images copied to", path_output, 'successfully.')