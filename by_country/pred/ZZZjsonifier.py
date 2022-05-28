import csv
import json 
import os

 # Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
 
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # establish primary key
            x = rows['NOC']
            if x in data:
                data[x].append(rows)
            else:
                data[x]=[rows]
            
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
          
# Decide the two file paths according to your
# computer system
def make_jsonS():
    # iterate over files in
    # that directory
    cwd = os.getcwd()
    print(cwd)
    file_list = os.listdir(cwd)
    
    # iterate over the files, changing the variables and applying the make json function
    for file in file_list:
        if '.csv' in str(file):
            json_name = file.split('.csv')[0]
            csvFilePath = f'{file}'
            jsonFilePath = f'{json_name}.json'
            # Call the make_json function
            make_json(csvFilePath, jsonFilePath)
make_jsonS()