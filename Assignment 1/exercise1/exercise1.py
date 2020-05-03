import csv
import pandas as pd

myDict = {'apple': ['appl','appel','appal'], 'market': ['markt','markte','markat']} 
mylist = ['markat', 'boayt', 'appl', 'orng']
table_name = input("Enter your desired Table Name: ") + '.csv'

def identifyKey(Dict, List, table_name):
    List=[]
    Match=[]
    for key, values in myDict.items():
        for item in mylist:
            if item in values:
                List.append(item)
                Match.append(key)
    for item in mylist:
        if item not in List:
            List.append(item)
            Match.append(" ")
    writeToCsv(table_name, List, Match)

def writeToCsv(table_name, List, Match):
    with open(table_name, 'w', newline='') as csvfile:
        fieldnames = ['List', 'Match']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, j in zip(List, Match):
            writer.writerow({'List': i, 'Match': j})


identifyKey(myDict, mylist, table_name="exercise1.csv")