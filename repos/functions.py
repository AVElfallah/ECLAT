import sys
import os
import csv
from itertools import combinations
from PyQt5.QtWidgets import  QFileDialog
import config.config as cf 

# show dialog 
def dialog():
    ## get file from dialog
    file , check = QFileDialog.getOpenFileName(None, "Load database","", "CSV Files (*.csv);;All Files (*);;")
    ## if file is found return file path
    if check:
        print(file)
        return file
    else:
        # if file is not chosen return empty string
        return ''

def loadDataFromCSV():
    ## passing file pass to [txtpath] form [dilaog()]
    txtpath=dialog()
    ## setting file pass and file name and store them in config
    cf.databaseFilePath=txtpath
    cf.databaseFileName=txtpath.split('/')[-1]
    ## check if file exists run code else return false
    if(txtpath!=''):
        ## read csv file
        with open(txtpath, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            ## store database and filter it in config file
            cf.dataList=filter(data)

            return True
    return False

#filter database
def filter(data:list(list([str]))):
    values = []
    ## in this filter we remove empty fildes from database
    for row in data:
        newRow=[product for product in row if len(product)>0]
        values.append(newRow)
    return values


# eclat func
def doECLAT(limits:int=0,mini:int=0):
        print("ECLAT Starting")
        ##print database limit and mini support
        print('database size='+str(limits))
        print('mini support='+str(mini))
        ## passing database to eclat , mini support and return result to algorithm var
        algorithm = eclat(cf.dataList[0:limits],mini)
        ## write Eclat Report to CSV file
        writeCSVFile(algorithm)
        ## store eclat report in config
        cf.eclatReport=algorithm
        return True
                
            

## eclat algorithm
def eclat(transactions, min_support):
    # Create a list of unique items in the transaction database
    items = set()
    for transaction in transactions:
        for item in transaction:
            items.add(item)
    items = list(items)

    # Create a dictionary to store the support count for each item
    support_count = {item: 0 for item in items}

    # Count the support for each item
    for transaction in transactions:
        for item in items:
            if item in transaction:
                support_count[item] += 1

    # Filter out items that do not meet the minimum support
    frequent_items = [item for item in support_count if support_count[item] >= min_support]

    # Create a list of frequent itemsets
    frequent_itemsets = []
    for i in range(1, len(frequent_items)+1):
        # Generate all combinations of frequent items
        frequent_itemsets += list(combinations(frequent_items, i))

    # Filter out infrequent itemsets
    frequent_itemsets = [itemset for itemset in frequent_itemsets if all(item in frequent_items for item in itemset)]

    return frequent_itemsets


    
# write eclat report to csv file and save it    
def writeCSVFile(ecreport):
    filename = "eclat_report.csv"
    
    with open(filename, 'w') as csvfile: 
        ## write report to csv file
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerows(ecreport)
        # using system cls to clear console on windows
        os.system('cls')
        print('eclat report has been written to \n'+filename)
        os.system('color 2')
        os.system(filename)
