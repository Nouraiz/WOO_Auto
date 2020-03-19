import os
import shutil

# user inputs
directory = int(input("Starting SKU: "))
numOfDir = int(input("Number of products to process: "))
itr = int(input("Images per SKU: "))
category_list = ["girlsT", "boysT", "casualT", "pants", "shorts"]
print(category_list)
category_selected = input("Which Category: ")
print(category_selected)

sku_prefix = ""
if category_selected == "girlsT" or category_selected == "boysT" or category_selected == "casualT":
    sku_prefix = "FWT-"
else:
    sku_prefix = "FWB-"


# Directory paths
copyTo_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020\new_stock"
copyFrom_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020\Garment pics"

copyTo_dir = os.path.join(copyTo_dir, category_selected)
copyFrom_dir = os.path.join(copyFrom_dir, category_selected)
print("copy from:", copyFrom_dir, "\n", "copy to: ", copyTo_dir)

try:
    os.mkdir(copyTo_dir)
    print("Folder created: ", copyTo_dir)
except OSError as e:
    print(e)

x = 0
while x < numOfDir:
    itr = 0
    path = os.path.join(copyTo_dir, sku_prefix+str(directory))
    try:
        os.mkdir(path)
        print("Directory created: ", path)
    except OSError as e:
        print(e)
        pass
    for files in os.listdir(copyFrom_dir):
        if itr < 3:
            shutil.move(os.path.join(copyFrom_dir, files), os.path.join(path, files))
            itr += 1
            print(str(files), "moved")
            continue
        else:
            break
    x += 1
    directory += 1
    print("\n")
