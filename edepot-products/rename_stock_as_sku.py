import os
import pandas as pd
import csv
import shutil



path_all = "C:\\Temp\\all_products"
# path_output = "C:\Temp\\all_products\\output\\14-15"
path_prod_name = "C:\\Temp\\data\\complete_stock.csv"
path_prod_sku = "C:\\Temp\\data\\complete_stock_sku.csv"
path_rename = "C:\Temp\\all_products\\after_rename"

all_products = []
# x = 0
#
directory: object

# Getting all products
#print("Loading All Products")
for root, directory, files in os.walk(path_all):
    for filename in files:
        all_products.append(filename)

prod_name_name = []
#print('opening .........................\n\n')
with open(path_prod_name, newline='\n') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for filename in row:
            #print(row)
            prod_name_name.append(row)
    #print('\n\n')

prod_name_sku = []
#print('opening .........................\n\n')
with open(path_prod_sku, newline='\n') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for filename in row:
            #print(row)
            prod_name_sku.append(row)
    #print('\n\n')

# print('Loading name and sku')
# print(prod_name_name)
# print(prod_name_sku)
# print('\n\n')
index = 0
for entry in all_products:
    if len(entry) > 24:
        for id, name in prod_name_name:
            if entry in name:
                print('matched: ', id)
                for id2, name2 in prod_name_sku:
                    if id == id2:
                        #print(entry, name, name2, '\n\n')
                        #os.rename
                        #source = ''.join([path_all, '\\', entry])
                        dest = ''.join([path_all, '\\', name2+'.jpg'])


                        try:
                            os.rename("C:\\Temp\\all_products\\"+str(entry), dest)
                            break
                        except (RuntimeError, TypeError, NameError):
                            pass
                        print(source, dest)
                        print('file renamed successfully')